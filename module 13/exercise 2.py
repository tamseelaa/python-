from flask import Flask, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/flight_game'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Airport(db.Model):
    __tablename__ = 'airport'
    icao_code = db.Column(db.String(4), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __init__(self, icao_code, name, location):
        self.icao_code = icao_code
        self.name = name
        self.location = location

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "ICAO": self.icao_code,
            "Name": self.name,
            "Location": self.location
        }
@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    airport = Airport.query.filter_by(icao_code=icao_code).first()

    if airport:
        return jsonify(airport.to_dict())
    else:
        return Response(
            '{"error": "Airport not found"}',
            status=404,
            mimetype='application/json'
        )

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)