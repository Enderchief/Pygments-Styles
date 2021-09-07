from os import getenv
from pincer import Client
from dotenv import load_dotenv

load_dotenv()


class Bot(Client):
    @Client.event
    async def on_ready(self):
        print(f'Bot logged in on as {self.bot}')


bot = Bot(getenv("TOKEN"))