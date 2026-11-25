from shlex import join

import mysql.connector
from config_local import DB_CONFIG
from models import Stays

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