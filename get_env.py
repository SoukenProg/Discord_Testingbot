import os
from os.path import join, dirname
from dotenv import load_dotenv

#setup
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#Discord API
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

