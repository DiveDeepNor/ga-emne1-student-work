import mysql.connector
from config_local import DB_CONFIG
from models import City


def get_city(city_id):
    sql = (
        "SELECT Name "
        "FROM city "
        "WHERE ID = %s"
    )
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (city_id,))
            row = cursor.fetchone()
    if row is None:
        return None
    return City(city_id, row[0])


def get_cities(code):
    sql = (
        "SELECT Name, Population "
        "FROM city "
        "WHERE CountryCode = %s "
        "ORDER BY Name ASC"
    )
    with mysql.connector.connect(
        **DB_CONFIG
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (code,))
            return cursor.fetchall()


def insert_city(name):
    sql = (
         "INSERT INTO city "
         "(Name, CountryCode, "
         "District, Population) "
         "VALUES (%s, %s, %s, %s)"
    )
    params = (name, "NOR", "Demo", 0)

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()






