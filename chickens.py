class Chickens():
    def __init__(self):
        self.chickens = []

    def add_chicken(self, chicken):
        self.chickens.append(chicken)

    def remove_chicken(self, id):
        self.chickens.pop(id)

    def change_name(self, id, name):
        self.chickens[id].change_name(name)

    def print_chickens(self):
        id = 0
        for chicken in self.chickens:
            print(f"{id} : {chicken.get_name()}")
            id += 1

    def return_chickens(self):
        return self.chickens