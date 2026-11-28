class Stays:
    def __init__(self, stay_id, pet_id, room_id, check_in, check_out,
                 pet_name, owner_name, room_number):

        self.stay_id = stay_id
        self.pet_id = pet_id
        self.room_id = room_id
        self.check_in = check_in
        self.check_out = check_out
        self.pet_name = pet_name
        self.owner_name = owner_name
        self.room_number = room_number

    @staticmethod
    def clean_name(value):
        name = value.strip()
        if not 1 <= len(name) <= 35:
            raise ValueError('Use 1 to 35 characters.')
        return name


class Pets:
    def __init__(self, pet_id, owner_id, name, species, breed):

        self.pet_id = pet_id
        self.owner_id = owner_id
        self.name = name
        self.species = species
        self.breed = breed


class Rooms:
    def __init__(self, room_id, room_number, room_type, daily_rate):

        self.room_id = room_id
        self.room_number = room_number
        self.room_type = room_type
        self.daily_rate = daily_rate


class Stay:
    def __init__(self, stay_id, pet_id, room_id, check_in, check_out):

        self.stay_id = stay_id
        self.pet_id = pet_id
        self.room_id = room_id
        self.check_in = check_in
        self.check_out = check_out