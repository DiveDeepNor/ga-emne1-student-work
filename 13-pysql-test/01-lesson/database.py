import mysql.connector
from config_local import DB_CONFIG
from models import City


def get_city(city_id):
    sql = (
        "SELECT ID, Name, CountryCode, District, Population "
        "FROM city "
        "WHERE ID = %s"
    )
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (city_id,))
            row = cursor.fetchone()
    if row is None:
        return None
    return City(city_id, row[1], row[2], row[3], row[4])


def get_cities(code):
    sql = (
        " SELECT ID, city.Name AS CityName, country.Name AS CountryName, city.Population AS CityPopulation "
        " FROM city "
        " JOIN country ON country.Code = city.CountryCode "
        " WHERE CountryCode = %s "
        " ORDER BY city.Name, city.ID;"
    )
    with mysql.connector.connect(
        **DB_CONFIG
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (code,))
            return cursor.fetchall()


def insert_city(name):
    sql = (
         "INSERT INTO city (Name, CountryCode, District, Population)"
         "VALUES (%s, %s, %s, %s)"
    )
    params = (name, "NOR", "Demo", 0)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()

def update_city(city_id, name):
    sql = (
         "UPDATE city "
         "SET Name = %s "
         "WHERE ID = %s"
    )
    params = (name, city_id)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()


def delete_city(city_id):
    sql = (
         "DELETE FROM city "
         "WHERE ID = %s"
    )
    params = (city_id,)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()


