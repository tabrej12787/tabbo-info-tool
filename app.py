from flask import Flask, request, jsonify, render_template
import requests
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

VECTOR_KEY = os.getenv("VECTOR_API_KEY")

db = sqlite3.connect("users.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
api_key TEXT,
expiry TEXT,
limit_day INTEGER
)
""")

db.commit()


@app.route("/")
def admin():

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    return render_template("admin.html", users=users)


@app.route("/create", methods=["POST"])
def create():

    key = request.form["key"]
    expiry = request.form["expiry"]
    limit = request.form["limit"]

    cursor.execute(
        "INSERT INTO users VALUES(?,?,?)",
        (key, expiry, limit)
    )

    db.commit()

    return "API Created"


@app.route("/lookup")
def lookup():

    key = request.args.get("key")
    mobile = request.args.get("mobile")

    cursor.execute(
        "SELECT expiry FROM users WHERE api_key=?",
        (key,)
    )

    user = cursor.fetchone()

    if not user:
        return {"error":"invalid api key"}

    expiry = user[0]

    if datetime.now().date() > datetime.fromisoformat(expiry).date():
        return {"error":"api expired"}

    url=f"https://api.vectorxo.online/lookup?key={VECTOR_KEY}&mobile={mobile}"

    r=requests.get(url)

    return jsonify(r.json())


app.run(host="0.0.0.0", port=5000)
