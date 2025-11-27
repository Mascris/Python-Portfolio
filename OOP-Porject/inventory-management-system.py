class Product:
    def __init__(self,name: str,product_id: str,price: float,stock_quantity: int):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.stock_quantity = stock_quantity

    def add_stock(self,amount):
        if 

    def display_product_info(self):
        print(f"id:{self.product_id},name: {self.name},price: {self.price},stock quantity: {self.stock_quantity}")

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self,name,product_id,price,stock_quantity):
        if product_id in self.products:
            print(f"this {product_id} is already!")
            return
        new_product = Product(name,product_id,price,stock_quantity)
        self.products[product_id] = new_product

    def find_product(self,product_id):
        return self.products.get(product_id,None)

    def update_stock(self,product_id,amount_change):
    

    def list_all_products(self):
        if not self.products:
            print("the store is empty!")
            return
        for product in self.products:
            product.display_product_info()

