import discord
import get_env

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# "おはよう"に返答
@client.event
async def on_message(message):
    if message.content.startswith("おはよう") and client.user != message.author:
        m = "おはようございます" + message.author.name + "さん！"
        await client.send_message(message.channel, m)


# "メンションに返答"
@client.event
async def on_message(message):
    if client.user.id in message.content:
        reply = f'{message.author.mention} やっほー'
        await client.send_message(message.channel, reply)


client.run(get_env.DISCORD_TOKEN)
