from datetime import datetime


class User:
    def __init__(self, name, birth_year):
        self.name: str = name
        self.birth_year: int = birth_year

    def get_name(self):
        return self.name.upper()

    def age(self, current_year=datetime.now().year):
        return current_year - self.birth_year
