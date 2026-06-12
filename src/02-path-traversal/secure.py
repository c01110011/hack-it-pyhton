from pathlib import Path

from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/files", methods=["GET"])
def handler():
    filename = request.args.get("filename")
    request_base_dir = Path(__file__).parent.joinpath("files")
    requested_file = request_base_dir.joinpath(filename)

    resolved = requested_file.resolve()
    if not resolved.is_relative_to(request_base_dir.resolve()):
        abort(403)

    return requested_file.read_bytes()

if __name__ == "__main__":
    base_dir = Path(__file__).parent.joinpath("files")
    Path.mkdir(base_dir, exist_ok=True)

    test_file = base_dir.joinpath("test.txt")
    test_file.write_text("hello world")

    app.run(debug=True)