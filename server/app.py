from robyn import Robyn, Request

app = Robyn(__file__)


@app.get("/", const=True)
def index(request: Request):
    return "Hello World!"


if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
