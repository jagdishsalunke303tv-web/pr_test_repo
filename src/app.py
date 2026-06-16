from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("demo.db")

@app.get("/search")
def search():
    q = request.args.get("q", "")
    # FIXED: SQL injection via parameterized query
    sql = "SELECT id, name FROM products WHERE name LIKE ?"
    con = get_db()
    cur = con.cursor()
    cur.execute(sql, (f'%{q}%',))
    return {"results": cur.fetchall()}

if __name__ == "__main__":
    app.run()