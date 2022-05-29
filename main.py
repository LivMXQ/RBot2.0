def main():
  import os
  import discord
  from cogs.utility import get_ticket_number
  from discord.ext import commands
  from keep_alive import keep_alive


  bot = commands.Bot(command_prefix='-', case_insensitive=True, intents=discord.Intents.all(), help_command=None)


  for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != "__init__.py":
      bot.load_extension(f'cogs.{filename[:-3]}')


  @bot.event
  async def on_ready():
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name="The Grinds guild"), status=discord.Status.online)
    print('We have logged in as {0.user}'.format(bot))

  @bot.event
  async def on_disconnect():
      print("bot disconnected")


  @bot.event
  async def on_connect():
    print("bot connected")

  @bot.event
  async def on_raw_reaction_add(payload):
    if payload.message_id == 978656534651359312:
      channel = bot.get_channel(payload.channel_id)
      guild = bot.get_guild(payload.guild_id)
      message = await channel.fetch_message(payload.message_id)
      user = bot.get_user(payload.user_id)
      await message.remove_reaction(emoji="✉️", member=user)
      ticket_number = get_ticket_number()

      ticket_channel = await guild.create_text_channel(name=f"ticket-{ticket_number}", category=discord.utils.get(guild.categories, name="verify"))
      await ticket_channel.send(f"{user.mention} Hello there")
      await ticket_channel.send("Just state which guy u have relation and pin a mod/admin")
      await ticket_channel.send("We should get to you in 12h")

  keep_alive()
  bot.run(os.getenv('TOKEN'))

if __name__ == "__main__":
  main()