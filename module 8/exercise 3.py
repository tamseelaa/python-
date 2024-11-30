import mysql.connector
from geopy import distance


connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='your username',
        password='your password',
        autocommit=True,
        collation='utf8mb3_general_ci'
    )


def coordinate(icao_x,icao_y):
    sql = f"select latitude_deg,longitude_deg from airport  where gps_code='{icao_x}' or gps_code='{icao_y}';"
    print (sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        distance_in_km=distance.distance(result[0],result[1]).kilometers
        print(f"Distance between {icao_x} and {icao_y} : {distance_in_km} Kilometer")
    else:
        print("invalid one or both entry")

icao_x=input("enter icao code of any airport").upper()
icao_y=input("enter icao code of any airport").upper()
coordinate(icao_x,icao_y)
