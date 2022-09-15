import random
import discord
import asyncio
from cogs.error import NotTicketChannel
from discord.ui import Button, View
from discord.ext import commands, tasks
from replit import db

class VerifyView(View):
  def __init__(self):
    super().__init__(timeout=None)
          
  async def interaction_check(self, interaction):
    if interaction.user.id not in db["tickets"].values():
      return True
    else:
      await interaction.response.send_message("You already have a ticket duh", ephemeral=True)
      return False
        
  @discord.ui.button(label="📩", custom_id="verify_button")
  async def callback(self, button, interaction):
    ticket_number = get_ticket_number()
    ticket_channel = await interaction.guild.create_text_channel(name=f"ticket-{ticket_number}", category=discord.utils.get(interaction.guild.categories, name="verify"))
    await interaction.response.send_message(f"Ticket {ticket_channel.mention} created", ephemeral=True)
    db["tickets"][str(ticket_channel.id)] = interaction.user.id
    await ticket_channel.send(f"{interaction.user.mention} Hello there")
    await ticket_channel.send("Just state why are you here and pin a mod/admin")
    await ticket_channel.send("We should get to you in 12h")

def reset_numbers():
  numbers = []
  for i in range(1, 101):
    numbers.append((3-len(str(i)))*"0"+str(i))
  return numbers

with open("ticket_numbers", "w") as f:
  a = []
  for i in db.keys():
    a.append(i + """
    """ + str(db[i]) + """
    """)
  f.write(str(a))

#db["ticket_numbers"] = reset_numbers()

def get_ticket_number():
  number = db["ticket_numbers"].pop(0)
  return number
  

class Utility(commands.Cog):
  def __init__(self, bot:commands.bot):
    self.bot = bot
    self.fetch_quotes.start()
        
  def cog_unload(self):
    self.fetch_quotes.cancel()
    
  @discord.slash_command(name="verifymsg", guild_ids=[846263154546573333])
  async def verifymsg(self, ctx):
    channel = self.bot.get_channel(972472475214544906)
    verify_view = VerifyView()
    await channel.send(content="""
      Hello there
This is not really a public server
So please create a ticket and to verify your identity to gain access to the rest of the server
If you are a random don't worry we might also accept you 
                                              
React to this message to open a ticket
Spamming tickets will earn you a warning/kick!
""", view=verify_view)
      
    await ctx.respond("Done!", ephemeral=True)
      
  @tasks.loop(minutes=20.0)
  async def fetch_quotes(self):
    await self.bot.wait_until_ready()
    channel = self.bot.get_channel(922440576115281981)
    quotelist = []
    async for i in channel.history(limit=None):
      quotelist.append(i.id)
    db["quotelist"] = quotelist

  @discord.slash_command(name="invite")
  @commands.is_owner()
  async def invite(self, ctx):
    await ctx.respond(discord.utils.oauth_url(client_id=self.bot.application_id, permissions=discord.Permissions.advanced()), ephemeral=True)
    
  @discord.slash_command(name="quote", description="Get some quotes from our server", guild_ids=[846263154546573333, 1019076662450729043])
  async def quote(self, ctx, amount:int=discord.Option(int, "amount of quotes to get", min_value=1, max_value=5, default=1)):
    quotes = db["quotelist"]
    if len(quotes) == 0:
      await ctx.respond("There are no more quotes! Please wait")
    for i in range(amount):
      view = View()
      channel = self.bot.get_channel(922440576115281981)
      id = random.choice(quotes)
      message = await channel.fetch_message(id)
      if len(message.content) > 256:
        await ctx.respond("message too long, pls ask someone to fix", ephemeral=True)
      else:
        quotes.remove(id)
        linkbtn = Button(label="Jump!", style=discord.ButtonStyle.link, url=message.jump_url)
        view.add_item(linkbtn)
        embed = discord.Embed(description=f"Random quote from {channel.mention}", title=message.content)
        embed.set_author(name=message.author.name)
        await ctx.respond(embed=embed, view=view)
        
      
  @discord.slash_command(name="delete", guild_ids=[846263154546573333]) 
  @commands.has_permissions(manage_channels=True)
  async def delete(self, ctx):
    if ctx.channel.name.startswith("ticket-"):
      db["ticket_numbers"].append(ctx.channel.name[7:])
      db["tickets"].pop(str(ctx.channel.id))
      await ctx.channel.delete()
    else:
      raise NotTicketChannel()
      

  @discord.slash_command(name="ban")
  async def ban(self, ctx, user:discord.User):
    await ctx.respond(f"{user.mention} has been banned")

  @discord.slash_command(name="bomb", guild_ids = [1019076662450729043])
  async def bomb(self, ctx):
    view = View()
    button = Button(label="allah!", style=discord.ButtonStyle.danger)
    async def allah_callback(interaction):
      await interaction.response.edit_message(content="🛬\n\n\n\n  \🏘")
      await asyncio.sleep(0.1)
      await interaction.followup.edit_message(message_id=interaction.message.id, content="🛬\n\n\n\n  \🏘")
    button.callback = allah_callback
    view.add_item(button)
    
    await ctx.respond("​\n\n\n\n\n  \🏘", view=view)

def setup(bot: commands.Bot):
    bot.add_cog(Utility(bot))