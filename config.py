#___Every Variable Is Mandatory/Required So Fill Those With Causion___#


import logging

#--------------------------------------------------------------------------------------------------------------------------#
# Telegram API credentials
API_ID = 29171167 # Replace with your API_ID 
API_HASH = "7ea2149629e445936619f06a3c0dc716" # Replace with your HASH
BOT_TOKEN = "" # Replace with your BOT TOKEN
BOT_UN = "akmoviezhub_bot" # Replace with your BOT Username Without @


# MongoDB setup
DB_URL = "mongodb+srv://ak:ak@cluster0.snpjz8c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" # Replace with your mongo db url
DB_NAME = "Cluster0" # Do Need To Change This 

# Admin and Channel details
ADMIN = 7251898668  # Replace with your Telegram user ID
CHANNEL = "-1002442422204" # Replace with your force sub channel username. add bot as admin in yourforce sub channel before start the bot  
DB_CHANNEL_UN = "moviesmod_moviesverse"  # Replace with your File store channel username .Must Be Public
IS_NOTIFY = "True"   # "True" or "False". If "True" Then It Will Send New Aired Chapter Notification In DM

# Download directory
DOWNLOAD_DIRECTORY = "./downloads" # Do Need To Change This

# Copyright Banner
BANNER_PATH = "banner.jpg" # Replace with your Copyright Banner Path

#--------------------------------------------------------------------------------------------------------------------------#

# Logging configuration
LOGGING_CONFIG = {  # Do Not Change This
    'level': logging.INFO,
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'handlers': [
        logging.FileHandler("manga_bot.log"),
        logging.StreamHandler()
    ]
}
