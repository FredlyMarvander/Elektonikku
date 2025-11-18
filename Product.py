from database import db_object

class Product:
    def __init__(self, name, description, price, stock, user_id):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.user_id = user_id

    def readProducts(self):
        result = db_object.fetch_data(f"SELECT * FROM Products")
        return result

    def insertProduct(self):
        query = """
        INSERT INTO Products (name, description, price, stock, user_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        value = (self.name, self.description, self.price, self.stock, self.user_id)
        result = db_object.insert_data(query, value)
        return result

    def updateProduct(self, name):
        query = """
        UPDATE Products
        SET name = %s,
            description = %s,
            price = %s,
            stock = %s
        WHERE name = %s
        """
        value = (self.name, self.description, self.price, self.stock, name)
        result = db_object.update_data(query, value)
        return result
        
    def deleteProduct(self, name):
        query = """
        DELETE FROM Products WHERE name = %s 
        """
        value = [name]
        result = db_object.delete_data(query, value)
        return result

obj_product = Product('Samsung Galaxy A54', 'Smartphone dengan layar Super AMOLED 6.6, RAM 8GB, baterai 5000mAh', 5499000, 20, '1')
# print(obj_product.readProducts())
# print(obj_product.insertProduct())
# print(obj_product.updateProduct("JBL Charge 5"))
print(obj_product.deleteProduct("Samsung Galaxy A54"))