import discord
import random
from discord.ext import commands
import praw
TOKEN= #TOKEN


intents = discord.Intents(messages=True, members=True)
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), intents=intents)
 
reddit = praw.Reddit(client_id= 'GmTgKVFh5Z0AlQ',client_secret = ' ouxhtobXWu_awgVKjfhGS0TQLS0fpg', username = 'memesofdiscord', password = 'Zl29633!',  user_agent = 'pythonpraw')
 
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game ("plague inc"))
  print('We have logged in as {0.user}'.format(bot))
 
 
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content.startswith("hello"):
    await message.channel.send("no")
  await bot.process_commands(message)
 
@bot.command()
async def meme(ctx):
  subreddit = reddit.subreddit("memes")
  all_subs = []
  top = subreddit.hot(limit = 50)
  for lowfsdf in top:
      all_subs.append(lowfsdf)
  random_sub = random.choice(all_subs)
  name = random_sub.title 
  url = random_sub.url
  em = discord.Embed (title = name)
  em.set_image(url = url)
  await ctx.send(embed = em) 

 
@bot.command()
async def _8ball(ctx):
  responses = [
           "It is certain.",
           "It is decidedly so.",
           "Without a doubt.",
           "Yes - definitely.",
           "You may rely on it.",
           "As I see it, yes.",
           "Most likely.",
           "Outlook good.",
           "Yes.",
           "Signs point to yes.",
           "Reply hazy, try again.",
           "Ask again later.",
           "Better not tell you now.",
           "Cannot predict now.",
           "Concentrate and ask again.",
           "Don't count on it.",
           "My reply is no.",
           "My sources say no.",
           "Outlook not so good.",
           "Very doubtful."]
  g = random.choice(responses)
  await ctx.send (g)
 
@bot.command()
async def convert(ctx):
  await ctx.send('no one expects the spanish inquisition')
 
@bot.command()
async def ship(ctx):   
  members = ctx.guild.members
  randomMember = str(random.choice(members))
  randomMember2 = str(random.choice(members))
  await ctx.send({randomMember.mention})
  await ctx.send({randomMember2.mention})
 
@bot.command()
async def death(ctx) :
  years = str(random.randrange(0, 100))
  days = str(random.randrange(0, 365))
  hour = str(random.randrange(0, 24))
  minutes = str(random.randrange(0, 60))
  seconds = str(random.randrange(0, 60))
  deathnote = ('you will die in ' + (years) + ' years, ' + (days) +' days, ' + (hour) + ' hours, ' + (minutes) + ' minutes, and ' + (seconds) + ' seconds.')
  await ctx.send(deathnote)
 
 
bot.run(TOKEN)
