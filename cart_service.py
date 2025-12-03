from database import db_object

class CartService:
    def getCartByUserId(self, userId):
        query = """
            SELECT ID
            FROM Carts
            WHERE userId = %s
            ORDER BY ID DESC
            LIMIT 1
        """
        val = (userId,)
        result = db_object.fetch_data(query, val)
        
        if result:
            return result[0]
        
        return None
    
    def getCartWithTransactionDate(self):
        query = """
            SELECT *
            From Carts
            WHERE transactionDate IS NOT NULL
        """

        result = db_object.fetch_data(query)

        if result:
            return result
        
        return None

    
    def checkCartActive(self, userId, sellerId):
        query = """
            SELECT id FROM Carts
            WHERE userId = %s
            AND sellerId = %s
            AND transactionDate IS NULL;
        """
        val = (userId, sellerId)
        result = db_object.fetch_data(query, val)
        
        if result:
            return True  
        
        return False
    
    def createCart(self, userId, sellerId):
        query = """
            INSERT INTO Carts (userId, sellerId)
            VALUES (%s, %s)
        """
        val = (userId, sellerId)
        result = db_object.insert_data(query, val)
        return result
    
    def getCartByUserAndSeller(self, userId, sellerId):
        query = """
            SELECT ID
            FROM Carts
            WHERE userId = %s
            AND sellerId = %s
            ORDER BY ID DESC
            LIMIT 1
        """
        val = (userId, sellerId)
        result = db_object.fetch_data(query, val)
        
        if result:
            return result[0] 
        
        return None
    
    def checkoutCart(self, userId, cartId, total):
        query  = """
        UPDATE Carts
        SET transactionDate = NOW()
        WHERE id = %s AND userId = %s
        """

        val = (cartId, userId)

        result = db_object.update_data(query, val)

        if result:
            return result
        
        return None

    def getCartById(self, cartId):
        query = """
        SELECT transactionDate
        FROM Carts
        WHERE ID = %s
        """

        val = (cartId,)

        result = db_object.fetch_data(query, val)

        if result:
            return result
        
        return None
    
    def getAllCartsByUserId(self, userId):
        query = """
        SELECT * FROM Carts
        WHERE userId = %s AND transactionDate IS NOT NULL
        ORDER BY transactionDate DESC
        """

        val = (userId,)

        result = db_object.fetch_data(query, val)

        return result
    

    def getCartAndCartDetails(self, admin_id):
        query = """
        SELECT DATE(Carts.transactionDate) AS transactionDate, SUM(CartDetails.price) AS totalPrice
        FROM Carts
        JOIN CartDetails ON Carts.id = CartDetails.cartId
        WHERE Carts.transactionDate IS NOT NULL AND sellerId = %s
        GROUP BY Carts.transactionDate

        ORDER BY transactionDate DESC
        """

        val = (admin_id,)

        result = db_object.fetch_data(query, val)

        return result

    def getCartAndCartDetailsCustomer(self, user_id):
        query = """
        SELECT Carts.id, Carts.transactionDate AS transactionDate, SUM(CartDetails.price) AS totalPrice, COUNT(CartDetails.id) AS itemCount
        FROM Carts
        JOIN CartDetails ON Carts.id = CartDetails.cartId
        WHERE Carts.transactionDate IS NOT NULL AND userId = %s
        GROUP BY Carts.transactionDate

        ORDER BY Carts.transactionDate DESC
        """

        val = (user_id,)

        result = db_object.fetch_data(query, val)

        return result

cart_services = CartService()