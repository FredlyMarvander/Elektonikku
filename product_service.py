from database import db_object

class ProductService:
    def fetchProducts(self):
        result = db_object.fetch_data(f"SELECT * FROM Products")
        return result
    
    def fetchProductById(self, id):
        query = """
        SELECT * FROM Products WHERE user_id = %s
        """

        value = (id,)

        result = db_object.fetch_data(query, value)

     

        return result
    
    def updateStock(self, productId, newStock):
        query = """
        UPDATE Products
        SET stock = %s
        WHERE id = %s
        """

        val = (newStock, productId)

        result = db_object.update_data(query, val)

        return result
    
    def getProductByName(self, name):
        query = """
        SELECT * FROM Products WHERE name = %s
        """

        val = (name,)

        result = db_object.fetch_data(query, val)

        if result:
            return result[0]
        
        return None
        

product_services = ProductService()