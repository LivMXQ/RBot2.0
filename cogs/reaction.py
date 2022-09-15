import discord
from replit import Database
import pickle
from discord.ext import commands

db = Database("https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NjMzNDY0ODIsImlhdCI6MTY2MzIzNDg4MiwiZGF0YWJhc2VfaWQiOiJiODY2ZTkxMi0zNzkwLTRjYmYtOTI1NC1hNTc5ZjllZDNiMTMiLCJ1c2VyIjoiTVhRTGl2Iiwic2x1ZyI6IlJCb3QyMCJ9.J-h0UgqHKSHwI1Bt26O0YCn8y9JAmEwUz6m8hB_-ZiJWfQlzxJbj-A_Cz97FLN7gHJjSq0Jo73WHS1g0ZDr0JQ")

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