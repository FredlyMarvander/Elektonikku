from database import db_object

class ProductService:
    def fetchProducts(self):
        result = db_object.fetch_data(f"SELECT * FROM Products")
        return result

product_services = ProductService()