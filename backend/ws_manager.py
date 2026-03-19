class WSManager:
    def __init__(self):
        self.active = []

    async def connect(self, ws):
        await ws.accept()
        self.active.append(ws)

    async def broadcast(self, msg):
        for ws in self.active:
            await ws.send_text(msg)
