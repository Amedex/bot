import discord
from discord.ext import commands
import random
import math
import yaml
config = yaml.load(open("settings.yml", "r", encoding="utf8", errors="ignore"), Loader=yaml.Loader)

discord_token = str(config["token"])
client = discord.Client
bot = commands.Bot(command_prefix=[str(config["prefix"])])
bot.remove_command('help')
#                     v in seconds
@bot.command(pass_contex=True)
async def gen(ctx):
    messages = open("conturi.txt", "r").readlines()
    message_content = random.choice(messages).strip()
    user = bot.get_user(id=ctx.author.id)
    message = await user.send(message_content)
    await user.send_message('Reply')

@bot.command(pass_contex=True)
async def pgen(ctx):
    messages = open("conturip.txt", "r").readlines()
    message_content = random.choice(messages).strip()
    user = bot.get_user(id=ctx.author.id)
    message = await user.send(message_content)
    await bot.send_message("Reply1")


@bot.event
async def on_ready(pass_contex=True):
    print("Bot-ul a pornit!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        user = bot.get_user(id=ctx.author.id)
        message = await user.send("Buna, " +
                                  "\ndin pacate, trebuie sa mai astepti " +
                                  str(math.ceil(error.retry_after)) +
                                  " secunde pentru a folosi aceasta comanda")
        await ctx.message.add_reaction(emoji=":x:")

@bot.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))

bot.run(discord_token)