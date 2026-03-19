import discord
import asyncio
from activities import get_activity
from ws_manager import WSManager

ws = WSManager()

class BotSession:
    def __init__(self, token):
        self.token = token
        self.client = discord.Client(intents=discord.Intents.all())
        self.task = None

    async def run(self):
        @self.client.event
        async def on_ready():
            await ws.broadcast(f"[READY] {self.client.user} started")

        @self.client.event
        async def on_error(event, *args, **kwargs):
            await ws.broadcast(f"[ERROR] {event}")

        try:
            await self.client.start(self.token)
        except Exception as e:
            await ws.broadcast(f"[TOKEN ERROR] {str(e)}")

    async def stop(self):
        try:
            await self.client.close()
            await ws.broadcast(f"[STOPPED] Bot closed")
        except:
            pass


class BotManager:
    def __init__(self):
        self.sessions: list[BotSession] = []

    async def start_all(self, tokens: list[str]):
        for t in tokens:
            session = BotSession(t)
            self.sessions.append(session)
            session.task = asyncio.create_task(session.run())
        await ws.broadcast("[SYSTEM] All bots started")

    async def stop_all(self):
        for s in self.sessions:
            await s.stop()

        self.sessions.clear()
        await ws.broadcast("[SYSTEM] All bots stopped")

    async def apply_status(self, activity_type: str, text: str):
        for bot in self.sessions:
            try:
                activity = get_activity(activity_type, text)
                await bot.client.change_presence(activity=activity)
            except:
                pass

        await ws.broadcast("[STATUS] Updated on all bots")
