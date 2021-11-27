import time
import os

from loguru import logger
from bot import MusicBot

from utils.Lavalink_run import lavalink_alive

if __name__ == "__main__":

    bot = MusicBot()
    bot.load_cogs("cogs")
    logger.info("All cogs have been successfully loaded", __name="Music Bot")
    lavalink_alive()
    try:
        time.sleep(14)  # Wait for lavalink to start

        bot.run(os.getenv("TOKEN"))
    except KeyboardInterrupt:
        logger.info("Shutting down...", __name="Music Bot")