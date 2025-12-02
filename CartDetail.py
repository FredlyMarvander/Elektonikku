from database import db_object

class CartDetail:
    def __init__(self, quantity, name, price, cartId, image_url):
        self.quantity = quantity       
        self.name = name
        self.price = price
        self.cartId = cartId
        self.image_url = image_url

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
        INSERT INTO CartDetails (quantity, name, price, cartId, image)
        VALUES (%s, %s, %s, %s, %s)
        """
        val = (self.quantity, self.name, self.price, self.cartId, self.image_url)
        result = db_object.insert_data(query, val)
        return result

   
    def deleteCartDetail(self, name):
        query = """
        DELETE FROM CartDetails
        WHERE name = %s AND cartId = %s
        """
        val = (name, self.cartId)
        result = db_object.delete_data(query, val)
        return result

