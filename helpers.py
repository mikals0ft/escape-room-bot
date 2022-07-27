import asyncio
import discord
from typing import List


def check_reaction(reaction, conditions):
    if 'coffee' in str(reaction.emoji).lower() or str(reaction.emoji) == '☕':
        conditions[0] = True
    elif 'sushi' in str(reaction.emoji).lower() or str(reaction.emoji) == '🍣':
        conditions[1] = True
    elif 'icecream' in str(reaction.emoji).lower() or str(reaction.emoji) == '🍦':
        conditions[2] = True
    elif 'beer' in str(reaction.emoji).lower() or str(reaction.emoji) == '🍺':
        conditions[3] = True
    return conditions

async def wait_for_reactions_on_message(message: discord.Message, bot: discord.Client, conditions) -> List[bool]:

    while True:
        try:
            react, reactor = await bot.wait_for('reaction_add')
        except asyncio.TimeoutError:
            return [False, False, False, False]
        if react.message.id != message.id:
            continue
        if str(react.emoji) == '❌':
            raise Exception('Wungus Food Tour instance terminated')
        return check_reaction(react, conditions)
