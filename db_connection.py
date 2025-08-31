import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database, port = 3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
            port = self.port
        )
        self.cursor = self.connection.cursor()

    def load_from_database(self):
        self.cursor.execute("SELECT * FROM chicken")
        return self.cursor.fetchall()

    def add_to_database(self, chicken):
        self.cursor.execute(f"INSERT INTO chicken (chicken_name) VALUES ('{chicken.get_name()}')")
        chicken_id = self.cursor.lastrowid # Retrieves the (int) primary key of the last row
        self.connection.commit()
        return chicken_id

    def delete_from_database(self, chicken_id):
        self.cursor.execute(f"DELETE FROM chicken WHERE chicken_id = {chicken_id}")
        self.connection.commit()

    def update_in_database(self, chicken_id, chicken_name):
        self.cursor.execute(f"UPDATE chicken SET chicken_name = '{chicken_name}' WHERE chicken_id = {chicken_id}")
        self.connection.commit()