from typing import Optional
from disnake.ext import commands
from aiohttp import ClientSession
from disnake.flags import Intents
from loguru import logger
import pkgutil
import traceback


class MusicBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        intents = Intents.all()
        intents.dm_messages = False

        super().__init__(command_prefix='m ', intents=intents,
                         case_insensitive=True, help_command=None, reload=True)
        self.session: Optional[ClientSession] = None
        self.logger = logger

    async def login(self, token: str) -> None:
        self.session = ClientSession()

        return await super().login(token)

    async def on_ready(self):
        print(
            f"-------Bot Initialization-------\n"
            f"Bot name: {self.user.name}\n"
            f"Bot ID: {self.user.id}\n"
            f"--------------------------------\n"
        )

    def load_cogs(self, exts) -> None:
        """
        A method that loads all cogs in the cogs folder.
        :param exts:
        :return:
        """
        for m in pkgutil.iter_modules(exts):
            module = f"cogs.{m.name}"
            try:
                self.load_extension(module)
                self.logger.info(f"Loaded extension '{m.name}'", __name="MusicBot")
            except Exception as e:
                traceback.format_exc(e)

    async def on_disconnect(self):
        self.clear()
        self.logger.info("Disconnected from Discord", __name="MusicBot")
        await self.session.close()
        self.logger.info("Session closed", __name="MusicBot")