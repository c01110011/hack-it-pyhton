import subprocess

from flask import Flask, request

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def handler():
    hostname = request.args.get("hostname")

    subprocess.run(["ping", "-c", "1", hostname])

    return "PONG"

if __name__ == "__main__":
    app.run(debug=True)