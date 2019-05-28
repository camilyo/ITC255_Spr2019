class OrderItem():
    def __init__(self, menuitem, itemquantity, itemprice):
        self.menuitem=menuitem 
        self.itemquantity=itemquantity
        self.itemprice=itemprice

    def getItemNumber(self):
        return self.menuitem

    def getItemName(self):
        return self.itemquantity

    def getItemPrice(self):
        return self.itemprice

    def __str__(self):
        return self.menuitem
    