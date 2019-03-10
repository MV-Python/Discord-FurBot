#YiffBot 3.0
#----------
from tokens import *
from main import *
#----------
import discord
import ssl
import sys
from discord.utils import get
from live import keep_alive
ssl._create_default_https_context = ssl._create_unverified_context
from discord.ext import commands
import asyncio
import random
print_errors = True
#-----------
triggers = ["OwO", "owo", "UwU", "uwu", "rawr","yiff", "xd"]
prefix = ">>>"
saveFile = r"C:\Users\mvale\Documents\e6Stuff\DiscordImage.jpg"
#-----------
client = discord.Client()
loop = asyncio.get_event_loop()
postNumber = 1000000
TextChannels = []
Servers = []
counter = 0
counter2 = 0
counter3 = 0
counter4 = 1
y = 0
def restart():
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
def tokenChoiceSelect(tokenChoice):
    global token
    global client_bot
    global client_email
    global client_password
    global client_token3
    global client_token2
    global client_token1
    #YiffBot1 (bot)
    if tokenChoice == "1":
        token = client_token1
        client_bot = True
    #YiffBot (user)
    if tokenChoice == "2":
        token = client_token2
        client_bot = False
        client_email = client_email2
        client_password = client_password2
    #MV_Katze (user)
    if tokenChoice == "3":
        token = client_token3
        client_bot = False
        client_email = client_email3
        cleint_password = client_password3
def atexit_command():
    print('''
Closed''')
async def print_TextChannels():
    global client
    global TextChannels
    global Servers
    global counter
    global counter2
    for guild in client.guilds:
        print("————————————————————————————————")
        server2 = str(guild)
        server2 = server2.encode('ascii', 'ignore').decode('ascii')
        counter += 1
        print(str(counter) + ". " + server2)
        print("————————————————————————————————")
        for TextChannel in guild.channels:
            TextChannel2 = str(TextChannel)
            TextChannel2 = TextChannel2.encode('ascii', 'ignore').decode('ascii')
            counter2 += 1
            print("  " + str(counter2) + ". " + TextChannel2)
            
async def send_yiff(TextChannel, guild):
    import urllib.parse
    import urllib.request
    global saveFile
    global counter3
    while True:
        try:
            y = random.randrange(postNumber)
            url = r'https://e621.net/post/show/' + str(y)
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib.request.Request(url, headers = headers)
            req = urllib.request.urlopen(req)
            webCode = []
            text = str(req.read())
            barOne = (text.rfind(r'https://static'))
            barTwo = (text.rfind(r'.jpg'))
            text = (text[barOne:barTwo + 4])
            urllib.request.urlretrieve(text, saveFile)
            await TextChannel.send(file=discord.File(saveFile))
            counter3 += 1
            TextChannel2 = str(TextChannel)
            server2 = str(guild)
            TextChannel2 = TextChannel2.encode('ascii', 'ignore').decode('ascii')
            server2 = server2.encode('ascii', 'ignore').decode('ascii')
            print("sent  |  " + str(counter3) + "  |  " + server2 + " - " + TextChannel2)
            break
        except Exception as e:
            if print_errors == True:
                print(str(e))
def seekTriggers(local1, local2):
    @client.event
    async def on_message(message):
        global token
        global triggers
        global client
        global y
        a = 0
        #--
        if message.author == client.user:
            return
        #--
        for word in triggers:
            if word in message.content:
                if local2 == "sfw":
                    if message.channel.is_nsfw():
                        msg = 'UwU {0.author.mention}'.format(message)
                        await message.channel.send(msg)
                        if local1 == "s":
                            while True:
                                await send_yiff(message.channel, message.guild)
                        if local1 == "p":
                            await send_yiff(message.channel, message.guild)
                        a = 1
                    if a != 1:
                        msg = '{0.author.mention} Use a nsfw chat!'.format(message)
                        await message.channel.send(msg)
                if local2 == "nsfw":
                    if local1 == "s":
                        while True:
                            await send_yiff(message.channel, message.guild)
                    if local1 == "p":
                        for i in range(counter4):
                            try:
                                await send_yiff(message.channel, message.guild)
                            except Exception as e:
                                print(str(e))
                                counter4 += 1
async def testMessage():
    global TextChannels
    await print_TextChannels()
    for guild in client.guilds:
        Servers.append(str(guild))
        for TextChannel in guild.channels:
            TextChannels.append(TextChannel)
    serverNumber = input('''
Server Number
>>> ''')
    TextChannelNumber = input('''
Channel Number
>>> ''')
    serverName = Servers[int(serverNumber) -1]
    TextChannelName = TextChannels[int(TextChannelNumber) -1]
    for guild in client.guilds:
        if guild == serverName:
            if TextChannel != None:
                TextChannel = discord.utils.get(TextChannels, guild__name=str(serverName), name=str(TextChannelName))
                await TextChannel.send("Spam bot ready, waiting for initialization...")
                print("Sent To: " + str(TextChannelName))
    serverName = Servers[int(serverNumber) -1]
    TextChannelName = TextChannels[int(TextChannelNumber) -1]
    for guild in client.guilds:
        if str(guild) == serverName:
            if TextChannel != None:
                TextChannel = discord.utils.get(TextChannels, guild__name=str(serverName), name=str(TextChannelName))
                #await (discord.Object(id=TextChannel.id)).send("Spam bot ready, waiting for initialization...")
                await TextChannel.send("Spam bot ready, waiting for initialization...")
                print("Sent To: " + str(TextChannelName))
async def directSpam():
    await print_TextChannels()
    for guild in client.guilds:
        Servers.append(guild)
        for TextChannel in guild.channels:
            TextChannels.append(TextChannel)
    serverNumber = input('''
Server Number
>>> ''')
    TextChannelNumber = input('''
Channel Number
>>> ''')
    serverName = Servers[int(serverNumber) -1]
    TextChannelName = TextChannels[int(TextChannelNumber) -1]
    TextChannelName = str(TextChannelName)
    for guild in client.guilds:
        if guild == serverName:
            if TextChannel != None:
                x = 1
                TextChannel = discord.utils.get(TextChannels, guild__name=str(serverName), name=str(TextChannelName))
                print("Sent To: " + TextChannelName)
                while True:
                    await send_yiff(TextChannel, guild)
    for guild in client.guilds:
        if str(guild) == serverName:
            if TextChannel != None:
                x = 1
                TextChannel = discord.utils.get(TextChannels, guild__name=str(serverName), name=str(TextChannelName))
                print("Sent To: " + TextChannelName)
                while True:
                    await send_yiff(TextChannel, guild)
def runBot():
    try:
        if client_bot == True:
            loop.run_until_complete(client.start(token))
        if client_bot == False:
            loop.run_until_complete(client.start(token, bot=False))
    except Exception as e:
        if client_bot == False:
            try:
                print("")
                print("Token Login Failed")
                print("Error:", str(e))
                print("")
                print("Using Email and Password...")
                print("")
                loop.run_until_complete(client.start(client_email, client_password))
            except Exception as e:
                print("All Logins Failed!")
                print("Error:", str(e))
        if client_bot == True:
            print("")
            print("All Logins Failed!")
            print("Error:", str(e))

    print("")
    print("Restarting...")
    restart()
    
def startup():
    print("Loading...")
    print("----------")
    while True:
        tokenChoice = input('''
1. Yiffbot1 (bot)
2. Yiffbot
3. MV Katze
>>> ''')
        tokenChoiceSelect(tokenChoice)
        global client
        @client.event
        async def on_ready():
            await client.wait_until_ready()
            x = 0
            y = 0
            print("Logged in as:")
            print(client.user.name)
            print("--------")
            choice1 = input('''
0. Restart
1. Test Message
2. Send Spam Directly
3. Seek Triggers for Spam
4. Seek Triggers for Passive Use
>>> ''')
            if choice1 == "0":
                restart()
            choice2 = input('''
Keep Alive? (y/n)
>>> ''')
            if choice1 == "1":
                await testMessage()
            if choice1 == "2":
                await directSpam()
            if choice1 == "3":
                seekTriggers("s", "nsfw")
            if choice1 == "4":
                global triggers
                triggers = [prefix + "yiff"]
                seekTriggers("p", "sfw")
            if choice2 == "y":
                keep_alive
        runBot()
seekTriggers("s", "nsfw")
runBot(True, None, None, "NTEzMTA3MzI1NDI3NjQ2NDk0.D1ythQ.jsgUhVdI2gVUIWhn6G-11nypzYE")
