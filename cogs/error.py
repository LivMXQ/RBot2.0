from discord.ext import commands


class Error(commands.Cog):  
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandOnCooldown):
      message = f"This command is on cooldown. Try again in {round(error.retry_after, 1)} seconds."
      await ctx.reply(content=message, delete_after=5)
      
    elif isinstance(error, commands.MissingPermissions):
      message = "You don't have the permission for this!"
      await ctx.reply(content=message, delete_after=5)

    elif isinstance(error, commands.NotOwner):
      message = "You are not the owner of the bot!"
      await ctx.reply(content=message)

    else:
      message = "Something went wrong while running the command ):"
      print(error, type(error))
      await ctx.reply(content=message, delete_after=5)

def setup(bot: commands.Bot):
  bot.add_cog(Error(bot))