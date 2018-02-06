#-----------------Imports----------------------#
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import discord, chalk
#------------------VARS------------------------#

prefix = "!" 
embed_role = "Sam" 
game = "eh!" 

#-------------------Prefix---------------------#

bot = commands.Bot(command_prefix=prefix)

#------------------OnReady---------------------#

@bot.event
async def on_ready():
    chalk.blue ("Ready.") 
    chalk.blue ("Name: {}".format(bot.user.name))
    chalk.blue ("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name=game))

#-----------------Commands---------------------#

@bot.command(pass_context=True)
@commands.has_role(embed_role)
async def embed(ctx, *, a_sMessage):
    embed = discord.Embed(description=a_sMessage, color=0x00a0ea)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.set_author(name=ctx.message.author.name + " says..")
    embed.set_footer(text="Fox 0.1")
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
    chalk.green(ctx.message.author.name + " has embedded a message in " + ctx.message.server.name)\


bot.run("Insert Token")
