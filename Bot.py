import asyncio
import discord
from discord.ext import commands
from typing import List, Optional

import settings

intents = discord.Intents.default()

cogs: list = ["Functions.Fun.games", "Functions.Fun.gameinfos", "Functions.Fun.otherfuncommands", "Functions.Info.info",
        "Functions.Misc.misc", "Functions.NewMember.newmember", "Functions.Admin.admin"]

client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))
    for cog in cogs:
        try:
            print(f"Loading cog {cog}")
            client.load_extension(cog)
            print(f"Loaded cog {cog}")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))

async def wait_for_reaction_on_message(confirm: str,
                                       cancel: Optional[str],
                                       message: discord.Message, author: discord.Member, bot: discord.Client,
                                       timeout: float = 30.0) -> bool:
    await message.add_reaction(confirm)
    await message.add_reaction(cancel)

    def check(reaction, user):
        return user == author and str(reaction.emoji) == confirm or cancel

    while True:
        try:
            react, reactor = await bot.wait_for('reaction_add', timeout=timeout, check=check)
        except asyncio.TimeoutError:
            return False
        if react.message.id != message.id:
            continue
        if str(react.emoji) == confirm and reactor == author:
            return True
        elif str(react.emoji) == cancel and reactor == author:
            return False

async def wait_for_multiple_reactions(reactions: List[str],
                                      message: discord.Message,
                                      member: discord.Member, bot: discord.Client,
                                      needed: int, timeout: float = 300.0) -> bool:
    for reaction in reactions:
        await message.add_reaction(reaction)

    def check(reaction, user):
        return user == member and str(reaction.emoji) in reactions

    current_reactions = 0
    while current_reactions < needed:
        try:
            react, reactor = await bot.wait_for('reaction_add', timeout=timeout, check=check)
        except asyncio.TimeoutError:
            return False
        if react.message.id != message.id:
            continue
        if str(react.emoji) in reactions and reactor == member:
            # make edit on image
            current_reactions += 1
    return await wait_for_reaction_on_message(YES, NO, message, member, bot)


client.run(settings.TOKEN)
