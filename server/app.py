from robyn import Response, Robyn, Request, WebSocket, WebSocketConnector
from collections import defaultdict
from robyn.logger import logger
from example import say_hello # type: ignore

app = Robyn(__file__)

ws_logs = WebSocket(app, "/logs")
ws_state = WebSocket(app, "/state")

websocket_state = defaultdict(int)

@app.before_request()
async def log_request(request: Request):
    logger.info(f"Received request: %s", request)

@app.after_request()
async def log_response(response: Response):
    logger.info(f"Sending response: %s", response)
    
@app.get("/", const=True)
def index(request: Request):
    return "Hello World!"

@ws_logs.on("connect")
async def notify_connect():
    return "Connected to notifications"

@ws_logs.on("message")
async def message(ws: WebSocketConnector, msg: str, global_dependencies) -> str:
    websocket_id = ws.id
    state = websocket_state[websocket_id]
    await ws.async_send_to(websocket_id, "This is a message to self")
    x  = say_hello()
    print(x)
    return ""

@ws_logs.on("close")
async def notify_close():
    return "Disconnected from notifications"


if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
