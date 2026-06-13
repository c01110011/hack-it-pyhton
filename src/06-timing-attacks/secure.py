import hmac

from flask import Flask, request

app = Flask(__name__)

SECRET_TOKEN = "supersecrettoken123"

@app.route("/validate", methods=["POST"])
def handler():
    token = request.json["token"]

    if hmac.compare_digest(token, SECRET_TOKEN):
        return "OK"
    return "UNAUTHORIZED", 401

if __name__ == "__main__":
    app.run(debug=True)

