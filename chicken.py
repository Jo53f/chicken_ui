class Chicken():
    def __init__(self, name, chicken_id = 0):
        self.name = name
        self.id = chicken_id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def change_name(self, name):
        self.name = name

    def __str__(self):
        return self.name
