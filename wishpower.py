import discord
import asyncio
import random
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
quoteList = []

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

bcount = 0

@client.event
async def on_message(message):
    global bcount
    if message.content == "?bcount --reset":
        bcount = 0
    elif message.content == "?bcount":
        await client.send_message(message.channel, "{0} too many 🅱's have been posted in this chat.".format(bcount))
    elif message.content.startswith("?addquote"):
        quoteList.append(message.content[10:])
        await client.send_message(message.channel, "Adding this juicy quote to the list. :ok_hand:")
    elif message.content == "?quote":
        await client.send_message(message.channel, "{0}".format(random.choice(quoteList)))
    elif message.content == "?help":
        await client.send_message(message.channel,\
'''He is in my behind. Here's what all you can do with me:

    - ?bcount: Returns the number of 🅱's sent in the channel since the inception of this bot.

    - ?addquote: Adds any subsequent text to a list of quotes which may be referenced with ?quote.

    - ?quote: Returns a random quote from the quote list.

    - ?help: You should know what this does...''')
    elif message.content.startswith("?"):
        await client.send_message(message.channel, "The wish power are together with you. Use ?help to view all commands.")
    if "🅱" in message.content and message.author.id != message.server.me.id:
        bcount += message.content.count("🅱")

client.run("NDIwODIwMzc5OTU1NjI1OTg1.DYEPmQ.iznb9pN53KCK-9-bj3iljzBfMD4")