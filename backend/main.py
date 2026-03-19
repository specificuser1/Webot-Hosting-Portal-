from fastapi import FastAPI, WebSocket
from models import TokenInput, BulkTokens, StatusModel
from database import Database
from bot_runner import BotManager
from ws_manager import WSManager

app = FastAPI()

db = Database()
bots = BotManager()
ws = WSManager()

# -------------------------
#  BOT APIs
# -------------------------

@app.post("/bot/add")
def add_bot(data: TokenInput):
    db.add_bot(data.token)
    return {"msg": "Bot added"}

@app.post("/bot/add/bulk")
def add_bulk(data: BulkTokens):
    db.add_bulk(data.tokens)
    return {"msg": "Bulk bots added"}

@app.get("/bots")
def get_bots():
    return db.get_all()


# -------------------------
#  START / STOP BUTTONS
# -------------------------

@app.post("/bots/start")
async def start_all():
    await bots.start_all(db.get_all())
    return {"msg": "All bots started"}

@app.post("/bots/stop")
async def stop_all():
    await bots.stop_all()
    return {"msg": "All bots stopped"}


# -------------------------
#  SET CUSTOM STATUS
# -------------------------

@app.post("/bots/status")
async def apply_status(data: StatusModel):
    await bots.apply_status(data.activity, data.text)
    return {"msg": "Status Applied"}


# -------------------------
#  WEB SOCKET LOGS
# -------------------------

@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await ws.connect(websocket)

    try:
        while True:
            msg = await websocket.receive_text()
            await ws.broadcast(msg)
    except:
        await ws.disconnect(websocket)
