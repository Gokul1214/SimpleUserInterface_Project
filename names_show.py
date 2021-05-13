from names_database import Database

class Names:

    def __init__(self, name, year, gender, nameCount, total):
        self._name = name
        self._year = year
        self._gender = gender
        self._nameCount = nameCount
        self._total = total

    def get_name(self):
        return self._name

    def get_year(self):
        return self._year

    def get_gender(self):
        return self._gender

    def get_nameCount(self):
        return self._nameCount

    def get_total(self):
        return self._total

    @staticmethod
    def fetch_names(gender, name):
        return Database.fetch_names(gender, name)

class ShowGender:
    GENDER = "-- All Genders --"

    def __init__(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

    @staticmethod
    def fetch_gender():
        return Database.fetch_gender()