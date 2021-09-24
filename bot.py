import discord
from discord import message
from discord import user
from discord import Guild
from discord.client import Client
from discord.ext import commands
from discord.utils import get
import random


intents = discord.Intents.all()
discord.member = True
client = commands.Bot(command_prefix="*",intents = intents)

@client.event
async def on_ready():
    print("SkeppyIsBadAtPVP's Little Minion is Ready!")
    await client.change_presence(activity=discord.Game('SkeppyIsBadAtPVP\'s Place'))

@client.event
async def on_member_join(member):
    print(f'{member} Has Joined The Server!')
    channel = client.get_channel(881216102682730506)
    await channel.send(f'{member.mention}, Welcome To The Server! :)')
    await member.send(f'```Thank You For Joining the server :)```')

@client.event
async def on_member_remove(member):
    await member.send(f'```You left the server :(```')
    print(f"{member} Has Left The Server :(")
    channel = client.get_channel(881216102682730506)
    await channel.send(f'{member.mention} Left The Server :(')
    
@client.command()
async def activatereactrole(ctx):
    channel = client.get_channel('889919006260228207')
    if not channel:
        return

    await channel.send("d")
    roleid = 852396532501053440
    
    # role = discord.utils.get(user.guild.roles, name="Peasant")
    # role = get(Guild.roles, id=roleid)
    # role = discord.utils.get(Guild.roles,name="Peasant")
    # message = await ctx.send_message(channel, "React to this message with 👍 to get access to the server (This also means you are agreeing to the rules.)")
    # while True:
    #     reaction = await client.wait_for_reaction(emoji="👍", message=message)
    #     await client.add_roles(reaction.message.author, role)



@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]

    await ctx.send(f'The Magical 8ball says : {random.choice(responses)}')


@client.command()
async def clear(ctx, amount = 99999999999999999999999):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.send(f'```You have been kicked for \"{reason}\"```')
    await ctx.send(f"You have sucessfully kicked {member.mention}.")
    reason = reason
    await member.kick(reason=reason)
    channel = client.get_channel(889368593114988604)
    await channel.send(f'{member.mention} was kicked by {ctx.author.mention}.')

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.send(f"You have sucessfully banned {member.mention}.")
    await member.send(f'```You have been banned for \"{reason}\"```')
    reason = reason
    await member.ban(reason=reason)
    channel = client.get_channel(889368593114988604)
    await channel.send(f'{member.mention} was banned by {ctx.author.mention}.')
    


@client.command()
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"You have sucessfully unbanned {user.mention}.")
            channel = client.get_channel(889368593114988604)
            await channel.send(f'{user.mention} was unbanned by {ctx.author.mention}.')
            return



@client.command(pass_context = True)
async def mute(ctx, *, member):
    role = discord.utils.get(Guild.roles, name='Muted')
    await client.add_roles(member, role)

@client.command()
async def unmute(ctx, *, member):
    role = discord.utils.get(Guild.roles, name='Muted')
    await client.remove_roles(member, role)



client.run('ODUzMjY4MjQ2Mzc4NDQ2ODQ4.YMS5-g.trWg8migIDFAKfaLI4XIIxKhjGA')