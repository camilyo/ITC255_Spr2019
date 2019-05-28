from orderitem import OrderItem

class MenuItem():
    def __init__(self, itemnum, itemname, itemdescription):
        self.itemnum=itemnum 
        self.itemname=itemname
        self.itemdescription=itemdescription

    def getItemNumber(self):
        return self.itemnum 

    def getItemName(self):
        return self.itemname 

    def getItemPrice(self):
        return self.itemdescription

    def __str__(self):
        return self.itemname 
    