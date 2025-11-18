from database import db_object

class User:
    def __init__(self, username, email, password, role, balance):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.balance = balance

    # REGISTER
    def register(self):
        query = """
        INSERT INTO Users (username, email, password, role, balance)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (self.username, self.email, self.password, self.role, self.balance)
        db_object.insert_data(query, values)
        print("User berhasil diregistrasi!")

    # LOGIN
    def login(self, username, password):
        query = "SELECT * FROM Users WHERE username = %s AND password = %s"
        values = (username, password)
        result = db_object.fetch_data(query, values)

        if len(result) > 0:
            user_data = result[0]  # ambil baris pertama
            print("Login berhasil!")
            print(f"Selamat datang, {user_data[0]}! (Role: {user_data[3]}, Balance: {user_data[4]})")
            return user_data
        else:
            print("Username atau password salah!")
            return None
        
user_object = User("a", "a", "a", "a", 100) # user_object.register() 
user_object.login("ab", "a")
