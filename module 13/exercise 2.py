from flask import Flask, Response
import json
import mysql.connector
app = Flask(__name__)

def get_airport_info(icao_code):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Shahid75',
        database='flight_game',
        autocommit=True,
        collation='utf8mb3_general_ci'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport,game WHERE ident = %s;", (icao_code,))
    data = cursor.fetchone()
    conn.close()
    if data:
        return {
            "ICAO": data[0],
            "Name": data[1],
            "Location": data[2]
        }
    else:
        return None

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    airport_info = get_airport_info(icao)

    if airport_info:
        response = json.dumps(airport_info)
        return Response(response, mimetype='application/json')
    else:
        error_response = json.dumps({"error": "Airport not found"})
        return Response(error_response, status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)