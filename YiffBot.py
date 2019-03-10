#YiffBot 3.0
#----------
from variables import *
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
channels = []
Servers = []
counter = 0
counter2 = 0
counter3 = 0
counter4 = 1
y = 0

def keepAlive():
  keep_alive()
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
        client_email = None
        client_password = None
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
async def printChannels():
    global client
    global channels
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
        for channel in guild.channels:
            channel2 = str(channel)
            channel2 = channel2.encode('ascii', 'ignore').decode('ascii')
            counter2 += 1
            print("  " + str(counter2) + ". " + channel2)
            
async def sendYiff(channel, guild):
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
            await channel.send(file=discord.File(saveFile))
            counter3 += 1
            channel2 = str(channel)
            server2 = str(guild)
            channel2 = channel2.encode('ascii', 'ignore').decode('ascii')
            server2 = server2.encode('ascii', 'ignore').decode('ascii')
            print("sent  |  " + str(counter3) + "  |  " + server2 + " - " + channel2)
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
                                await sendYiff(message.channel, message.guild)
                        if local1 == "p":
                            await sendYiff(message.channel, message.guild)
                        a = 1
                    if a != 1:
                        msg = '{0.author.mention} Use a nsfw chat!'.format(message)
                        await message.channel.send(msg)
                if local2 == "nsfw":
                    if local1 == "s":
                        while True:
                            await sendYiff(message.channel, message.guild)
                    if local1 == "p":
                        while True:
                            try:
                                await sendYiff(message.channel, message.guild)
                                break
                            except Exception as e:
                                print(str(e))
async def testMessage():
    global channels
    await printChannels()
    for guild in client.guilds:
        Servers.append(str(guild))
        for channel in guild.channels:
            channels.append(channel)
    serverNumber = input('''
Server Number
>>> ''')
    channelNumber = input('''
Channel Number
>>> ''')
    serverName = Servers[int(serverNumber) -1]
    channelName = channels[int(channelNumber) -1]
    for guild in client.guilds:
        if guild == serverName:
            if channel != None:
                channel = discord.utils.get(channels, guild__name=str(serverName), name=str(channelName))
                await channel.send("Spam bot ready, waiting for initialization...")
                print("Sent To: " + str(channelName))
    serverName = Servers[int(serverNumber) -1]
    channelName = channels[int(channelNumber) -1]
    for guild in client.guilds:
        if str(guild) == serverName:
            if channel != None:
                channel = discord.utils.get(channels, guild__name=str(serverName), name=str(channelName))
                #await (discord.Object(id=channel.id)).send("Spam bot ready, waiting for initialization...")
                await channel.send("Spam bot ready, waiting for initialization...")
                print("Sent To: " + str(channelName))
async def directSpam():
    await printChannels()
    for guild in client.guilds:
        Servers.append(guild)
        for channel in guild.channels:
            channels.append(channel)
    serverNumber = input('''
Server Number
>>> ''')
    channelNumber = input('''
Channel Number
>>> ''')
    serverName = Servers[int(serverNumber) -1]
    channelName = channels[int(channelNumber) -1]
    channelName = str(channelName)
    for guild in client.guilds:
        if guild == serverName:
            if channel != None:
                x = 1
                channel = discord.utils.get(channels, guild__name=str(serverName), name=str(channelName))
                print("Sent To: " + channelName)
                while True:
                    await sendYiff(channel, guild)
    for guild in client.guilds:
        if str(guild) == serverName:
            if channel != None:
                x = 1
                channel = discord.utils.get(channels, guild__name=str(serverName), name=str(channelName))
                print("Sent To: " + channelName)
                while True:
                    await sendYiff(channel, guild)
def runBot(client_bot, client_email, client_password, token):
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
    client.close()

    print("")
    print("Restarting...")
    restart()
    
def startup():
    print("Loading...")
    print("----------")
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
            keep_alive()

#Modules
def main():
    startup()
def run_bot(client_bot, client_email, client_password, token):
    runBot(client_bot, client_email, client_password, token)
async def test_message():
    await testMessage
def seek_triggers(PorS, SFWorNSFW):
    seekTriggers(PorS, SFWorNSFW)
async def send_yiff(Channel, Server):
    await sendYiff(Channel, Server)
async def print_channels():
    await printChannels()
async def direct_spam():
    await directSpam()
