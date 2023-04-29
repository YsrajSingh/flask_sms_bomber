from flask import Flask
from App.views import bomber

app = Flask(__name__)

@app.route("/")
def index():
    return '! Program Initiated ! , LOADING'

@app.route("/api/<number>")
def api(number):
    return bomber(number)

@app.route("/api/<number>/<count>")
def api(number, count):
    return bomber(number, count)

if __name__ == "__main__":
    app.run()
