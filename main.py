import os
import logging
import discord
from discord.ext import commands
from keep_alive import keep_alive
from cogs.utility import VerifyView
from cogs.slk import ColourRolesView, RegionView, PronounsView, DevicesView, PingsView
from replit import db

#db["tickets"] = {}
  
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True

class RoyosukeBot(commands.Bot):
  def __init__(self):
    super().__init__(intents=intents, debug_guilds=[954583503490658344, 846263154546573333, 1006924989104136262, 1019076662450729043])

  async def on_ready(self):
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name="God, Syria, Al Bashar!"), status=discord.Status.online)
    print('We have logged in as {0.user}'.format(bot))

  async def on_disconnect(self):
      print("bot disconnected")

  async def on_connect(self):
    await self.sync_commands()
    bot.add_view(VerifyView())
    bot.add_view(ColourRolesView())
    bot.add_view(RegionView())
    bot.add_view(PronounsView())
    bot.add_view(DevicesView())
    bot.add_view(PingsView())
    print("bot connected")
      

bot = RoyosukeBot()

for filename in os.listdir('./cogs'):
  if filename.endswith('.py') and filename != "__init__.py":
    bot.load_extension(f'cogs.{filename[:-3]}', store=False)
    
keep_alive()
try:
  bot.run(os.getenv('TOKEN'))
except:
  os.system("kill 1")

  