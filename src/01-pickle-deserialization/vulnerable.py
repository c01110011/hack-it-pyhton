import base64
import pickle

from flask import Flask, request

app = Flask(__name__)


@app.route("/load", methods=["POST"])
def handler():
    data_payload: bytes = request.json["data"]
    data_decoded: bytes = base64.b64decode(data_payload)

    return pickle.loads(data_decoded)

if __name__ == "__main__":
    app.run(debug=True)