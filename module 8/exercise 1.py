import mysql.connector
def icao(n):
     sql=f"select name,municipality from airport where ident='{n}'"
     print(sql)
     cursor=connection.cursor()
     cursor.execute(sql)
     result=cursor.fetchall()
     if cursor.rowcount>0:
         for row in result:
             print(f"name of airport is {row[0]} and town is {row[1]}")
connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='your username',
        password='your password',
        autocommit=True,
        collation='utf8mb3_general_ci'
       )
icao_code=input("enter the icao code of airports")
icao(icao_code)