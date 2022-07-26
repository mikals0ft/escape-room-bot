from constants import ATTENDEE_ROLE_NAME, VALID_ROOM_ROLES
from discord.ext import commands
from discord.role import Role
import discord.utils


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def unlockroom(self, ctx, room_name):
        """
        Picks a random user from the server to win your giveaway.
        """
        if room_name in VALID_ROOM_ROLES:
            room_role: Role = discord.utils.get(ctx.guild.roles, name=room_name)
            attendees_role: Role = discord.utils.get(ctx.guild.roles, name=ATTENDEE_ROLE_NAME)
            for user in attendees_role.members:
                await user.add_roles(room_role, atomic=True)
            await ctx.send(f'{room_name} unlocked')
        else:
            await ctx.send(f'Must specify a valid room role out of the following: {",".join(VALID_ROOM_ROLES)}')

def setup(bot):
    bot.add_cog(Admin(bot))
