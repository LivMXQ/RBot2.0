import discord
import functools
from discord.ext import commands
from discord.ui import Button, View

class TestView(View):
  def __init__(self):
    pass
  """async def callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name=name)
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)"""
    
class Test(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @discord.slash_command(name="test")
  async def test(self, ctx):
    view = View()
    await ctx.respond("yes", view=view)
  
def setup(bot):
  bot.add_cog(Test(bot))