from flask import Flask

from config import DEBUG

app = Flask('LP_Project')


@app.route("/")
def hello():
    return "Привет!"


if __name__ == "__main__":
    app.run(debug=DEBUG)
