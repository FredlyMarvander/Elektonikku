import mysql.connector as mysql_conn

class Database:
    def __init__(self):
        self.mydb = mysql_conn.connect(
            host="localhost",
            user="root",
            password="",
            database="db_ecommerce"
        )
        self.cursor = self.mydb.cursor()

    # Jalankan query apa pun 
    def execute_sql(self, sql, val=None):
        self.cursor.execute(sql, val)
        self.mydb.commit()
        return self.cursor.rowcount

    # Ambil data (SELECT)
    def fetch_data(self, sql, val=None):
        self.cursor.execute(sql, val)
        result = self.cursor.fetchall()
        return result

    # Tambah data (INSERT)
    def insert_data(self, sql, val=None):
        self.cursor.execute(sql, val)
        self.mydb.commit()
        return self.cursor.rowcount

    # Update data (UPDATE)
    def update_data(self, sql, val=None):
        self.cursor.execute(sql, val)
        self.mydb.commit()
        return self.cursor.rowcount

    # Hapus data (DELETE)
    def delete_data(self, sql, val=None):
        self.cursor.execute(sql, val)
        self.mydb.commit()
        return self.cursor.rowcount


# Objek tunggal untuk dipakai di semua file
db_object = Database()
