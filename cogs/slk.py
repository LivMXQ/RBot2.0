import discord
from discord.ext import commands
from discord.ui import Button, View

class SLK(commands.Cog):
  @discord.slash_command(name="slkrules", guild_ids=[1006924989104136262], default_member_permissions=discord.Permissions.advanced())
  async def slk_rules(self, ctx):

    basic_desc = """\n\n ✦ Follow Discord ToS rules

✦ Follow Bot ToS rules

✦ Use your brain please, I know you are not stupid"""

    respect_desc = """\n\n ✦ Respect everyone equally 

✦ No bullying, harassing or even threatening anyone, this is a serious offence and can lead to a ban/mute

✦ Discrimination, being homophobic and sexually annoying are not welcomed and will lead to a mute

✦ Racial or offensive slurs will lead to a permanent and immediate ban

✦ Staff and Streamers are to be respected, people caught bad-mouthing them in public will be banned/muted

✦ Constructive Criticism and negative feedback are welcomed, but we do not tolerate signs of aggression and entitled demands

✦ Mass pinging members or any staff can lead to a mute

✦ Revealing of ones personal information have a zero tolerance and will lead to a permanent ban"""

    chat_desc = """\n\n ✦ Keep the chat sfw 

✦ NSFW is not allowed and can lead to a mute

✦ Cursing is allowed, but if excessive, it will lead to a curse ban and a mute

✦ Controversial topics such as religon and politics are strictly prohibited and can lead to a mute

✦ Bot commands are only allowed in <#1007177283833974834> and <#1007168917581602836>

✦ Do not flood any of the chats except for <#1007118198258282536> with messages, GIFs, images and stickers, or you will be muted

✦ Images are only allowed in <#1007099377036296192> <#1007899660549116015> and <#1007097901761171566>

✦ We are an English speaking server, so keep your language to English only

✦ No ear-vapes in VC's if caught, you will be banned from <#1007177283833974834>"""

    advertisement_desc = """\n\n ✦ Advertising in the server is **STRICTLY** prohibited, this includes DM advertising, if caught, you will receive and temporary ban""" 

    basic_embed = discord.Embed(title="**__Basic Rules__**", description=basic_desc)
    respect_embed = discord.Embed(title="**__Respect__**", description=respect_desc)
    chat_embed = discord.Embed(title="**__Chat Rules__**", description=chat_desc)
    advertisement_embed = discord.Embed(title="**__Advertising__**", description=advertisement_desc)
    verifying_embed = discord.Embed(title="**__Click on the reaction to verify__**")
    await ctx.channel.send("https://i.ibb.co/6wwgdDp/unknown.png")
    await ctx.channel.send(embed=basic_embed)
    await ctx.channel.send(embed=respect_embed)
    await ctx.channel.send(embed=chat_embed)
    await ctx.channel.send(embed=advertisement_embed)
    msg = await ctx.channel.send(embed=verifying_embed)
    await msg.add_reaction("✅")
  

  @discord.slash_command(name="slkreactionroles", guild_ids=[1006924989104136262], default_member_permissions=discord.Permissions.advanced())
  async def slk_reaction_roles(self, ctx):

    colour_desc = """\n🍎 <@&1007291524406591641>
🍊 <@&1007291817496170647>
🍋 <@&1007292021951696998>
🍏 <@&1007292132467421218>
🍐 <@&1007292227896213526>
🫐 <@&1007292440291582097>
🌊 <@&1007292537335185549>
🍇 <@&1007292743422324777>
🍑 <@&1007292880932585643>
🖤 <@&1007293679746162749> """
    
    pronouns_desc = """\n<:1_:1007984448400261231> <@&1007293692865953892>
<:2_:1007988848292286582> <@&1007293697022496868>
<:3_:1007988872694739014> <@&1007994791662989404>
<:4_:1007988888977035368> <@&1007994981954367548>
<:5_:1007988906249162812> <@&1007995008588189718>"""

    region_desc = """\n 🟥 <@&1008204282354479104>
🟧 <@&1008204394212372480> 
🟨 <@&1008204167250190406>
🟩 <@&1008230244555173979> 
🟦 <@&1008205701430132766> """

    devices_desc = """\n <:mobile_phone:1008533270159441981> <@&1008520374234910801>
<:desktop:1008534327002406965> <@&1008520463472939088>"""

    pings_desc = """\n 📺 <@&1010146238756311040>
    📢 <@&1010146876277927958>
    🪦 <@&1010146948541583423>"""

    
    colour_embed = discord.Embed(title="✦ Colour Roles ✦", description=colour_desc)
    pronouns_embed = discord.Embed(title="დ Pronoun Roles დ", description=pronouns_desc)
    region_embed = discord.Embed(title="❀ Region Roles ❀", description=region_desc)
    devices_embed = discord.Embed(title="¤ Devices Roles ¤", description=devices_desc)
    pings_embed = discord.Embed(title="♪ Pings Role ♪", description=pings_desc)
    
    colour_embed.set_thumbnail(url="https://c.tenor.com/6ZtvhEzg0DkAAAAC/pusheen-unikitty.gif")
    pronouns_embed.set_thumbnail(url="https://c.tenor.com/FtmzXpzx3-QAAAAC/unicorn-pusheen.gif")#oh lol HAHAH
    region_embed.set_thumbnail(url="https://c.tenor.com/xxsRVYaZglcAAAAd/pusheen-kitty.gif") 
    devices_embed.set_thumbnail(url="https://c.tenor.com/Kxh1yHwtE6IAAAAC/pusheen-phone.gif")
    pings_embed.set_thumbnail(url="https://c.tenor.com/sJnOE_eYvFcAAAAC/pusheen.gif")
    
    button_roles_view = ColourRolesView()
    pronouns_view = PronounsView()
    region_view = RegionView()
    devices_view = DevicesView() 
    pings_view = PingsView()
    await ctx.respond("menu created", ephemeral=True)
    await ctx.channel.send("https://i.ibb.co/fnXzX58/self-roles.png")
    await ctx.channel.send(embed=colour_embed, view=button_roles_view)
    await ctx.channel.send(embed=pronouns_embed, view=pronouns_view)
    await ctx.channel.send(embed=region_embed, view=region_view)
    await ctx.channel.send(embed=devices_embed, view=devices_view)
    await ctx.channel.send(embed=pings_embed, view=pings_view)
    await ctx.channel.send("""**__Click on the corresponding emoji to get your role!
Click it again to remove the role__**""")

class PingsView(View):
  def __init__(self):
    super().__init__(timeout=None)
    
  @discord.ui.button(label="📺", custom_id="stream_role")
  async def stream_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Stream Pings 📺")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)
                                              
  @discord.ui.button(label="📢", custom_id="announcement_role")
  async def announcement_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Announcement Pings 📢")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)
  
  @discord.ui.button(label="🪦", custom_id="revival_role")
  async def revival_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Chat Revival Ping 🪦")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)
    
class DevicesView(View):
  def __init__(self):
    super().__init__(timeout=None)
    self.role_names = ["Phone📱", "PC🖥️"]
    
  @discord.ui.button(label="📱", custom_id="phone_role")
  async def phone_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, id=1008520374234910801)
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🖥️", custom_id="pc_role")
  async def pc_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, id=1008520463472939088)
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

class RegionView(View):
  roles = []
  def __init__(self):
    super().__init__(timeout=None)
    self.role_names = ["NA", "SA", "EU", "IN", "AS"]

  @discord.ui.button(label="🟥", custom_id="na_role")
  async def na_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="NA")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🟧", custom_id="sa_role")
  async def sa_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="SA")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🟨", custom_id="europe_role")
  async def europe_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="EU")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🟩", custom_id="india_role")
  async def india_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="IN")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🟦", custom_id="asia_role")
  async def asia_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="AS")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

class PronounsView(View):
  def __init__(self):
    super().__init__(timeout=None)
    self.role_names = ["he/him ❧", "he/they ❧", "she/her ❧", "she/they ❧", "they/them ❧"]

  @discord.ui.button(emoji="<:1_:1007984448400261231>", custom_id="he/him_role")
  async def him_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="he/him ❧")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(emoji="<:2_:1007988848292286582>", custom_id="he/they_role")
  async def they_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="he/they ❧")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(emoji="<:3_:1007988872694739014>", custom_id="she/her_role")
  async def her_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="she/her ❧")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(emoji="<:4_:1007988888977035368>", custom_id="she/they_role")
  async def she_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="she/they ❧")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

      
  @discord.ui.button(emoji="<:5_:1007988906249162812>", custom_id="they/them_role")
  async def them_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="they/them ❧")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)
  

class ColourRolesView(View):
  def __init__(self):
    super().__init__(timeout=None)
    self.role_names = ["Red", "Orange", "Yellow", "Green", "Lime", "Blue", "Aqua", "Purple", "Pink", "Black"]
    
  @discord.ui.button(label="🍎", custom_id="red_role")
  async def red_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Red")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🍊", custom_id="orange_role")
  async def orange_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Orange")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🍋", custom_id="yellow_role")
  async def yellow_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Yellow")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)
  
  @discord.ui.button(label="🍏", custom_id="green_role")
  async def green_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Green")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🍐", custom_id="lime_role")
  async def lime_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Lime")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🫐", custom_id="blue_role")
  async def blue_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Blue")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🌊", custom_id="aqua_role")
  async def aqua_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Aqua")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🍇", custom_id="purple_role")
  async def purple_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Purple")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

  @discord.ui.button(label="🍑", custom_id="pink_role")
  async def pink_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Pink")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)
  
  @discord.ui.button(label="🖤", custom_id="black_role")
  async def black_callback(self, button, interaction):
    role = discord.utils.get(interaction.guild.roles, name="Black")
    if role in interaction.user.roles:
      await interaction.user.remove_roles(role)
      await interaction.response.send_message("Role removed", ephemeral=True)
    else:
      for i in interaction.user.roles:
        if i.name in self.role_names:
          await interaction.user.remove_roles(i)
      await interaction.user.add_roles(role)
      await interaction.response.send_message("Role added", ephemeral=True)

def setup(bot: commands.Bot):
  bot.add_cog(SLK(bot))