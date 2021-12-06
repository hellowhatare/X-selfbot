import discord
from discord.ext import commands
from discord.ext.commands.cog import Cog
from cogs.utils.checks import get_user


'''Module for moderator commands.'''


class Mod(Cog):

    def __init__(self, bot):
        self.bot = bot

    def are_overwrites_empty(self, overwrites):
        """There is currently no cleaner way to check if a
        PermissionOverwrite object is empty"""
        original = [p for p in iter(overwrites)]
        empty = [p for p in iter(discord.PermissionOverwrite())]
        return original == empty

    @commands.command(pass_context=True)
    async def kick(self, ctx, user, *, reason=""):
        """Kicks a user (if you have the permission)."""
        user = get_user(ctx.message, user)
        if user:
            try:
                await user.kick(reason=reason)
                return_msg = "Kicked user `{}`".format(user.mention)
                if reason:
                    return_msg += " for reason `{}`".format(reason)
                return_msg += "."
                await ctx.message.edit(content=self.bot.bot_prefix + return_msg)
            except discord.Forbidden:
                await ctx.message.edit(content=self.bot.bot_prefix + 'Could not kick user. Not enough permissions.')
        else:
            return await ctx.message.edit(content=self.bot.bot_prefix + 'Could not find user.')


    # TODO: Add reason with ban
    @commands.command(aliases=['hban'], pass_context=True)     
    async def hackban(self, ctx, user_id: int):
        """Bans a user outside of the server."""
        author = ctx.message.author
        guild = author.guild

        user = guild.get_member(user_id)
        if user is not None:
            return await ctx.invoke(self.ban, user=user)

        try:
            await self.bot.http.ban(user_id, guild.id, 0)
            await ctx.message.edit(content=self.bot.bot_prefix + 'Banned user: %s' % user_id)
        except discord.NotFound:
            await ctx.message.edit(content=self.bot.bot_prefix + 'Could not find user. '
                               'Invalid user ID was provided.')
        except discord.errors.Forbidden:
            await ctx.message.edit(content=self.bot.bot_prefix + 'Could not ban user. Not enough permissions.')


    @commands.command(pass_context=True)
    async def ban2(self, ctx, user, *, reason=""):
        """Bans a user (if you have the permission)."""
        user = get_user(ctx.message, user)
        if user:
            try:
                await user.ban(reason=reason)
                return_msg = "Banned user `{}`".format(user.mention)
                if reason:
                    return_msg += " for reason `{}`".format(reason)
                return_msg += "."
                await ctx.message.edit(content=self.bot.bot_prefix + return_msg)
            except discord.Forbidden:
                await ctx.message.edit(content=self.bot.bot_prefix + 'Could not ban user. Not enough permissions.')
        else:
            return await ctx.message.edit(content=self.bot.bot_prefix + 'Could not find user.')

    @commands.command(aliases=['sban'], pass_context=True)
    async def softban(self, ctx, user, *, reason=""):
        """Bans and unbans a user (if you have the permission)."""
        user = get_user(ctx.message, user)
        if user:
            try:
                await user.ban(reason=reason)
                await ctx.guild.unban(user)
                return_msg = "Banned and unbanned user `{}`".format(user.mention)
                if reason:
                    return_msg += " for reason `{}`".format(reason)
                return_msg += "."
                await ctx.message.edit(content=self.bot.bot_prefix + return_msg)
            except discord.Forbidden:
                await ctx.message.edit(content=self.bot.bot_prefix + 'Could not softban user. Not enough permissions.')
        else:
            return await ctx.message.edit(content=self.bot.bot_prefix + 'Could not find user.')



def setup(bot):
    bot.add_cog(Mod(bot))
