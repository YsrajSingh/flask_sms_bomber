from flask import Flask
from views import bomber

app = Flask(__name__)


@app.route("/<number>")
def test(number):
    return bomber(number)


if __name__ == "__main__":
    app.run()
