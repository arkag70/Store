from item import *

class Customer:

    def __init__(self):

        self.number = ""
        self.name = ""
        self.items = []
        self.amount = 0.0
    
    def getDetails(self):
        
        ans = 'y'
        self.number = input("Enter mobile number: ")
        self.name = input("Enter Name: ")

        while ans == 'y':

            if ans == 'n':
                break
            else:
                _id = input("Enter product ID: ")
                _product = input("Enter product Name: ")
                _brand = input("Enter Brand: ")
                _price = float(input("Enter Price: "))

                self.items.append(Item(_id,_product,_brand,_price))

            ans = input("Do you want to enter purchase details (y/n)? : ")

    def calculateTotal(self):
        
        sum = 0.0
        for i in self.items:
            sum += float(i.price)
        return sum

    def generateBill(self):
        
        self.amount = self.calculateTotal()
        print("\n\nBill\n\nMORE MEGA STORE")
        print(f"Customer : {self.name}")
        print(f"Mobile : {self.number}")
        
        if len(self.items) > 0:
            for i in self.items:
                print(f"{i.ID}\t{i.product}\t{i.brand}\t{i.price}")

        print(f"Total : {self.amount}")

if __name__ == "__main__":
    c = Customer()
    c.getDetails()
    c.generateBill()
