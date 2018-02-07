#-----------------Imports----------------------#
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import discord, chalk
#------------------VARS------------------------#

prefix = "!" 
embed_role = "Sam" 
game = "eh!" 
kick_role = "Sam"
ban_role = "Sam"

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
    embed = discord.Embed(description=a_sMessage, color=0xffdd00)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.set_author(name=ctx.message.author.name + " says..")
    embed.set_footer(text="Fox 0.3")
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
    chalk.green(ctx.message.author.name + " has embedded a message in " + ctx.message.server.name)

#-----------------ModCommands-------------------#

@bot.command(pass_context=True)
@commands.has_role(kick_role)
async def kick(ctx, user: discord.Member):
    embed = discord.Embed(title="Kicked {}.format(user.name)", description="Get that out of here", color=0xffdd00)
    embed.set_footer(text="Fox 0.6")
    await bot.say(embed)
    await bot.kick(user)


@bot.command(pass_context=True)
@commands.has_role(kick_role)
async def ban(ctx, user: discord.Member):
    embed = discord.Embed(title="The Ban Hammer RAINED On {}.format(user.name)", description=":Boot: Don`t let the door kick you in the ass. -Dr Phil", color=0xffdd00)
    embed.set_footer(text="Fox 0.6")
    await bot.say(embed)
    await bot.ban(user)
    
#-----------------InfoCommands------------------#
    
@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0xffdd00)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_footer(text="Fox 0.6")
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed)
    
@bot.command(pass_context=True)
async def profile(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s Profile".format(user.name), description="Here's what I could find.", color=0xffdd00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text="Fox 0.6")
    await bot.say(embed)

@bot.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(title="Fox.", color=0xffdd00)
    embed.add_field(name="Fox is a fully modular discord.py bot, made by Samuel-Flynn New. ", inline=True)
    embed.set_thumbnail(url=bot.avatar_url)
    embed.set_footer(text="Fox 0.6")
    await bot.say(embed)

    
bot.run("Insert Token")
#Made By Samuel-Flynn New
