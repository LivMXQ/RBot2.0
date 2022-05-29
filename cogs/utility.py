import random
import discord
from cogs.error import NotTicketChannel
from discord.ui import Button, View
from discord.ext import commands, tasks
from replit import db

db["ticket_numbers"]

ticket_numbers = db["ticket_numbers"]
def get_ticket_number():
  number = ticket_numbers.pop(0)
  return number
  

class Utility(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot
        self.fetch_quotes.start()
        

    def cog_unload(self):
        self.fetch_quotes.cancel()
       
      
    @commands.command("verifymsg")
    async def verifymsg(self, ctx):
      channel = self.bot.get_channel(972472475214544906)
      
      await channel.purge(limit=2)
      
      msg = await channel.send("""
      Hello there
This is not really a public server
So please create a ticket and to verify your identity to gain access to the rest of the server
If you are a random don't worry we might also accept you 
                                              
React to this message to open a ticket
Spamming tickets will earn you a warning/kick!
""")
      await msg.add_reaction("✉️")
      
    @tasks.loop(minutes=10.0)
    async def fetch_quotes(self):
      await self.bot.wait_until_ready()
      channel = self.bot.get_channel(922440576115281981)
      quotes = channel.history()
      quotelist = []
      async for i in quotes:
        quotelist.append([i.clean_content, i.author.name, i.jump_url])
      db["quotelist"] = quotelist

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount:int):
      await ctx.message.delete()
      await ctx.channel.purge(limit=amount)
      await ctx.channel.send(content=f"Successfully purged {amount} messages from this channel",delete_after=5)
      
    @commands.command(name="quote")
    async def quote(self, ctx):
      view = View()
      quotes = db["quotelist"]
      content = random.choice(quotes) 
      linkbtn = Button(label="Jump!", style=discord.ButtonStyle.link, url=content[2])
      view.add_item(linkbtn)
      embed = discord.Embed(description=f"Random quote from {self.bot.get_channel(922440576115281981).mention}", title=content[0])
      embed.set_author(name=content[1])
      await ctx.send(embed=embed, view=view)
        
    
      
    @commands.command(name="delete", aliases=["del"]) 
    @commands.has_permissions(manage_channels=True)
    async def delete(self, ctx):
      if ctx.channel.name.startswith("ticket-"):
        ticket_numbers.append(ctx.channel.name[7:])
        await ctx.channel.delete()
      else:
        raise NotTicketChannel()
      

    @commands.command("giverole", aliases = ["gr"])
    @commands.has_permissions(manage_roles=True)
    async def giverole(self, ctx, member:discord.Member, role):
        if not isinstance(role, discord.Role):
          role = discord.utils.get(ctx.guild.roles, name=role)
        await member.add_roles(role)
        await ctx.message.delete()



def setup(bot: commands.Bot):
    bot.add_cog(Utility(bot))