import mysql.connector
from config_local import DB_CONFIG
from models import Stays, Pets, Rooms, Stay


def get_stays():
    sql = (
        'SELECT stays.stay_id, stays.pet_id, stays.room_id, stays.check_in, stays.check_out, pets.name AS pet_name, owners.name AS owner_name, rooms.room_number '
        'FROM stays '
        'JOIN pets ON stays.pet_id = pets.pet_id '
        'JOIN owners ON pets.owner_id = owners.owner_id '
        'JOIN rooms  ON stays.room_id = rooms.room_id'
    )

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

    if not rows:
        return []

    return [Stays(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in rows]


def get_pets():
    sql = (
        'SELECT * '
        'FROM pets '
    )

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

    if not rows:
        return []

    return [Pets(row[0], row[1], row[2], row[3], row[4])
            for row in rows]


def get_rooms():
    sql = (
        'SELECT * '
        'FROM rooms '
    )

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

    if not rows:
        return []

    return [Rooms(row[0], row[1], row[2], row[3])
            for row in rows]


def get_stay(stay_id):
    sql = (
        "SELECT stay_id, pet_id, room_id, check_in, check_out "
        "FROM stays "
        "WHERE stay_id = %s"
    )
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (stay_id,))
            row = cursor.fetchone()
    if row is None:
        return None
    return Stay(row[0], row[1], row[2], row[3], row[4])


def add_stay(pet_id, room_id, check_in, check_out):

    # Sjekker om rommet er ledig
    check_sql = (
        'SELECT stay_id '
        'FROM stays ' 
        'WHERE room_id = %s '
        'and check_in < %s '
        'and check_out > %s '
        'Limit 1'
    )

    insert_sql = (
        'INSERT INTO stays (pet_id, room_id, check_in, check_out) '
        'VALUES (%s, %s, %s, %s)'
    )

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                check_sql,
                (room_id, check_out, check_in)
            )

            # Om rommet er opptatt
            if cursor.fetchone() is not None:
                return False

            # Registrer nytt opphold
            cursor.execute(
                insert_sql,
                (pet_id, room_id, check_in, check_out)
            )

        connection.commit()
    return True


def update_stay(stay_id, pet_id, room_id, check_in, check_out):

    # Sjekke om rommet er opptatt
    check_sql = (
        "SELECT stay_id "
        "FROM stays "
        "WHERE room_id = %s "
        "AND check_in < %s "
        "AND check_out > %s "
        "AND stay_id != %s "
        "LIMIT 1"
    )

    check_params = (room_id, check_out, check_in, stay_id)

    # Oppdatere eksisterende opphold
    sql = (
        'UPDATE stays '
        'SET pet_id = %s, '
        'room_id = %s, '
        'check_in = %s, '
        'check_out = %s '
        'WHERE stay_id = %s'
    )
    params = (pet_id, room_id, check_in, check_out, stay_id)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(check_sql, check_params)

            # Dersom rommet allerede er opptatt
            if cursor.fetchone() is not None:
                return False

            cursor.execute(sql, params)

        connection.commit()

        return True