import discord
import asyncio
from ws_manager import WSManager

ws = WSManager()

class BotManager:
    def __init__(self):
        self.sessions = []

    async def start_all(self, bots):
        for token in bots:
            asyncio.create_task(self._run_bot(token))

    async def _run_bot(self, token):
        client = discord.Client(intents=discord.Intents.all())

        @client.event
        async def on_ready():
            await ws.broadcast(f"[OK] {client.user} Started")

        @client.event
        async def on_error(event, *args, **kwargs):
            await ws.broadcast(f"[ERROR] {event}")

        try:
            await client.start(token)
        except Exception as e:
            await ws.broadcast(f"[TOKEN ERROR] {e}")

    async def stop_all(self):
        for s in self.sessions:
            await s.close()
        self.sessions.clear()
