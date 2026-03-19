from fastapi import FastAPI, WebSocket
from database import DB
from bot_runner import BotManager
from ws_manager import WSManager

app = FastAPI()
db = DB()
bots = BotManager()
ws = WSManager()

@app.get("/bots")
def get_bots():
    return db.get_bots()

@app.post("/bot/add")
def add_bot(token: str):
    db.add_bot(token)
    return {"msg": "Bot Added"}

@app.post("/bot/add/bulk")
def add_bot_bulk(tokens: list[str]):
    for t in tokens:
        db.add_bot(t)
    return {"msg": "Bulk Bots Added"}

@app.post("/bot/start")
async def start_all():
    await bots.start_all(db.get_bots())
    return {"msg": "Bots Started"}

@app.post("/bot/stop")
async def stop_all():
    await bots.stop_all()
    return {"msg": "Bots Stopped"}

@app.websocket("/ws/logs")
async def websocket_logs(ws_conn: WebSocket):
    await ws.connect(ws_conn)
    while True:
        msg = await ws_conn.receive_text()
        await ws.broadcast(msg)
