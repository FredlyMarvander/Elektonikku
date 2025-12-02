from database import db_object

class CartDetailService:
    def checkProductInCart(self, cartId, name):
        query = """
        SELECT id FROM CartDetails
        WHERE cartId = %s AND name = %s
        """

        val = (cartId, name)
        result = db_object.fetch_data(query, val)
        
        if result:
            return True  
        
        return False
    
    def increaseQuantity(self, cartId, name):
        query = """
        UPDATE CartDetails
        SET quantity = quantity + 1
        WHERE cartId = %s AND name = %s
        """

        val = (cartId, name)

        result = db_object.update_data(query, val)

        return result
    
    def decreaseQuantity(self, cartId, name):
        query = """
        UPDATE CartDetails
        SET quantity = CASE 
            WHEN quantity > 1 THEN quantity - 1 
            ELSE 1 
        END
        WHERE cartId = %s AND name = %s
        """

        val = (cartId, name)

        result = db_object.update_data(query, val)

        return result
    
    def removeItemFromCart(self, cartId, name):
        query = """
        DELETE FROM CartDetails
        WHERE cartId = %s AND name = %s
        """

        val = (cartId, name)

        result = db_object.delete_data(query, val)

        return result
    
    def fetchCartDetailsByCartId(self, cartId):
        query = """
        SELECT * FROM CartDetails
        WHERE cartId = %s
        """
        val = (cartId,)
        result = db_object.fetch_data(query, val)
        return result
    
    
cart_detail_service = CartDetailService()