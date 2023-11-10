from shopping_cart import ShoppingCart
import unittest


shoppingcart=ShoppingCart(12)
obj_1=ShoppingCart(50)
obj_2=ShoppingCart(50)
shoppingcart.add_item("notebook",150)
obj_1.add_item("pen",100)
obj_1.add_item("book",200)
obj_1.add_item("notebook",400)
obj_1.add_item("milk",400)

obj_1.mean_item_price()
obj_1.apply_discount

# write your tests here
class my_test(unittest.TestCase):

    def test_mean_item_price(self):
        self.assertEqual(obj_1.mean_item_price(),obj_1.total/obj_1.item_count)
    

    def test_median_item_price(self):
        self.assertEqual(obj_1.median_item_price(),300)

    def test_apply_discount(self):
        self.assertEqual(obj_1.apply_discount(),550)
    
    def test_void_last_item(self):
        self.assertEqual(obj_1.void_last_item(),300)
        


if __name__=='__main__':
    unittest.main()
