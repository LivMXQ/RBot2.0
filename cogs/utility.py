import random
import time
import discord
from discord.ui import Button, View
from discord.ext import commands, tasks
from replit import db

class Utility(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot
        self.fetch_quotes.start()

    def cog_unload(self):
        self.fetch_quotes.cancel()

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
    async def clear(self, ctx, amount:int):
      await ctx.message.delete()
      await ctx.channel.purge(limit=amount)
      await ctx.channel.send(content=f"Successfully purged {amount} messages from this channel",delete_after=5)
      
    @commands.command(name="quote")
    async def quote(self, ctx):
      view = View()
      quotes = db["quotelist"]
      content = random.choice(quotes)
      if ctx.guild.id == 846263154546573333:
        linkbtn = Button(label="Jump to message", style=discord.Buttonstyle.link, url=content[2])
        view.add_item(linkbtn)
      embed = discord.Embed(description=f"Random quote from {self.bot.get_channel(922440576115281981).mention}", title=content[0])
      embed.set_author(name=content[1])
      await ctx.send(embed=embed, view=view)
        

    @commands.command()
    async def verifymsg(self, ctx):
        await ctx.send("""
        Hi there
This is not really a public server
So pls specify your identity and pin a mod/admin to gain access to the server
Just state which guy u have relation to and you are set
If you are a random don't worry we might also accept you 
""")

    @commands.command("accessgrant", aliases = ["ag"])
    @commands.has_permissions(manage_roles=True)
    async def accessgrant(self, ctx, member:discord.Member):
        msg = await ctx.send(f"""{member.mention} Welcome to The Grinds. 
    Make sure to check out <#906852361081860166> and <#960059349559017522>
    You will be granted access in a couple of seconds""")
        role = discord.utils.get(ctx.guild.roles, name="Gamers/ Everyone")
        time.sleep(3)
        await member.add_roles(role)
        await ctx.message.delete()
        await msg.delete()



def setup(bot: commands.Bot):
    bot.add_cog(Utility(bot))