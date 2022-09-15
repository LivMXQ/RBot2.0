import discord
from replit import Database
import pickle
from discord.ext import commands
import os

db = Database(os.getenv("REPLIT_DB_URL"))

db["reaction_roles"] = {}

class Reaction(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    if payload.message_id==1009037985783758858 and payload.emoji==discord.PartialEmoji.from_str("✅"):
      guild = self.bot.get_guild(1006924989104136262)
      member = discord.utils.get(guild.members, id=payload.user_id)
      role = discord.utils.get(guild.roles, name="SLK@Everyone")
      await member.add_roles(role)
      
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    if payload.message_id==1009037985783758858 and payload.emoji==discord.PartialEmoji.from_str("✅"):
      guild = self.bot.get_guild(1006924989104136262)
      member = discord.utils.get(guild.members, id=payload.user_id)
      role = discord.utils.get(guild.roles, name="SLK@Everyone")
      await member.remove_roles(role)

def setup(bot: commands.Bot):
  bot.add_cog(Reaction(bot))