import mysql.connector
def area(n):
    sql = f"select name,type from airport where iso_country ='{n}'order by type,name "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Name: {row[0]} and Type: {row[1]}")
connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='your username',
        password='your password',
        autocommit=True,
        collation='utf8mb3_general_ci'
       )
area_code=input("Enter country code").upper()
area(area_code)