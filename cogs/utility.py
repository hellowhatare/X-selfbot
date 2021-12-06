import datetime
import asyncio
from discord.ext.commands.cog import Cog
import pytz
import re
import requests
import discord
import os
import glob
import io
from PIL import Image
from discord.ext import commands
from cogs.utils.checks import *
from bs4 import BeautifulSoup
from urllib import parse
from math import sqrt
from cogs.utils.dataIO import dataIO
from cogs.utils.config import write_config_value

'''Module for fun/meme commands commands'''


class Utility(Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def get_datetime():
        a = None
        tzerror = False
        opt = dataIO.load_json('settings/optional_config.json')
        try:
            if opt['timezone']:
                tz = opt['timezone']
                a = pytz.timezone(tz)
        except IndexError:
            # Timezone entry missing in configuration file
            pass
        except pytz.exceptions.UnknownTimeZoneError:
            tzerror = True
        return datetime.datetime.now(a), tzerror

    @commands.command(pass_context=True)
    async def now(self, ctx):
        """Date time module."""
        opt = dataIO.load_json('settings/optional_config.json')
        thebool = True
        try:
            if opt['24hours'] == "true":
                thebool = True
            else:
                thebool = False
        except IndexError:
            # No 24 hour bool given so default to true
            pass
        dandt, tzerror = self.get_datetime()
        if embed_perms(ctx.message):
            em = discord.Embed(color=discord.Color.blue())
            if thebool:
                em.add_field(name=u'\u23F0 Time', value="{:%H:%M:%S}".format(dandt), inline=False)
            else:
                em.add_field(name=u'\u23F0 Time', value="{:%I:%M:%S %p}".format(dandt), inline=False)
            em.add_field(name=u'\U0001F4C5 Date', value="{:%d %B %Y}".format(dandt), inline=False)
            if tzerror:
                em.add_field(name=u'\u26A0 Warning', value="Invalid timezone specified, system timezone was used instead.", inline=False)

            await ctx.send(content=None, embed=em)
        else:
            msg = '**Local Date and Time:** ```{:Time: %H:%M:%S\nDate: %Y-%m-%d```}'.format(dandt)
            await ctx.send(self.bot.bot_prefix + msg)
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def time(self, ctx):
        """Show current time"""
        opt = dataIO.load_json('settings/optional_config.json')
        thebool = True
        try:
            if opt['24hours'] == "true":
                thebool = True
            else:
                thebool = False
        except IndexError:
            # No 24 hour bool given so default to true
            pass
        await ctx.message.delete()
        dandt, tzerror = self.get_datetime()
        if thebool:
            returnstring = '{:Time: `%H:%M:%S`}'.format(dandt)
        else:
            returnstring = '{:Time: `%I:%M:%S %p`}'.format(dandt)
        msg = returnstring
        await ctx.send(self.bot.bot_prefix + msg)

    @commands.command(pass_context=True)
    async def date(self, ctx):
        """Show current date"""
        await ctx.message.delete()
        dandt, tzerror = self.get_datetime()
        msg = '{:Date: `%d %B %Y`}'.format(dandt)
        await ctx.send(self.bot.bot_prefix + msg)

    @commands.command(pass_context=True)
    async def code(self, ctx, *, msg):
        """Write text in code format."""
        await ctx.message.delete()
        await ctx.send("```" + msg.replace("`", "") + "```")
    
    @commands.command(pass_context=True)
    async def toggletime(self, ctx):
        """Toggle between 24 hours time and 12 hours time"""
        opt = dataIO.load_json('settings/optional_config.json')
        try:
            if opt['24hours'] == "true":
                write_config_value("optional_config", "24hours", "false")
                await ctx.send(self.bot.bot_prefix + "Set time to `12 hour` clock")
            else:
                write_config_value("optional_config", "24hours", "true")
                await ctx.send(self.bot.bot_prefix + "Set time to `24 hour` clock")
        except:
            # Nothing was set, so changing the default to 12hrs
            write_config_value("optional_config", "24hours", "false")
            await ctx.send(self.bot.bot_prefix + "Set time to `12 hour` clock")

    @commands.command(pass_context=True)
    async def timezone(self, ctx, *, msg):
        """Set preferred timezone. Use the timezonelist for a full list of timezones."""
        write_config_value("optional_config", "timezone", msg)
        await ctx.send(self.bot.bot_prefix + 'Preferred timezone has been set.')

    @commands.command(pass_context=True)
    async def timezonelist(self, ctx):
        """List all available timezones for the timezone command."""
        await ctx.message.delete()
        embed = discord.Embed()
        embed.description = "[List of valid timezones](https://gist.github.com/anonymous/67129932414d0b82f58758a699a5a0ef)"
        await ctx.send("", embed=embed)

    @commands.command(pass_context=True)
    async def cmdprefix(self, ctx, *, msg):
        """Set your command prefix for normal commands. Requires a reboot."""
        write_config_value("config", "cmd_prefix", msg)
        await ctx.send(self.bot.bot_prefix + 'Prefix changed. Use `restart` to reboot the bot for the updated prefix.')

    @commands.command(pass_context=True)
    async def customcmdprefix(self, ctx, *, msg):
        """Set your command prefix for custom commands."""
        write_config_value("config", "customcmd_prefix", msg)
        self.bot.customcmd_prefix = msg
        await ctx.send(self.bot.bot_prefix + 'Prefix changed.')

    @commands.command(pass_context=True)
    async def botprefix(self, ctx, *, msg):
        """Set bot prefix"""
        write_config_value("config", "bot_identifier", msg)
        self.bot.bot_prefix = msg + ' '
        await ctx.send(self.bot.bot_prefix + 'Prefix changed.')

    @commands.command(pass_context=True)
    async def calc1(self, ctx, *, msg):
        """Simple calculator. Ex: [p]calc 2+2"""
        equation = msg.strip().replace('^', '**').replace('x', '*')
        try:
            if '=' in equation:
                left = eval(equation.split('=')[0], {"__builtins__": None}, {"sqrt": sqrt})
                right = eval(equation.split('=')[1], {"__builtins__": None}, {"sqrt": sqrt})
                answer = str(left == right)
            else:
                answer = str(eval(equation, {"__builtins__": None}, {"sqrt": sqrt}))
        except TypeError:
            return await ctx.send(self.bot.bot_prefix + "Invalid calculation query.")
        if embed_perms(ctx.message):
            em = discord.Embed(color=0xD3D3D3, title='Calculator')
            em.add_field(name='Input:', value=msg.replace('**', '^').replace('x', '*'), inline=False)
            em.add_field(name='Output:', value=answer, inline=False)
            await ctx.send(content=None, embed=em)
            await ctx.message.delete()
        else:
            await ctx.send(self.bot.bot_prefix + answer)


    @commands.command(pass_context=True)
    async def ud(self, ctx, *, msg):
        """Pull data from Urban Dictionary. Use [p]help ud for more information.
        Usage: [p]ud <term> - Search for a term on Urban Dictionary.
        You can pick a specific result to use with [p]ud <term> | <result>.
        If no result is specified, the first result will be used.
        """
        await ctx.message.delete()
        number = 1
        if " | " in msg:
            msg, number = msg.rsplit(" | ", 1)
        search = parse.quote(msg)
        async with self.bot.session.get("http://api.urbandictionary.com/v0/define", params={"term": search}) as resp:
            result = await resp.json()
        if not result["list"]:
            await ctx.send(self.bot.bot_prefix + "{} couldn't be found on Urban Dictionary.".format(msg))
        else:
            try:
                top_result = result["list"][int(number) - 1]
                embed = discord.Embed(title=top_result["word"], description=top_result["definition"],
                                      url=top_result["permalink"])
                if top_result["example"]:
                    embed.add_field(name="Example:", value=top_result["example"])
                embed.set_author(name=top_result["author"],
                                 icon_url="https://lh5.ggpht.com/oJ67p2f1o35dzQQ9fVMdGRtA7jKQdxUFSQ7vYstyqTp-Xh-H5BAN4T5_abmev3kz55GH=w300")
                number = str(int(number) + 1)
                embed.set_footer(text="{} results were found. To see a different result, use >ud {} | {}.".format(
                    len(result["list"]), msg, number))
                await ctx.send("", embed=embed)
            except IndexError:
                await ctx.send(self.bot.bot_prefix + "That result doesn't exist! Try >ud {}.".format(msg))

    @commands.command(pass_context=True, aliases=['vid', 'video'])
    async def youtube2(self, ctx, *, msg):
        """Search for videos on YouTube."""
        search = parse.quote(msg)
        youtube_regex = re.compile('\/watch\?v=[\d\w\-]*')
        async with self.bot.session.get("https://www.youtube.com/results", params={"search_query": search}) as resp:
            response = await resp.text()
        await ctx.message.delete()
        url = youtube_regex.findall(response)[0]
        await ctx.send("https://www.youtube.com{}".format(url))

    @commands.command(pass_context=True)
    async def xkcd(self, ctx, *, comic=""):
        """Pull comics from xkcd."""
        if comic == "random":
            randcomic = requests.get("https://c.xkcd.com/random/comic/".format(comic))
            comic = randcomic.url.split("/")[-2]
        site = requests.get("https://xkcd.com/{}/info.0.json".format(comic))
        if site.status_code == 404:
            site = None
            found = None
            search = parse.quote(comic)
            async with self.bot.session.get("https://www.google.co.nz/search?&q={}+site:xkcd.com".format(search)) as resp:
                result = await resp.text()
            soup = BeautifulSoup(result, "html.parser")
            links = soup.find_all("cite")
            for link in links:
                if link.text.startswith("https://xkcd.com/"):
                    found = link.text.split("/")[3]
                    break
            if not found:
                await ctx.send(self.bot.bot_prefix + "That comic doesn't exist!")
            else:
                site = requests.get("https://xkcd.com/{}/info.0.json".format(found))
                comic = found
        if site:
            json = site.json()
            embed = discord.Embed(title="xkcd {}: {}".format(json["num"], json["title"]), url="https://xkcd.com/{}".format(comic))
            embed.set_image(url=json["img"])
            embed.set_footer(text="{}".format(json["alt"]))
            await ctx.send("", embed=embed)

    @commands.command(pass_context=True)
    async def whoisplaying(self, ctx, *, game):
        """Check how many people are playing a certain game."""
        msg = ""
        for guild in self.bot.guilds:
            for user in guild.members:
                if user.activity is not None:
                    if user.activity.name is not None:
                        if user.activity.name.lower() == game.lower():
                            msg += "{}#{}\n".format(user.name, user.discriminator)
        msg = "\n".join(set(msg.split("\n")))  # remove dupes
        if len(msg) > 1500:
            hastebin_output = await hastebin(msg, self.bot.session)
            await ctx.send("{}Large output posted to Hastebin: {}".format(self.bot.bot_prefix, hastebin_output))
        elif len(msg) == 0:
            await ctx.send(self.bot.bot_prefix + "Nobody is playing that game!")
        else:
            embed = discord.Embed(title="Number of people playing {}".format(game), description=msg)
            await ctx.send("", embed=embed)
            
    @commands.command(pass_context=True, aliases=['anim'])
    async def animate(self, ctx, animation):
        """Play an animation from a text file. [p]help animate for more details.
        [p]animate <animation> - Animate a text file.
        Animation text files are stored in the anims folder. Each frame of animation is put on a new line.

        An example text file looks like this:
        family
        fam ily
        fam i ly
        fam i love y
        fam i love you

        You can additionally add a number to the top of the file to denote the delay between each frame. The default is 0.2 seconds.
        1
        fam
        fam i
        fam i love
        fam i love you
        """
        try:
            with open("anims/{}.txt".format(animation), encoding="utf-8") as f:
                anim = f.read().split("\n")
        except IOError:
            return await ctx.send(self.bot.bot_prefix + "You don't have that animation in your `anims` folder!")
        if anim:
            try:
                delay = float(anim[0])
                for frame in anim[1:]:
                    await ctx.message.edit(content=frame)
                    await asyncio.sleep(delay)
            except ValueError:
                for frame in anim:
                    await ctx.message.edit(content=frame)
                    await asyncio.sleep(0.2)

    @commands.command(pass_context=True)
    async def roles(self, ctx, *, user=None):
        """Check the roles of a user."""
        await ctx.message.delete()
        if not user:
            member = ctx.message.author
        else:
            member = get_user(ctx.message, user)
        if not member:
            await ctx.send(self.bot.bot_prefix + "That user couldn't be found. Please check your spelling and try again.")
        elif len(member.roles[1:]) >= 1:
            embed = discord.Embed(title="{}'s roles".format(member.name), description="\n".join([x.name for x in member.roles[1:]]), colour=member.colour)
            await ctx.send("", embed=embed)
        else:
            await ctx.send(self.bot.bot_prefix + "That user has no roles!")

    @commands.command(pass_context=True)
    async def messagedump(self, ctx, limit, filename, details="yes", reverse="no"):
        """Dump messages."""
        await ctx.message.delete()
        await ctx.send(self.bot.bot_prefix + "Downloading messages...")
        if not os.path.isdir('message_dump'):
            os.mkdir('message_dump')
        with open("message_dump/" + filename.rsplit('.', 1)[0] + ".txt", "w+", encoding="utf-8") as f:
            if reverse == "yes":
                if details == "yes":
                    async for message in ctx.message.channel.history(limit=int(limit)):
                        f.write("<{} at {} on {}> {}\n".format(message.author.name, message.created_at.strftime('%d %b %Y'), message.created_at.strftime('%H:%M:%S'), message.content))

                else:
                    async for message in ctx.message.channel.history(limit=int(limit)):
                        f.write(message.content + "\n")
            else:
                if details == "yes":
                    async for message in ctx.message.channel.history(limit=int(limit), reverse=True):
                        f.write("<{} at {} on {}> {}\n".format(message.author.name, message.created_at.strftime('%d %b %Y'), message.created_at.strftime('%H:%M:%S'), message.content))

                else:
                    async for message in ctx.message.channel.history(limit=int(limit), reverse=True):
                        f.write(message.content + "\n")
        await ctx.send(self.bot.bot_prefix + "Finished downloading!")

    @commands.group(pass_context=True)
    async def link(self, ctx):
        """Shorten/lengthen URLs"""
        await ctx.message.delete()
        if ctx.invoked_subcommand is None:
            await ctx.send(self.bot.bot_prefix + "Usage: `link <shorten/lengthen> <url>`")

    @link.command(pass_context=True)
    async def shorten(self, ctx, url):
        try:
            r = requests.get(url).status_code
        except requests.exceptions.RequestException:
            r = 404
        if r == 200:
            params = {
                "access_token": "757c24db53fac6a6a994439da41bdbbe325dfb99",
                "longUrl": url
            }
            response = requests.get("https://api-ssl.bitly.com/v3/shorten", params=params)
            if response.status_code == 200:
                await ctx.send(self.bot.bot_prefix + "<{}>".format(response.json()["data"]["url"]))
            else:
                await ctx.send(self.bot.bot_prefix + "There was an error shortening your URL.")
        else:
            await ctx.send(self.bot.bot_prefix + "You did not enter a valid URL.")

    @link.command(pass_context=True)
    async def lengthen(self, ctx, url):
        try:
            r = requests.get(url).status_code
        except requests.exceptions.RequestException:
            r = 404
        if r == 200:
            await ctx.send(self.bot.bot_prefix + "<{}>".format(requests.get(url).url))
        else:
            await ctx.send(self.bot.bot_prefix + "You did not enter a valid URL.")

    @commands.command(pass_context=True, aliases=['getcolor'])
    async def getcolour(self, ctx, *, colour_codes):
        """Posts color of given hex"""
        await ctx.message.delete()
        colour_codes = colour_codes.split()
        size = (60, 80) if len(colour_codes) > 1 else (200, 200)
        if len(colour_codes) > 5:
            return await ctx.send(self.bot.bot_prefix + "Sorry, 5 colour codes maximum")
        for colour_code in colour_codes:
            if not colour_code.startswith("#"):
                colour_code = "#" + colour_code
            image = Image.new("RGB", size, colour_code)
            with io.BytesIO() as file:
                image.save(file, "PNG")
                file.seek(0)
                await ctx.send("Colour with hex code {}:".format(colour_code), file=discord.File(file, "colour_file.png"))
            await asyncio.sleep(1)  # Prevent spaminess

    @commands.has_permissions(add_reactions=True)
    @commands.command(pass_context=True)
    async def poll(self, ctx, *, msg):
        """Create a poll using reactions. [p]help poll for more information.
        [p]poll <question> | <answer> | <answer> - Create a poll. You may use as many answers as you want, placing a pipe | symbol in between them.
        Example:
        [p]poll What is your favorite anime? | Steins;Gate | Naruto | Attack on Titan | Shrek
        You can also use the "time" flag to set the amount of time in seconds the poll will last for.
        Example:
        [p]poll What time is it? | HAMMER TIME! | SHOWTIME! | time=10
        """
        await ctx.message.delete()
        options = msg.split(" | ")
        time = [x for x in options if x.startswith("time=")]
        if time:
            time = time[0]
        if time:
            options.remove(time)
        if len(options) <= 1:
            return await ctx.send(self.bot.bot_prefix + "You must have 2 options or more.")
        if len(options) >= 11:
            return await ctx.send(self.bot.bot_prefix + "You must have 9 options or less.")
        if time:
            time = int(time.strip("time="))
        else:
            time = 30
        emoji = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣']
        to_react = []
        confirmation_msg = "**{}?**:\n\n".format(options[0].rstrip("?"))
        for idx, option in enumerate(options[1:]):
            confirmation_msg += "{} - {}\n".format(emoji[idx], option)
            to_react.append(emoji[idx])
        confirmation_msg += "\n\nYou have {} seconds to vote!".format(time)
        poll_msg = await ctx.send(confirmation_msg)
        for emote in to_react:
            await poll_msg.add_reaction(emote)
        await asyncio.sleep(time)
        async for message in ctx.message.channel.history():
            if message.id == poll_msg.id:
                poll_msg = message
        results = {}
        for reaction in poll_msg.reactions:
            if reaction.emoji in to_react:
                results[reaction.emoji] = reaction.count - 1
        end_msg = "The poll is over. The results:\n\n"
        for result in results:
            end_msg += "{} {} - {} votes\n".format(result, options[emoji.index(result)+1], results[result])
        top_result = max(results, key=lambda key: results[key])
        if len([x for x in results if results[x] == results[top_result]]) > 1:
            top_results = []
            for key, value in results.items():
                if value == results[top_result]:
                    top_results.append(options[emoji.index(key)+1])
            end_msg += "\nThe victory is tied between: {}".format(", ".join(top_results))
        else:
            top_result = options[emoji.index(top_result)+1]
            end_msg += "\n{} is the winner!".format(top_result)
        await ctx.send(end_msg)

    @commands.command(aliases=['clist'])
    async def loaded(self, ctx):
        """Shows loaded/unloaded cogs"""
        await ctx.message.delete()
        core_cogs = []
        custom = []
        cogs = ["cogs." + os.path.splitext(f)[0] for f in [os.path.basename(f) for f in glob.glob("cogs/*.py")]]
        custom_cogs = ["custom_cogs." + os.path.splitext(f)[0] for f in [os.path.basename(f) for f in glob.glob("custom_cogs/*.py")]]
        loaded = [x.__module__.split(".")[1] for x in self.bot.cogs.values()]
        unloaded = [c.split(".")[1] for c in cogs
                    if c.split(".")[1] not in loaded]
        embed = discord.Embed(title="List of installed cogs")
        cogs = [w.replace('cogs.', '') for w in cogs]
        custom_cogs = [w.replace('custom_cogs.', '') for w in custom_cogs]
        for cog in loaded:
            if cog in cogs:
                core_cogs.append(cog)
            if cog in custom_cogs:
                custom.append(cog)
        if core_cogs:
            embed.add_field(name="Core Loaded", value="\n".join(sorted(core_cogs)), inline=True)
        if custom:
            embed.add_field(name="Custom Loaded", value="\n".join(sorted(custom)), inline=True)
        if not custom and not core_cogs:
            embed.add_field(name="Loaded", value="None!", inline=True)
        if unloaded:
            embed.add_field(name="Not Loaded", value="\n".join(sorted(unloaded)), inline=True)
        else:
            embed.add_field(name="Not Loaded", value="None!", inline=True)
        await ctx.send("", embed=embed)

    @commands.command(pass_context=True, aliases=['clearconsole', 'cc', 'clear'])
    async def cleartrace(self, ctx):
        """Clear the console."""
        if os.name == 'nt':
            os.system('cls')
        else:
            try:
                os.system('clear')
            except Exception:
                for _ in range(100):
                    print()

        message = 'Logged in as %s.' % self.bot.user
        uid_message = 'User id: %s.' % self.bot.user.id
        separator = '-' * max(len(message), len(uid_message))
        print(separator)
        try:
            print(message)
        except: # some bot usernames with special chars fail on shitty platforms
            print(message.encode(errors='replace').decode())
        print(uid_message)
        print(separator)
        await ctx.send(self.bot.bot_prefix + 'Console cleared successfully.')
        
    @commands.command()
    async def read(self, ctx, id: int=None):
        """Marks a specified server as read. If an ID is not provided, all servers will be marked as read."""
        await ctx.message.delete()
        if id:
            guild = self.bot.get_guild(int(id))
            if guild:
                await guild.ack()
                await ctx.send(self.bot.bot_prefix + "Marked {} as read.".format(guild.name))
            else:
                await ctx.send(self.bot.bot_prefix + "Invalid server ID.")
        else:
            for guild in self.bot.guilds:
                await guild.ack()
            await ctx.send(self.bot.bot_prefix + "Marked {} guilds as read.".format(len(self.bot.guilds)))
            

def setup(bot):
    bot.add_cog(Utility(bot))
