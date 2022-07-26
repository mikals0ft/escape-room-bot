from discord.ext import commands
from helpers import wait_for_reactions_on_message
from constants import FOOD_TOUR_INTRO_MESSAGE, FOOD_TOUR_SOLUTIONS
import operator


class WungusFoodTour(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wungusfoodtour(self, ctx):
        conditions = [False] * 4
        message = await ctx.send(FOOD_TOUR_INTRO_MESSAGE)
        while not all(condition for condition in conditions):
            conditions = await wait_for_reactions_on_message(message, self.bot, conditions)
            words_guessed = ",".join(map(operator.itemgetter(0), filter(lambda x: x[1], zip(FOOD_TOUR_SOLUTIONS, conditions))))
            await ctx.send(f'{sum(conditions)} out of 4 items delivered. Words guessed correctly so far: {words_guessed}')

        await ctx.send('Problem solved')
        # TODO: Give escape room participators role to unlock next room(s)


def setup(bot):
    bot.add_cog(WungusFoodTour(bot))
