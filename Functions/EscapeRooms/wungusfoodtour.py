from discord.ext import commands
from helpers import wait_for_reactions_on_message
from constants import food_tour_intro_message, food_tour_solutions
import operator


class WungusFoodTour(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wungusfoodtour(self, ctx):
        conditions = [False] * 4
        message = await ctx.send(food_tour_intro_message)
        while not all(condition for condition in conditions):
            conditions = await wait_for_reactions_on_message(message, self.bot, conditions)
            if not all(condition for condition in conditions):
                words_guessed = ",".join(map(operator.itemgetter(0), filter(lambda x: x[1], zip(food_tour_solutions, conditions))))
                await ctx.send(f'{sum(conditions)} out of 4 items delivered. Words guessed correctly so far: {words_guessed}')

        await ctx.send('Problem solved')
        # TODO: Give escape room participators role to unlock next room(s)

def setup(bot):
    bot.add_cog(WungusFoodTour(bot))
