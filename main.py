import os
import discord
import requests
import pycoingecko
from discord.ext import commands
from discord.ext.commands import Bot
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

bot = commands.Bot(command_prefix='ar!') # Bot prefix
baseUrl = 'https://api.coingecko.com/api/v3'


@bot.event
async def on_ready():
    print('✅ Auto-React Operational') # This message will show in the console when the bot is online and ready to be used


@bot.event
async def on_message(message):
    if message.channel.id == os.environ['CHANNELID']:
        if 'coin' in message.content:
            await message.add_reaction("👍")
            if 'trending' in message.content:
                result = cg.get_search_trending()
                await message.channel.send('showing trending')
                for item in result.get('coins'):
                  await message.channel.send(item.get('item').get('market_cap_rank'))
                  await message.channel.send(item.get('item').get('id'))  
            if 'ping' in message.content:
                result = cg.ping()
                await message.channel.send(result)
            if 'price' in message.content:
                res = message.content.split()
                result = cg.get_price(ids=res[2], vs_currencies=res[3], include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
                await message.channel.send(result.get('bitcoin'))
            if 'vslist' in message.content:
                result = cg.get_supported_vs_currencies()
                await message.channel.send(result)
                
bot.run(os.environ['TOKEN']) # Paste bot token