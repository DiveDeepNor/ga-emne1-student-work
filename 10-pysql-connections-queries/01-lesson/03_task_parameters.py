import mysql.connector
from mysql.connector import Error

try:
    print("Connecting to the database...")
    with mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password= "gokstad",
        database= "world"
    ) as connection:
        print("Connected to MySQL!")

        with connection.cursor() as cursor:
            sql = ("SELECT Name, Population, CountryCode "
                   "FROM city "
                   "WHERE Name =%s "
            )
            #cont = input("Hvilket kontinent vil du ha?:")
            cursor.execute(sql, (input("Hvilket by vil du ha?:"),))
            rows = cursor.fetchall()
            if not rows:
                print("No city found.")
            else:
                for name, population, countrycode in rows:
                    print(f"{name}: {population}: {countrycode}")
except Error as e:
    print (f"Error using MySQL!: {e}")