"""
AppID: 958079131780796456
Public key: 8137e84974c5c83f755d8707ce7baed4b14241d7166d52b232370c818b669f3a

Bot token: OTU4MDc5MTMxNzgwNzk2NDU2.YkIGuQ.GD0kKgAwAz5AVOiTNsKX_B340ms
Permisions Int: 534723950672
"""

# bot.py
import asyncio
from makePrediction import predict_h1, predict_D

import os, discord, datetime
from discord.ext import commands, tasks



bot = commands.Bot(command_prefix="!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!btc'):
        await message.channel.send(("-"*40) + "\n" +
            "Daily Bitcoin Prediction: " + str(predict_D()[0]) + "\n" + 
            "Confidence: " + str(predict_D()[1]) + "%" + "\n" +
            "\n" +
            "Hourly Bitcoin Prediction: " + str(predict_h1()[0]) + "\n" +
            "Confidence: " + str(predict_h1()[1]) + "%" + "\n" + 
            ("-"*40))


async def schedule_hourly_message():
	while True:
		
		channel = bot.get_channel(958081115409756251)

		await channel.send(("-"*40) + "\n" + 
                     "Hourly Bitcoin Prediction: " + str(predict_h1()[0]) + "\n" + 
                     "Confidence: " + str(predict_h1()[1]) + "%" + "\n" + 
                     ("-"*40))
  
		now = datetime.datetime.now()
		then = now + datetime.timedelta(hours=1)
		wait_time = (then-now).total_seconds()
		await asyncio.sleep(wait_time)

		


async def schedule_daily_message():
    
    
	while True:
		
		channel = bot.get_channel(958081115409756251)

		await channel.send(("-"*40) + "\n" + 
                     "Daily Bitcoin Prediction: " + str(predict_D()[0]) + "\n" + 
                     "Confidence: " + str(predict_D()[1]) + "%\n" + 
                     ("-"*40))
		
		now = datetime.datetime.now()
		then = now + datetime.timedelta(days=1)

		wait_time = (then-now).total_seconds()
		await asyncio.sleep(wait_time)

		



@bot.event
async def on_ready():
	print(f"Loggined in as: {bot.user.name}")
	
	await schedule_hourly_message()
	await schedule_daily_message()

    
bot.run(os.getenv('BOT_TOKEN'))
