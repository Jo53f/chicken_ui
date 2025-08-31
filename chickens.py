from db_connection import DatabaseConnection
from chicken import Chicken

class Chickens:

    def __init__(self):
        self.chickens = []
        self.database = DatabaseConnection(
            host = "localhost",
            user = "dev",
            password = "dev_pass",
            database = "chicken_db"
        )
        self.database.connect()
        self.load_chickens()

    def add_chicken(self, chicken):
        chicken_id = self.database.add_to_database(chicken) # Retrieve id assigned by database to set chicken id locally
        chicken.set_id(chicken_id)
        self.chickens.append(chicken)

    def remove_chicken(self, id):
        chicken = self.chickens.pop(id)
        self.database.delete_from_database(chicken.get_id())

    def change_name(self, id, name):
        self.chickens[id].change_name(name)
        self.database.update_in_database(self.chickens[id].get_id(), name)

    def print_chickens(self):
        id = 0
        for chicken in self.chickens:
            print(f"{id} : {chicken.get_name()}")
            id += 1

    def return_chickens(self):
        return self.chickens

    def reload_chickens(self):
        self.chickens = []
        self.load_chickens()

    def load_chickens(self):
        chicken_data = self.database.load_from_database()
        for chicken in chicken_data:
            self.chickens.append(Chicken(chicken[1], chicken[0]))