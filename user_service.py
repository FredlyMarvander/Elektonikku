from database import db_object
from User import User

class UserService:
      # REGISTER
    

    # LOGIN
    def login(self, username, password):
        query = "SELECT * FROM Users WHERE username = %s AND password = %s"
        values = (username, password)
        result = db_object.fetch_data(query, values)

        if len(result) > 0:
           
            row = result[0]

            
            user = User(
                username=row[0],
                email=row[1],
                password=row[2],
                role=row[3],
                balance=row[4]
            )

            print(f"Login berhasil! Selamat datang {user.username}")
            return user
        else:
            print("Username atau password salah!")
            return None
        
user_services = UserService()