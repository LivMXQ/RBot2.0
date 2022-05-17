def main():
  import os
  import discord
  from discord.ext import commands
  from keep_alive import keep_alive


  bot = commands.Bot(command_prefix='-', case_insensitive=True, intents=discord.Intents.all(), help_command=None)


  for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != "__init__.py":
      bot.load_extension(f'cogs.{filename[:-3]}')


  @bot.event
  async def on_ready():
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name=";help"), status=discord.Status.online)
    print('We have logged in as {0.user}'.format(bot))

  @bot.event
  async def on_disconnect():
      print("bot disconnected")


  @bot.event
  async def on_connect():
      print("bot connected")
    

  keep_alive()
  bot.run(os.getenv('TOKEN'))

if __name__ == "__main__":
  main()