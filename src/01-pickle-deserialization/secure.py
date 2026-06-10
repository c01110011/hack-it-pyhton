import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/load", methods=["POST"])
def handler():
    return json.dumps(request.json["data"])

if __name__ == "__main__":
    app.run(debug=True)