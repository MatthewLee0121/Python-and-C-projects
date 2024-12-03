import discord
import requests
import logging

# Enable logging to help debug issues
logging.basicConfig(level=logging.DEBUG)

# Set up the bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Discord bot token
DISCORD_TOKEN = 'your_token_here'

# The URL of the chart image (replace with actual image URL)
CHART_IMAGE_URL = "https://pump.fun/cdc4a082-448a-48ef-8496-dd9d0b5cab9d"

# Channel ID where you want to send the message (replace with your actual channel ID)
CHANNEL_ID = 123456789012345678

@client.event
async def on_ready():
    try:
        print(f'Logged in as {client.user}')
        
        # Get the target channel
        channel = client.get_channel(CHANNEL_ID)
        if channel is None:
            print(f"Channel not found with ID: {CHANNEL_ID}")
            return
        
        # Create an embed with the chart image
        embed = discord.Embed(title="Live Crypto Chart", description="Here’s the latest crypto chart!")
        embed.set_image(url=CHART_IMAGE_URL)  # Set the image URL for the chart

        # Send the embed with the chart image to the channel
        await channel.send(embed=embed)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the bot
client.run(DISCORD_TOKEN)
