from robyn import Robyn, Request, WebSocket

app = Robyn(__file__)

ws = WebSocket(app, "/logs")

@app.get("/", const=True)
def index(request: Request):
    return "Hello World!"

@ws.on("connect")
async def notify_connect():
    return "Connected to notifications"

@ws.on("message")
async def notify_message(message):
    return f"Received: {message}"

@ws.on("close")
async def notify_close():
    return "Disconnected from notifications"


if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
