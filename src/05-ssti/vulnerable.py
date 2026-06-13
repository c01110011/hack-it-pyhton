from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/dashboard", methods=["POST"])
def handler():
    template_str = "Hello, " + request.json["name"] + "!"
    print(render_template_string(template_str))
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)

