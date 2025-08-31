class Chicken():
    def __init__(self, name, chicken_id = 0):
        self.name = name
        self.id = chicken_id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def set_id(self, chicken_id):
        self.id = chicken_id

    def change_name(self, name):
        self.name = name
