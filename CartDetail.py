from database import db_object

class CartDetail:
    def __init__(self, quantity, name, price, cartId):
        self.quantity = quantity       
        self.name = name
        self.price = price
        self.cartId = cartId

    def fetchCartDetail(self):
        query = """
        SELECT * FROM CartDetails
        WHERE cartId = %s
        """
        val = (self.cartId,)
        result = db_object.fetch_data(query, val)
        return result

    def insertCartDetail(self):
        query = """
        INSERT INTO CartDetails (quantity, name, price, cartId)
        VALUES (%s, %s, %s, %s)
        """
        val = (self.quantity, self.name, self.price, self.cartId)
        result = db_object.insert_data(query, val)
        return result

    def decreaseQuantity(self, name):
        query = """
        UPDATE CartDetails
        SET quantity = quantity - 1
        WHERE name = %s AND cartId = %s AND quantity > 0
        """
        val = (name, self.cartId)
        result = db_object.update_data(query, val)
        return result
    
    def increaseQuantity(self, name):
        query = """
        UPDATE CartDetails
        SET quantity = quantity + 1
        WHERE name = %s AND cartId = %s
        """
        val = (name, self.cartId)
        result = db_object.update_data(query, val)
        return result
    
    def deleteCartDetail(self, name):
        query = """
        DELETE FROM CartDetails
        WHERE name = %s AND cartId = %s
        """
        val = (name, self.cartId)
        result = db_object.delete_data(query, val)
        return result
