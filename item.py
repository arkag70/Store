
class Item:

    def __init__(self,_id,_product,_brand,_price):
        
        self.ID = _id
        self.product = _product
        self.brand = _brand
        self.price = _price

    def showItems(self):
        
        print(f"{self.ID}\t{self.product}\t{self.brand}\t{self.price}")

