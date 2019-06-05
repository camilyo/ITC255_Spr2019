import unittest
from item import MenuItem
from payment import Payment
from orderitem import OrderItem
from order import Order
from user import User


class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item=MenuItem(1, 'burguer', 'not for vegetarians')
        self.item2=MenuItem(2, 'orange juice', 'fresh squeezed')

    def test_itemString(self):
        self.assertEqual(str(self.item),self.item.itemname)
        self.assertEqual(str(self.item2),self.item2.itemname)

    def test_getPrice(self):
        self.assertEqual(str(self.item.getItemDescription()), 'not for vegetarians')
        self.assertEqual(str(self.item2.getItemDescription()), 'fresh squeezed')

    def test_getItemNumber(self):
        self.assertEqual(str(self.item.getItemNumber()),'1')
        self.assertEqual(str(self.item2.getItemNumber()),'2')

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user=User(1, 'Michael', "True")

    def test_UserNumber(self):
        self.assertEqual(str(self.user.getUserNumber()), '1')

    def test_UserName(self):
        self.assertEqual(str(self.user.getUserName()), 'Michael')

    def test_UserPermission(self):
        self.assertEqual(str(self.user.getUserPermission()), "True")

class OrderItemTest(unittest.TestCase):
    def setUp(self):
        self.orderitem1=OrderItem('drink', 2, 2.00)
        self.orderitem2=OrderItem('cheeseburguer', 3, 4.00)

    def test_MenuItem(self):
        self.assertEqual(str(self.orderitem1), 'drink')
        self.assertEqual(str(self.orderitem2), 'cheeseburguer')

    def test_Quantity(self):
        self.assertEqual(str(self.orderitem1.getQuantity()), '2')
        self.assertEqual(str(self.orderitem2.getQuantity()), '3')

    def test_ItemPrice(self):
        self.assertEqual(str(self.orderitem1.getItemPrice()), '2.0')
        self.assertEqual(str(self.orderitem2.getItemPrice()), '4.0')

class OrderTest(unittest.TestCase):

   def setUp(self):
       self.o=Order()
       self.item1=MenuItem(1,'cheeseburguer', 6.00)
       self.item2=MenuItem(2,'french fries', 2.50)
       
       self.orderitem1=OrderItem(1, 2, 6.00)
       self.orderitem2=OrderItem(2, 1, 2.50)
       
       self.o.addOrderItems(self.orderitem1)
       self.o.addOrderItems(self.orderitem2)
       
   def test_addandGetOrderItems(self):
    
       self.oitems=self.o.getOrderItems()
       self.assertEqual(len(self.oitems), 2)

   def test_CalculateTotal(self):
        payment=self.o.calcTotal()
        self.assertEqual(str(payment), 'Your total is 14.5')
