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

    # Using frontend security for the backend.
    # It's not duplication if someone malicious skips the frontend security!
    if len(map_name) > 20 or len(map_description) > 250 or len(map_spu) > 3:
        return jsonify("error"), 400

    try:
        float(map_spu)
        if map_spu[1] != '.' or float(map_spu) >= 4.0 or float(map_spu) < 0.0:
            return jsonify("error"), 400
    except ValueError:
        return jsonify("error"), 400

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

    conn = get_db_connection()
    conn.execute('DELETE FROM waveMaps WHERE map = ?',
                 (map_name,))
    conn.commit()
    conn.close()
    return jsonify(map_name), 200

if __name__ == "__main__":
    backend_app.run(port=5001, debug=True)