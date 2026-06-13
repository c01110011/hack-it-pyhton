from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/dashboard", methods=["POST"])
def handler():
    print(render_template_string("Hello, {{ name }}!", name=request.json["name"]))
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)

