from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("demo.db")

@app.get("/search")
def search():
    q = request.args.get("q", "")
    # VULNERABLE: SQL injection via string concatenation
    sql = f"SELECT id, name FROM products WHERE name LIKE '%{q}%'"
    con = get_db()
    cur = con.cursor()
    cur.execute(sql)
    return {"results": cur.fetchall()}

if __name__ == "__main__":
    app.run()
