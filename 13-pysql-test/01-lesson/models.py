class City:
    def __init__(self, city_id, name, country_code, district, population):
        self.id = city_id
        self.name = name
        self.country_code = country_code
        self.district = district
        self.population = population

    @staticmethod
    def clean_name(value):
        name = value.strip()
        if not 1 <= len(name) <= 35:
            raise ValueError('Use 1 to 35 characters.')
        return name