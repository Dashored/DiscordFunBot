import os
from dotenv import load_dotenv
from settings import Settings
from fun_bot import FunBot





if __name__ == "__main__":
    load_dotenv(dotenv_path="config/token.env")
    settings = Settings.load_from_config()
    bot = FunBot(settings)
    token = os.getenv("TOKEN")
    bot.run(token)