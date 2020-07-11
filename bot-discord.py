import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='`')
@bot.command(pass_context=True)
async def finger(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)


bot.run(str(os.environ.get('BOT_TOKEN')))
