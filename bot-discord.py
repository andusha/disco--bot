import discord
from discord.ext import commands

TOKEN = 'NzMxMDk0MzA3NjAzMzQ5NTc1.XwhWrA.6oIAa1QPw5pmve7qBxOhh66hJ0M'

bot = commands.Bot(command_prefix='`')
@bot.command(pass_context=True)
async def finger(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)
    
bot.run(TOKEN)
