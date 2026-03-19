class WSManager:
    def __init__(self):
        self.connections = []

    async def connect(self, websocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def disconnect(self, websocket):
        self.connections.remove(websocket)

    async def broadcast(self, message: str):
        for ws in self.connections:
            await ws.send_text(message)
