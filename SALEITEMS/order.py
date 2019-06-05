from item import MenuItem
from orderitem import OrderItem
from payment import Payment

class Order():
    def __init__(self):
        self.orderitems=[]

    def addOrderItems(self, orderitem):
        self.orderitems.append(orderitem)

    def getOrderItems(self):
        return self.orderitems

    def calcTotal(self):
        total=0.0
        for n in self.orderitems:
            total+= n.itemprice * n.itemquantity
        payment=Payment(total)
        return payment
