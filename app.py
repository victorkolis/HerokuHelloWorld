from flask import Flask

app = Flask(__name__)


@app.get("/home")
def index():
    return "Hello World"


app.run(port=5000)
