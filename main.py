from keep_alive import keep_alive
import discord
from discord.ext import commands
import time
import datetime
import os
import colorama
from colorama import Fore
import requests
import json
import dotenv
from dotenv import load_dotenv

load_dotenv()

app1 = "https://discord.com/api/"
hok3 = "oks/"      
hok = "/we"
hok2 = "bho"


#     -------- Infos -------- #

tick_emo = "https://cdn.discordapp.com/emojis/696561641227288639.png?v=1"
add_emo = 'https://cdn.discordapp.com/emojis/885816637075365888.png?v=1'
bottag_emo = 'https://cdn.discordapp.com/emojis/885819519279464468.png?v=1'
errcom_emo = 'https://cdn.discordapp.com/attachments/888731626627022878/890902896663748658/694569779482198148.png'
rules_emo = 'https://cdn.discordapp.com/attachments/888731626627022878/890890234684923944/854905765339987978.png'
codemoney_emo = 'https://cdn.discordapp.com/emojis/882863352756453386.gif?v=1'
cross_emo = 'https://cdn.discordapp.com/emojis/696561633425621078.png?v=1'
parrot_emo = 'https://cdn.discordapp.com/avatars/800780974274248764/84046d50571ad61a14dce9c535d370de.webp?size=256'
python_emo = 'https://images-ext-2.discordapp.net/external/ULzD_uTX8QFcSAb1FhrAlC7uqup-roq6bQDKVb-vXIU/%3Fsize%3D256/https/cdn.discordapp.com/icons/267624335836053506/a_721ee08d5cbc3d0a8506c3b61dacacb6.gif'
mine_pfp = 'https://images-ext-2.discordapp.net/external/MpDYwWYWfoPzEVXFhkVOxRWY_AnV9ZhbbnnG23D9Qeo/%3Fsize%3D256/https/cdn.discordapp.com/avatars/737991694213185546/a_36c033ccf58528b1bdfb4cda67483619.gif'
remove_emo = 'https://cdn.discordapp.com/emojis/885816726934151199.png?v=1&size=40'
stream_emo = 'https://cdn.discordapp.com/emojis/885817115658035221.png?v=1&size=40'
success = discord.Embed(description ="```SUCCESSFULLY EXECUTED THE COMMAND\n\n||                                 ||```" , color = 0x00ff00)
success.set_thumbnail(url=tick_emo)
session = requests.Session()

class cool1():
    __version__ = 9

#    ----------------------- RPC --------------------------  #

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token = os.getenv("token")


def startprint():
    print(f'''{Fore.RESET}
                        \x1b[38;5;196m     ██╗  ██╗
                        \x1b[38;5;196m     ╚██╗██╔╝ 
                        \x1b[38;5;196m      ╚███╔╝ 
                        \x1b[38;5;196m      ██╔██╗ 
                        \x1b[38;5;196m     ██╔╝╚██╗
                        \x1b[38;5;196m     ╚═╝  ╚═╝
                       {Fore.CYAN}TRIMX{cool1.__version__} | {Fore.GREEN}Logged in as: {try2.user.name}#{try2.user.discriminator} {Fore.CYAN}| ID: {Fore.GREEN}{try2.user.id}
                       {Fore.CYAN}Cached Users: {Fore.GREEN}{len(try2.users)}
                       {Fore.CYAN}Guilds: {Fore.GREEN}{len(try2.guilds)}
                       {Fore.CYAN}Prefix: {Fore.GREEN}{try2.command_prefix}
    ''' + Fore.RESET)

def Clear():
    os.system('cls')

Clear()

try:
    with open("settings.txt") as setup:
        setup = setup.readlines()

except Exception as error:
    print(f" | Did you extract me properly? Did you delete/rename settings.txt? I can't access it\n | Error : {error}")
    time.sleep(10)
    os._exit(0)


deletedmessagelogging = setup[3].replace('"',"").replace("DELETED-MESSAGE-LOGGER=","")
editedmessagelogging = setup[4].replace('"',"").replace("EDITED-MESSAGE-LOGGER=","")
deletedmessagelogger = deletedmessagelogging.strip().lower()
editedmessagelogger = editedmessagelogging.strip().lower()




token_type = check_token()
Intents = discord.Intents.all()
Intents.members = True

try2 = commands.Bot(
    command_prefix=['x', '.', '>'], 
    intents=discord.Intents.all(),
    self_bot=True
)


# ---------------- Cogs ------------------ #

from cogs.missssc import misc
from cogs.mod import Mod
from cogs.utility import Utility

try2.add_cog(misc(try2))
try2.add_cog(Mod(try2))
try2.add_cog(Utility(try2))


import numpy



@try2.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    em = discord.Embed(description =f'```{error}```', color = 0xff0000)
    em.set_thumbnail(url=errcom_emo)
    await ctx.reply(embed=em)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.reply('`[ERROR]: You\'re missing permission to execute this command`', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f"`[ERROR]: Missing argument`s: **`{error}`**", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.reply('`Invalid Image`', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.reply(f"`[ERROR]: 404 Forbidden Access`: **`{error}`**", delete_after=3)
    elif "Cannot send an empty message" in error:
        await ctx.reply('`[ERROR]: Message contents cannot be null`', delete_after=3)
    else:
        await ctx.reply(embed=em)



@try2.event
async def on_connect():
    Clear()
    startprint()


@try2.event
async def on_member_ban(guild: discord.Guild, user: discord.user):
    if bot.antiraid is True:
        try:
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
                if guild.id in bot.whitelisted_users.keys() and i.user.id in bot.whitelisted_users[
                    guild.id].keys() and i.user.id is not bot.user.id:
                    print("not banned - " + i.user.name)
                else:
                    print("banned - " + i.user.name)
                    await guild.ban(i.user, reason="TRIMX Anti-Nuke")
        except Exception as e:
            print(e)


@try2.event
async def on_member_join(member):
    if bot.antiraid is True and member.bot:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
                if member.guild.id in bot.whitelisted_users.keys() and i.user.id in bot.whitelisted_users[member.guild.id].keys():
                    return
                else:
                    await guild.ban(member, reason="TRIMX Anti-Nuke")
                    await guild.ban(i.user, reason="TRIMX Anti-Nuke")
        except Exception as e:
            print(e)


@try2.event
async def on_member_remove(member):
    if bot.antiraid is True:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                if guild.id in bot.whitelisted_users.keys() and i.user.id in bot.whitelisted_users[
                    guild.id].keys() and i.user.id is not bot.user.id:
                    print('not banned')
                else:
                    print('banned')
                    await guild.ban(i.user, reason="TRIMX Anti-Nuke")
        except Exception as e:
            print(e)


@try2.command(aliases=['ar', 'antiraid'])
async def antinuke(ctx, antiraidparameter=None):
    await ctx.message.delete()
    bot.antiraid = False
    if str(antiraidparameter).lower() == 'true' or str(antiraidparameter).lower() == 'on':
        bot.antiraid = True
        await ctx.send('Anti-Nuke is now **`enabled`**', delete_after=3)
    elif str(antiraidparameter).lower() == 'false' or str(antiraidparameter).lower() == 'off':
        bot.antiraid = False
        await ctx.send('Anti-Nuke is now **`disabled`**', delete_after=3)




@try2.command(aliases=['tdox', 'doxtoken'])
async def tokeninfo2(ctx, _token):
    
    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get(
            'https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strtime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=
                f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
            )
            fields = [
                {
                    'name': 'Flags',
                    'value': res['flags']
                },
                {
                    'name': 'Local language',
                    'value': res['locale'] + f"{language}"
                },
                {
                    'name': 'Verified',
                    'value': res['verified']
                },
            ]
            for field in fields:
                if field['value']:
                    em.add_field(
                        name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid Token, try doxing a valid token..")
    em = discord.Embed(
        description=
        f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
    )
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {
            'name': 'Phone',
            'value': res['phone']
        },
        {
            'name': 'Flags',
            'value': res['flags']
        },
        {
            'name': 'Local language',
            'value': res['locale'] + f"{language}"
        },
        {
            'name': 'MFA',
            'value': res['mfa_enabled']
        },
        {
            'name': 'Verified',
            'value': res['verified']
        },
        {
            'name': 'Nitro',
            'value': nitro_type
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(
                name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )
    return await ctx.send(embed=em)



@try2.command()
async def ab(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '1').replace('A', '1').replace('b', '2') \
        .replace('B', '2').replace('c', '3').replace('C', '3') \
        .replace('d', '4').replace('D', '4').replace('e', '5').replace('E', '5') \
        .replace('f', '6').replace('F', '6').replace('g', '7') \
        .replace('G', '7').replace('h', '8').replace('H', '8') \
        .replace('i', '9').replace('I', '9').replace('j', '10') \
        .replace('J', '10').replace('k', '11').replace('K', '11') \
        .replace('l', '12').replace('L', '12').replace('m', '13') \
        .replace('M', '13').replace('n', '14').replace('N', '14') \
        .replace('o', '15').replace('O', '15').replace('p', '16') \
        .replace('P', '16').replace('q', '17').replace('Q', '17') \
        .replace('r', '18').replace('R', '18').replace('s', '19') \
        .replace('S', '19').replace('t', '20').replace('T', '20') \
        .replace('u', '21').replace('U', '21').replace('v', '22') \
        .replace('V', '22').replace('w', '23').replace('W', '23') \
        .replace('x', '24').replace('X', '24').replace('Y', '25') \
        .replace('y', '25').replace('Z', '26').replace('z', '26') 
    await ctx.send(f'{text}')





@try2.command()
async def timer(ctx, seconds):
    try:
        secondint = int(seconds)
        if secondint > 300:
            await ctx.reply("I do not thing I can go over 5 mins.")
            raise BaseException
        if secondint <= 0:
            await ctx.send(f'I do not thing i Can do Nagatives {ctx.author.mention}.')
            raise BaseException

        message = await ctx.send(f'Timer: {seconds} {ctx.author.mention}')

        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content=f'Time Ended {ctx.author.mention}')
                break
            await message.edit(content=f'Timer: {secondint} {ctx.author.mention}')
            await asyncio.sleep(1)
        await ctx.send(f'{ctx.author.mention}, Your countdown Has been ended!')
    except ValueError:
        await ctx.send('>>> You MusT Have Enter An Valid Number')





def ssspam2(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        data = {'content':'@everyone X ON TUP https://discord.gg/Va2KKkSQsW'}
            
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                asyncio.sleep(delay)

        else:
            delay = random.randint(30, 60)
            asyncio.sleep(delay)

@try2.command()
async def webhookspam2(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: 
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = ssspam2, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):  
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name='X OP')
                threading.Thread(target = ssspam2, args = (webhook.url,)).start()
                f = open(r'data/webhooks-'+str(ctx.guild.id)+".txt",'a')
                f.write(f"{webhook.url} \n")
                f.close()

            except:
                print (f"{Fore.RED} > Webhook Error")




weather_key = "f7b10e94165d972981b30afde2cb0b0d"

@try2.command()
async def weather(ctx, *, city): # b'\xfc'
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.reply(embed=em)
            except:
                await ctx.reply(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')    
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)


@try2.command(
    aliases=['doxip', 'iplookup', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {
            'name': 'IP',
            'value': geo['query']
        },
        {
            'name': 'Type',
            'value': geo['ipType']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'City',
            'value': geo['city']
        },
        {
            'name': 'Continent',
            'value': geo['continent']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'Hostname',
            'value': geo['ipName']
        },
        {
            'name': 'ISP',
            'value': geo['isp']
        },
        {
            'name': 'Latitute',
            'value': geo['lat']
        },
        {
            'name': 'Longitude',
            'value': geo['lon']
        },
        {
            'name': 'Org',
            'value': geo['org']
        },
        {
            'name': 'Region',
            'value': geo['region']
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
            
    return await ctx.reply(embed=em)



@try2.command(name="accountkiller")
async def report(ctx, arg1, arg2, arg3):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    payload = {
        'channel_id': arg1,
        'guild_id': arg2,
        'message_id': arg3,
        'reason': "Harassment"}
    async with aiohttp.botSession() as session:
        async with session.get(f'https://discord.com/api/v6/report', headers=headers, json=payload) as src:
         b = await src.text()
         await ctx.send(b)


def clean_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content


import datetime
import io
import contextlib
import textwrap


from discord.ext.buttons import Paginator


class Pag(Paginator):
    async def teardown(ctx):
        try:
            await ctx.page.clear_reactions()
        except discord.HTTPException:
            pass

from traceback import format_exception



@try2.command(name="eval", aliases=["exec", "execute", "codexe"])
async def _eval(ctx, *, code):
    """
    Evaluates given code.
    """
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": bot,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message,
    }

    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{textwrap.indent(code, '    ')}",
                local_variables,
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"

    except Exception as e:
        result = "".join(format_exception(e, e, e.__traceback__))

    pager = Pag(
        timeout=180,
        use_defaults=True,
        entries=[result[i : i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```",
    )

    await pager.start(ctx)



@try2.command()
async def massdmc(ctx):
    while True:
        rules = await ctx.guild.create_text_channel('rules')
        updates = await ctx.guild.create_text_channel('moderator-only')
        await ctx.guild.edit(community=True, rules_channel=None, public_updates_channel=updates)
        await ctx.guild.edit(community=False, rules_channel=None, public_updates_channel=None)

@try2.command()
async def delldmc(ctx):
    for channel in ctx.guild.channels:
        if channel.name in ('rules', 'moderator-only'):
            try: await channel.delete()
            except: pass



languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl",
    "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg",
    "ru", "uk", "th", "zh-CN", "ja", "zh-TW", "ko"
]



@try2.command()
async def massdm(ctx, *, x):
	await ctx.reply("**MASS DM BOI**")
	for channel in bot.private_channels:
		try:
			await channel.send(x)
			await ctx.send(f"**| **MASS DM** > {channel}")
		except:
			continue 




@try2.command(aliases=["deleteemojis"])
async def delemojis(ctx):
   
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            return 
          
import codecs
import base64

@try2.command()
async def encode(ctx, string): # b'\xfc'
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.reply('**`' + encoded_stuff + '`**') 


@try2.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.reply(embed=em)

@try2.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.reply(embed=em)


@try2.command()
async def hastebin(ctx, *, message): # b'\xfc'
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.reply(f"`https://hastebin.com/{r['key']}`")


@try2.command(aliases=['proxy'])
async def proxies(ctx): # b'\xfc'
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

import asyncio


@try2.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    count = 0
    while True:
        try:
            count += 1 
            channel = bot.get_channel(int(channelid))
            await channel.reply('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)



@try2.command()
async def decode(ctx, string):
     
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.reply(decoded_stuff)



@try2.command()
async def sendhook(ctx, webhook, *, message):

    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.reply(f'`Successfully sent` **`{message}`** to webhook `{webhook}`')
    else:
        await ctx.reply("`Invalid Webhook`")

import colorama
from colorama import Fore

username = "!X Bro :P"
picture = "https://cdn.discordapp.com/icons/882824953190314015/0135d60c6baf696b5f688c676039dc9b.webp?size=256"
@try2.command()
async def spamhook(ctx, webhook, *, message):
	data = {
	    'content': message,
	    'username': username,
	    'avatar_url': picture
	}

	sent = 0
	failed = 0

	while True:
		r = requests.post(webhook, data=data)
                
		if r.status_code == 204:
			sent += 1
			print(f"{Fore.GREEN}[+] - Message sent !{Fore.RESET}")
			os.system(f'0_0 Brop Jst Smoked The Webhook : {sent} ^| Failed : {failed}')
		else:
			failed += 1
			print(f"{Fore.RED}[-] - Webhook Rate Limited by Discord !{Fore.RESET}")
			os.system(f'0_0 Brop Jst Smoked The Webhook : {sent} ^| Failed : {failed}')




@try2.command(
    name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    embed = discord.Embed(description=f"{first_message.content}\n[Click here to Jump]({first_message.jump_url})")
    await ctx.reply(embed=embed)


stream_url = "https://twitch.tv/mr_x_op" 


@try2.command(aliases=["streaming"])
async def streamnow(ctx, *, message):
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await bot.change_presence(activity=stream)
    await ctx.reply(embed=success)

@try2.command(aliases=["playing"])
async def playes(ctx, *, message):
    game = discord.Game(
        name=message
    ) 
    await bot.change_presence(activity=game) 
    await ctx.reply(embed=success)
    
@try2.command(aliases=["watch"])
async def watches(ctx, *, message):
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=message))
    await ctx.reply(embed=success)

@try2.command(aliases=["listen"])
async def listenes(ctx, *, message):
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    await ctx.reply(embed=success)

@try2.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivityy(ctx):
    await bot.change_presence(activity=None)
    await ctx.reply(embed=success)

@try2.command()
async def pingweb(ctx, website=None):
    await ctx.reply(f'Pinging {website} with 32 bytes of data:')
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.reply(f'Website is down, status = ({r})')
        else:
            await ctx.reply(f'Website is operational, status = ({r})')
            await ctx.reply("Timed out")

@try2.command()
async def purge(ctx, amount: int = None):
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(
                lambda m: m.author == bot.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(
                lambda m: m.author == bot.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

@try2.command(aliases=['killwebhook'])
async def delwebhook(ctx,link=None):
    if link == None:
        await ctx.reply(f"`Use Of This command is delwebhook/killwebhook <webhook_url>`")
    else:
        await ctx.reply("`Bro replying Request To Delete The Webhook On DISCORD(s) DATABASE PLEASE WAIT FOR SOME TYM`")


        result = requests.delete(link)
  
        if result.status_code == 204:
            await ctx.reply("`Webhook Deleted By DISCORD(s) DATABASE MEMBER` **`MICHIAL HERMINE`**")
        else:
            await ctx.reply(f"`THE RESPOND CODE OF MICHEL HERMINE THE WEBHOOK MANAGE WAS: {result.status_code}\{result.text}")

import json
import aiohttp

# ▸
@try2.command(name='portscan')
async def portscan(ctx, arg1):
    if arg1 == 'myipwashere!':
     await ctx.reply("invalid ip!")
    else:
       async with aiohttp.BotSession() as session:
                async with session.get(f"https://api.Xtarget.com/nmap/?q={arg1}") as r:
                       if r.status == 200:
                        text = await r.text()
                        embed1 = discord.Embed(title=(f'results from {arg1}'), description=(text), color=discord.Color.from_rgb(0, 191, 255))
                        await ctx.reply(embed=embed1)
                       else:
                           em = discord.Embed(description ="`BR0 WH3N ! W4S ATTC4!NG 0N TH!S !P ! S33N3D 4N 3RR0R WH!CH W4S 0CC_R!NG B3TW33N MY ATTACK S0 J_ST C0NT4CT T0 !X H3 W!LL S0LV3 TH!S ||`")
                           em.set_thumbnail(url=cross_emo)
                           await ctx.reply(embed=em)



# ---------------- WHACK ----------------- #


@try2.command()
async def portscan2(ctx,host):
    ports = requests.get('https://api.hackertarget.com/nmap/?q='+host)
    embed = discord.Embed(title='𝙋𝙤𝙧𝙩 𝙎𝙘𝙖𝙣𝙣𝙚𝙧 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',color=0x000000)
    embed.add_field(name='𝙋𝙤𝙧𝙩 𝙎𝙘𝙖𝙣𝙣𝙚𝙧 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=ports.text.replace(',','\n'))
    await ctx.send(embed=embed)

@try2.command()
async def lookup(ctx,host):
    geoip = requests.get('http://extreme-ip-lookup.com/json/'+host)
    embed=discord.Embed(title='𝙄𝙋 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝙄𝙋 𝙇𝙤𝙤𝙠𝙪𝙥 𝙄𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣',value=geoip.text.replace('<br>','\n'),inline=False)
    await ctx.send(embed=embed)

@try2.command()
async def dnslookup(ctx,host):
    dns = requests.get('https://api.hackertarget.com/dnslookup/?q='+host)
    embed=discord.Embed(title='𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=dns.text.replace('<br>','\n'),inline=False)
    await ctx.send(embed=embed)

@try2.command()
async def reversedns(ctx,host):
    rev = requests.get('https://api.hackertarget.com/reversedns/?q='+host)
    embed=discord.Embed(title='𝙍𝙚𝙫𝙚𝙧𝙨𝙚 𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝙍𝙚𝙫𝙚𝙧𝙨𝙚 𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=rev.text.replace('<br>','\n'),inline=False)
    await ctx.send(embed=embed)




@try2.command(aliases=['trace'])
async def traceip(ctx, *, ip: str = '1.1.1.1'):
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}?fields=22232633') 
        geo = r.json()
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), title="**IP Lookup**", color=0xfefefe)
        try:
        	embed.add_field(name="IP", value=geo['query'], inline=False)
        except:
        	embed.add_field(name="IP", value="None", inline=False)
        try:
        	embed.add_field(name="City", value=geo['city'], inline=False)
        except:
        	embed.add_field(name="City", value="None", inline=False)
        try:
        	embed.add_field(name="Region/State", value=geo['regionName'], inline=False)
        except:
        	embed.add_field(name="Region/State", value="None", inline=False)
        try:
        	embed.add_field(name="Country", value=geo['country'], inline=False)
        except:
        	embed.add_field(name="Country", value="None", inline=False)
        try:
        	embed.add_field(name="Continent", value=geo['continent'], inline=False)
        except:
        	embed.add_field(name="Continent", value="None", inline=False)
        try:
        	embed.add_field(name="ISP", value=geo['isp'], inline=False)
        except:
        	embed.add_field(name="ISP", value="None", inline=False)
        try:
        	embed.add_field(name="Organization", value=geo['org'], inline=False)
        except:
        	embed.add_field(name="Organization", value="None", inline=False)
        try:
        	embed.add_field(name="Reverse DNS", value=geo['reverse'], inline=False)
        except:
        	embed.add_field(name="Reverse DNS", value="None", inline=False)
        try:
        	embed.add_field(name="AS", value=geo['as'], inline=False)
        except:
        	embed.add_field(name="AS", value="None", inline=False)
        try:
        	embed.add_field(name="Mobile?", value=geo['mobile'], inline=False)
        except:
        	embed.add_field(name="Mobile?", value="None", inline=False)
        try:
        	embed.add_field(name="Proxy/VPN?", value=geo['proxy'], inline=False)
        except:
        	embed.add_field(name="Proxy/VPN?", value="None", inline=False)
        try:
        	embed.add_field(name="Hosting?", value=geo['hosting'], inline=False)
        except:
        	embed.add_field(name="Hosting?", value="None", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)
    except:
        await ctx.send('Not A Valid IP/No Info Found!', delete_after=60)

@try2.command()
async def icmping(ctx, *, ip: str = '1.1.1.1'):
    headers = {
        'Accept': 'application/json'
    }
    r = requests.get(f'https://check-host.net/check-ping?host={ip}&max_nodes=15', headers=headers).text
    host = json.loads(r)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), title="**ICMP Check Host**", color=0xfefefe)
    embed.add_field(name="Link To Report", value=host['permanent_link'], inline=False)
    await ctx.send(embed=embed)
   
@try2.command()
async def tcping(ctx, *, ip: str = '1.1.1.1:443'):
    headers = {
        'Accept': 'application/json'
    }
    r = requests.get(f'https://check-host.net/check-tcp?host={ip}&max_nodes=15', headers=headers).text
    host = json.loads(r)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), title="**TCP Check Host**", color=0xfefefe)
    embed.add_field(name="Link To Report", value=host['permanent_link'], inline=False)
    await ctx.send(embed=embed)

@try2.command()
async def nmap(ctx, ip: str = '1.1.1.1'):
    if ip == None:
        await ctx.send('You need to enter a IP address to scan!', delete_after=30)
    else:
        scan = requests.get(f'https://api.hackertarget.com/nmap/?q={ip}').text
        embed = discord.Embed(timestamp=datetime.utcnow(), color=0xfefefe)
        embed.add_field(name='Port Scan Results:', value=f'{scan}')
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)


#        ----------------- Moderation ---------------          #


@try2.command(aliases = ["slowmode"]) #an aliases for the command
@commands.has_permissions(manage_channels=True) #checking the perms for manage_channels
async def sm(ctx, seconds: int): #defining seconds as int
    await ctx.channel.edit(slowmode_delay=seconds) #editing the slowmode of the channel to your input
    await ctx.reply(embed=success)

@try2.command() #this is the kick command 
@commands.has_permissions(kick_members=True) #checking the perms for "kick_members" = true
async def kick2(ctx, member: discord.Member, *, reason): #defining member as discord.Member and taking a reason 
    await member.kick(reason=reason) #kicking the member you mentioned and returning the reason you gave
    await ctx.reply(embed=success)

@try2.command() #this is the ban command!
@commands.has_permissions(ban_members=True) #checking perms for the "ban_members" = true
async def ban(ctx, member: discord.Member, *, reason): #defining member as discord.Member
    await member.ban(reason=reason) #banning a member you mentioned for the reason given
    await ctx.reply(embed=success)


@try2.command() #this is the mute command
@commands.has_permissions(manage_messages=True) #checking if has "manage_messages" = true
async def mute(ctx, member: discord.Member, *, reason=None): #defining stuff ;-;
    guild = ctx.guild #making a variable for ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted") #giving the user muted role when he/she is muted

    if not mutedRole: #checking if there is no role name "Muted" in the guild
        mutedRole = await guild.create_role(name="Muted") #this line will create the role

        for channel in guild.channels: #perms for the muted member
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          reply_messages=False,
                                          read_message_history=True,
                                          read_messages=False)

    await member.add_roles(mutedRole, reason=reason) #this will add the muted role to the member for the given reason
    await ctx.reply(embed=success)
    




@try2.command() #this is the unmute command
@commands.has_permissions(manage_messages=True) #checking perms
async def unmute(ctx, member: discord.Member): #defining stuff
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted") #checking if the member you mentioned has the muted role

    await member.remove_roles(mutedRole) #removing the muted role
    await ctx.reply(embed=success)

#     ----------------- EVnets ----------------- #


os.system('cls')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')







@try2.command(
  aliases=["NUKE", "nn", "nuke", "hi"]
  )
async def destroy(ctx):
    try:
       await ctx.message.delete()
       guild = ctx.guild.id
    except:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error.")
      sleep(10)
      _exit(0)
    
    def delete_role(i):
        session.delete(
          f"https://discord.com/api/v9/guilds/{guild}/roles/{i}",
          headers=headers
        )
    
    def delete_channel(i):
        session.delete(
          f"https://discord.com/api/v9/channels/{i}",
          headers=headers
        )
    
    def create_channels(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json
        )
  
    def create_roles(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/roles",
          headers=headers,
          json=json
        )
    
    try:
       for i in range(3):
         for role in list(ctx.guild.roles):
             threading.Thread(
               target=delete_role,
               args=(role.id, )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads.")
             print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mDeleted role {role}.")
    
       for i in range(3):
         for channel in list(ctx.guild.channels):
             threading.Thread(
               target=delete_channel,
               args=(channel.id, )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads.")
             print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mDeleted channel {channel}.")
     
       for i in range(100):
           threading.Thread(
             target=create_channels,
             args=(random.choice(channel_names), )
           ).start()
           #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads.")
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated channel {random.choice(channel_names)}.")
       
       sleep(3)
       
       for i in range(500):
           threading.Thread(
             target=create_roles,
             args=(random.choice(role_names), )
           ).start()
           #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads")
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated role {random.choice(role_names)}.")


       for i in range(500):
           threading.Thread(
             target=create_channels,
             args=(random.choice(channel_names), )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated channel {random.choice(channel_names)}.")
    except Exception as error:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error" + error)
      sleep(10)
      _exit(0)




@try2.command(
  aliases=["banall", "ww", "bb"]
  )
async def massban(ctx):
    try:
       await ctx.message.delete()
       guild = ctx.guild.id
    except:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error.")
      sleep(10)
      _exit(0)
    
    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
          f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
          headers=headers
        )
    try:
       for i in range(3):
         for member in list(ctx.guild.members):
             threading.Thread(
               target=mass_ban,
               args=(member.id, )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} threads")
             print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mExecuted member {member}.")
       print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mOperation mass ban successful.")
    except Exception as error:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error" + error)
      sleep(10)
      _exit(0)



from itertools import cycle

#     ------ Nukes ------      #
import os, sys, discord, requests, json, threading, random, asyncio
from discord.ext import commands
from os import _exit
from time import sleep
from datetime import datetime

user_ids = []
role_ids = []
channel_ids = []
proxies = []
rotating = cycle(proxies)
try:
    for line in open('Proxies.txt'):
        proxies.append(line.replace('\n', ''))
except:
    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mFailed To Load Proxies From Proxies.txt")

with open("settings.json") as f:
    settings = json.load(f)
channel_names = settings.get("Channel Names")
role_names = settings.get("Role Names")
Webhook_users = settings.get("Webhook Usernames")
Webhook_contents = settings.get("Spam Messages")
bot = settings.get("Bot")
now = datetime.now()
ftime = now.strftime("%H:%M:%S")

if bot:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }



@try2.command(aliases=["redblock"])
async def redtext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```diff\n- {message}```")

@try2.command(aliases=["orangeblock"])
async def orangetext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```css\n[{message}]```")

@try2.command(aliases=["yellowblock"])
async def yellowtext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```fix\n{message}```")

@try2.command(aliases=["greenblock"])
async def greentext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```diff\n+{message}```")

@try2.command(aliases=["lightgreenblock"])
async def lightgreentext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```css\n\"{message}\"```")

@try2.command(aliases=["cyanblock"])
async def cyantext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```json\n\"{message}\"```")  

@try2.command(aliases=["blueblock"])
async def bluetext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```ini\n[{message}]```")


###
@try2.command(aliases=["base64","base64encode","encodebase64"])
async def encrypt(ctx,*,message):
    msg = base64.b64encode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"`{final[1:]}`")

@try2.command(aliases=["base64decode","decodebase64"])
async def decrypt(ctx,*,message):
    msg = base64.b64decode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"`{final[1:]}`")


@try2.command(aliases=["infotoken"])
async def tokeninfo(ctx, bokenxd):
    await ctx.message.delete()
    data = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': bokenxd,'Content-Type': 'application/json'})

    if data.status_code == 200: 

    # user info
        j = data.json()
        # I had something in my folder that helped me with this, if you know who owns the code of subscription data lemme know so I can add credit stuff
        name = f'{j["username"]}#{j["discriminator"]}'
        userid = j['id']
        avatar = f"https://cdn.discordapp.com/avatars/{j['id']}/{j['avatar']}.webp"
        phone = j['phone']
        isverified = j['verified']
        email = j['email']
        twofa = j['mfa_enabled']
        flags = j['flags']
        creation_date = datetime.utcfromtimestamp(((int(userid) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title=f"bot selfbot - Token info", description=f"Token info:\nUser : `{name}`\nUser-id : `{userid}`\nAvatar url : `{avatar}`\nPhone number linked : `{phone}`\nEmail verification status : `{isverified}`\nEmail linked : `{email}`\n2f/a Status : `{twofa}`\nFlags : `{flags}`", color=randcolor)
        message = await ctx.send(embed=embed)

        has_nitro = False
        datahmm = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers={'Authorization': bokenxd,'Content-Type': 'application/json'})
        nitro_data = datahmm.json()
        nitroyems = bool(len(nitro_data) > 0)
        if nitroyems:
            end = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            start = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            totalnitro = abs((start - end).days)
            embed=discord.Embed(title=f"bot selfbot - Token info", description=f"Token info:\nUser : `{name}`\nUser-id : `{userid}`\nAvatar url : `{avatar}`\nPhone number linked : `{phone}`\nEmail verification status : `{isverified}`\nEmail linked : `{email}`\n2f/a Status : `{twofa}`\nFlags : `{flags}`\n\nNitro Data:\nHad nitro since : `{end}`\nNitro ends on : `{start}`\nTotal nitro : `{totalnitro}`", color=randcolor)
            await message.edit(embed=embed)
    else:
        embed=discord.Embed(title=f"bot selfbot - Token info", description=f"Site responded with status code : `{data.status_code}`\nMessage : `{data.text}`")
        await ctx.send(embed=embed)



def deletionofachannel(channeldetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://canary.discord.com/api/v8/channels/{channeldetails}",headers=headers)
    except:
        pass

def deletionofarole(idoftheguild,roledetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://discord.com/api/v8/guilds/{idoftheguild}/roles/{roledetails}",headers=headers)
    except:
        pass

@try2.command(aliases=['deletechans', 'deleteallchannels',"delchan","delchans","channeldel","channeldeletion"])
async def deletechannels(ctx):
    await ctx.message.delete()
    for chan in ctx.guild.channels:
     
        try:
            threading.Thread(target = deletionofachannel, args = (chan.id,)).start() 
        except:
            pass

@try2.command(aliases=['deleterols', 'deleteallroles',"delroles","roledel","delrols","roldel","roledeletion"])
async def deleteroles(ctx):
    await ctx.message.delete()
    for rol in ctx.guild.roles:
        threading.Thread(target = deletionofarole, args = (ctx.guild.id,rol.id,)).start()


webhookspam2

def nooooourrolesgotnukedomg(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        randcolor = random.randint(0x000000, 0xFFFFFF)
        make = requests.post(f"https://discord.com/api/v8/guilds/{idofguild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":randcolor,"mentionable":"true"})
    except:
        pass

@try2.command(aliases=['spamrole', 'rolefuck',"fuckrole","fuckroles","rolesfuck","nukeroles","rolenuke"])
async def rolespam(ctx,amountofthemtomake=None,*,nameofthem=None):
    await ctx.message.delete()
    if nameofthem == None:
        nameofthem = "Nuked via bot ig"

    if amountofthemtomake == None:
        amountofthemtomake = 50
    for i in range(int(amountofthemtomake)):
        threading.Thread(target = nooooourrolesgotnukedomg, args = (ctx.guild.id,nameofthem,)).start()




def nooooourchannelsgotnukedomg(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        req = requests.post(f"https://canary.discord.com/api/v8/guilds/{idofguild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass

@try2.command(aliases=['textchannelcreation', 'textchannelnuke',"channelspam","nuketextchannels","channelsspam"])
async def nuketextchannel(ctx,amountofthemtomake=None,*,nameofthem=None):
    await ctx.message.delete()
    if nameofthem == None:
        nameofthem = "Nuked-via-bot-ig"
    else:
        nameofthem = nameofthem.replace(" ","-")

    if amountofthemtomake == None:
        amountofthemtomake = 50
    for i in range(int(amountofthemtomake)):
        threading.Thread(target = nooooourchannelsgotnukedomg, args = (ctx.guild.id,nameofthem,)).start()

@try2.command(aliases=['token', 'halftoken'])
async def tokenhalf(ctx, member: discord.Member):#
    string = member.id
    string = str(string)
    data = base64.b64encode(string.encode())
    final = str(data).replace("'","")
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="bot Selfbot - Message edit spam", description=f"{member.name}'s Token Begins With : \n`{final[1:]}`", color=randcolor)
    await ctx.message.edit(content="",embed=embed)


@try2.command(aliases=['deletedmessagelogger', 'deletedmessageslogger',"logdeleted","deletedlogger"])
async def logdeletedmessages(ctx,deletestatus=None):
    global deletedmessagelogger 
    if deletestatus == None:
        if deletedmessagelogger == "off":
            deletedmessagelogger = "on"
        elif deletedmessagelogger == "on":
            deletedmessagelogger = "off"
    else:
        if deletestatus.lower() == "off":
            deletedmessagelogger = "off"
        if deletestatus.lower() == "on":
            deletedmessagelogger = "on"

        if deletestatus.lower() == "true": #could i of made the code shorter : yes ... but i like it this way, more clearer to scroll past
            deletedmessagelogger = "on"
        if deletestatus.lower() == "false":
            deletedmessagelogger = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="bot Selfbot - Deleted message logger", description=f"Deleted message logger is now : `{deletedmessagelogger}`", color=randcolor)
    await ctx.message.edit(content="",embed=embed)

@try2.command(aliases=['editedmessagelogger', 'editedmessageslogger','editlog','logedit',"editlogger"])
async def logediteddmessages(ctx,editstatus=None):
    global editedmessagelogger 
    if editstatus == None:
        if editedmessagelogger == "off":
            editedmessagelogger = "on"
        elif editedmessagelogger == "on":
            editedmessagelogger = "off"
    else:
        if editstatus.lower() == "off":
            editedmessagelogger = "off"
        if editstatus.lower() == "on":
            editedmessagelogger = "on"

        if editstatus.lower() == "true": #could i of made the code shorter : yes ... but i like it this way, more clearer to scroll past
            editedmessagelogger = "on"
        if editstatus.lower() == "false":
            editedmessagelogger = "off"

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="bot Selfbot - Edited message logger", description=f"Edited message logger is now : `{editedmessagelogger}`", color=randcolor)
    await ctx.message.edit(content="",embed=embed)


@try2.event
async def on_message_delete(ctx):
    global deletedmessagelogger
    if deletedmessagelogger == "on":
        if ctx.guild == None:
            if ctx.author.id != bot.user.id:
                if len(str(ctx.content)) != 0: #if theyre using a sb itll show nothing so yuh
                    try:
                        await ctx.channel.send(f"**Message logged by {ctx.author.mention} : ** \n{ctx.content}")
                    except:
                        pass


editedmessages ={}


@try2.event
async def on_message_edit(before,after):
    global editedmessages
    global editedmessagelogger
    editedmessages.update({after.channel.id: before.content.replace("@","@\u200b")}) #this needs working on
    if editedmessagelogger == "on":
        if after.guild == None:
            if after.author.id != bot.user.id:
                if before.content != after.content: #embeds sometimes mess with it
                    try:
                        await after.channel.send(f"**Message edited by {after.author.mention} : ** \n**Before : **{before.content}\n**After : **{after.content}")
                    except:
                        pass




token = setup[0].replace('"',"").replace("TOKEN=","")

try2.run(token.strip(), bot=False)