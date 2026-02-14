from flask import Flask, render_template, request, redirect
import sqlite3
from difflib import SequenceMatcher

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def highlight_match(text, keyword):
    words = text.split()
    highlighted = []
    for w in words:
        if similarity(w, keyword) > 0.6:
            highlighted.append(f"<mark>{w}</mark>")
        else:
            highlighted.append(w)
    return " ".join(highlighted)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()

    if request.method == "POST":
        item_type = request.form["type"]
        item_name = request.form["item_name"]
        location = request.form["location"]
        description = request.form["description"]

        conn.execute(
            "INSERT INTO items (type, item_name, location, description, status) VALUES (?, ?, ?, ?, 'active')",
            (item_type, item_name, location, description)
        )
        conn.commit()
        return redirect("/")

    lost_items = conn.execute(
        "SELECT * FROM items WHERE type='Lost' AND status='active'"
    ).fetchall()

    found_items = conn.execute(
        "SELECT * FROM items WHERE type='Found' AND status='active'"
    ).fetchall()

    matches = []

    for lost in lost_items:
        for found in found_items:
            score = similarity(lost["item_name"], found["item_name"])
            if score > 0.6:
                matches.append({
                    "lost_id": lost["id"],
                    "found_id": found["id"],
                    "item": lost["item_name"],
                    "lost_desc": highlight_match(lost["description"], found["item_name"]),
                    "found_desc": highlight_match(found["description"], lost["item_name"]),
                })

    conn.close()
    return render_template("index.html", lost_items=lost_items, found_items=found_items, matches=matches)

@app.route("/resolve/<int:lost_id>/<int:found_id>")
def resolve(lost_id, found_id):
    conn = get_db_connection()
    conn.execute("UPDATE items SET status='resolved' WHERE id=?", (lost_id,))
    conn.execute("UPDATE items SET status='resolved' WHERE id=?", (found_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

