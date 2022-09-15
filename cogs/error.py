from discord.ext import commands

class NotTicketChannel(commands.CommandError):
  def __init__(self, message="This channel is not a ticket lol"):
    super().__init__(message)
    

class Error(commands.Cog):
  @commands.Cog.listener()
  async def on_application_command_error(self, ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandOnCooldown):
      message = f"This command is on cooldown. Try again in {round(error.retry_after, 1)} seconds."
      await ctx.followup.send(content=message, ephemeral=True)

    elif isinstance(error, NotTicketChannel):
      message = "This is not a ticket lmao"   
      await ctx.followup.send(content=message, ephemeral=True)
      
    elif isinstance(error, commands.CommandNotFound):
      pass
      
    elif isinstance(error, commands.MissingPermissions):
      message = "You don't have the permissions for this!"
      await ctx.followup.send(content=message, ephemeral=True)

    elif isinstance(error, commands.NotOwner):
      message = "You are not the owner of the bot!"
      await ctx.followup.send(content=message, ephemeral=True)

    else:
      await ctx.followup.send(content=error, ephemeral=True)

def setup(bot: commands.Bot):
  bot.add_cog(Error(bot))