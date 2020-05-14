from discord.ext import commands
from os import environ
import build
import skill_order
import tier_list

bot = commands.Bot(command_prefix='>')

@bot.command()
async def get_build(ctx, champ, lane):
    data = build.get(lane, champ)
    str = ''
    for i in data:
        build_items = ''
        for j in i[1]:
            build_items += j
            build_items += ', '
        str = str + i[0] + ': ' + build_items[:len(build_items) - 2] + '\n'
    await ctx.send(str)


@bot.command()
async def get_skills(ctx, champ, lane):
    data = skill_order.get(lane, champ)
    str = '->'.join(data)
    await ctx.send(str)


@bot.command()
async def get_tier(ctx, lane):
    place, name, win_rate, ban_rate = tier_list.get(lane)
    str = "\n" + lane.upper() + " TIER LIST\n\nTier\t\tName\t\tWin Rate\tBan Rate\n"
    for i in range(0, len(place)):
        if len(name[i]) >= 8:
            str = str + place[i] + "\t\t" + name[i] + "\t" + win_rate[i] + "\t\t" + ban_rate[i] + "\n"
        else:
            str = str + place[i] + "\t\t" + name[i] + "\t\t" + win_rate[i] + "\t\t" + ban_rate[i] + "\n"
    await ctx.send(str)

bot.run(environ['DISC_BOT_KEY'])
