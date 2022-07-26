from discord.ext import commands
from helpers import check_reaction, wait_for_reactions_on_message


class WumpusFoodTour(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wumpusfoodtour(self, ctx):
        conditions = [False] * 4
        message = await ctx.send(f"Hai")
        while not all(condition for condition in conditions):
            conditions = await wait_for_reactions_on_message(message, self.bot, conditions)
            if not all(condition for condition in conditions):
                print(conditions)
                await ctx.send(f'{sum(conditions)} out of 4 items delivered')

        await ctx.send('Problem solved')

def setup(bot):
    bot.add_cog(WumpusFoodTour(bot))
