from database import db_object

class User:
    def __init__(self, username, email, password, role, balance):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.balance = balance

    def register(self):
        

        query = """
        INSERT INTO Users (username, email, password, role, balance)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (self.username, self.email, self.password, self.role, self.balance)
        db_object.insert_data(query, values)
        print("User berhasil diregistrasi!")
  
    
        

