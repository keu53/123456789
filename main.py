from flask import Flask
from flask_ngrok import run_with_ngrok
import os

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/")
def index():
    return "jhghgjhgjhgjh"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)