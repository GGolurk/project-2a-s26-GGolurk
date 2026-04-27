from flask import Flask, request, jsonify
import sqlite3
import json

backend_app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('../backend/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@backend_app.route("/api", methods=["GET"])
def get_all():
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM waveMaps').fetchall()
    conn.close()

    result_list = [dict(row) for row in rows]
    json_output = json.dumps(result_list, indent=4)
    return(json_output), 200

@backend_app.route("/api/new", methods=["POST"])
def add_map():
    # get info from POST request
    data = request.get_json()  # parses incoming json
    map_name = data[0].get("map")
    map_description = data[0].get("description")
    map_spu = data[0].get("spu")
    # TODO: Input validation on all fields prior to database insertion!

    # Connect to DB and insert information
    conn = get_db_connection()
    conn.execute('INSERT INTO waveMaps (map, description, spu) VALUES (?, ?, ?)',
                 (map_name, map_description, map_spu))
    conn.commit()
    conn.close()
    return jsonify({"map": map_name}), 201

@backend_app.route("/api/remove", methods=["POST"])
def remove_map():
    data = request.get_json()
    map_name = data[0]
    #TODO validate here too

    conn = get_db_connection()
    conn.execute('DELETE FROM waveMaps WHERE map = ?',
                 (map_name,))
    conn.commit()
    conn.close()
    return jsonify(map_name), 200

if __name__ == "__main__":
    backend_app.run(port=5001, debug=True)