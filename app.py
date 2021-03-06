from flask import Flask, request
from flask_cors import CORS, cross_origin
import sqlite3
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

@app.route("/", methods=['GET'])
@cross_origin()
def index():
    return "You are not supposed to be here.", 200

@app.route("/api/new", methods=['POST'])
@cross_origin()
def post_query():
    a, b = run_query(request.json)
    print(request.json)
    return a, b

def run_query(data):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    results = []
    try:
        for row in cur.execute(data["query"]):
            results.append(row)
        json_obj = json.dumps(results)
        print(json_obj)
        return json_obj, 200
    except sqlite3.Error as e:
        return str(e), 500
