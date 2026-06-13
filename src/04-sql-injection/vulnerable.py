import sqlite3

from flask import Flask, request

app = Flask(__name__)
conn = sqlite3.connect(":memory:", check_same_thread=False)

@app.route("/login", methods=["POST"])
def handler():
    username: bytes = request.json["username"]

    db_query = conn.cursor().execute(f"SELECT * FROM users WHERE username = '{username}'").fetchall()
    print(db_query)

    return "OK"

if __name__ == "__main__":
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'secret')")
    cursor.execute("INSERT INTO users VALUES ('user', 'secret')")
    conn.commit()

    app.run(debug=True)

