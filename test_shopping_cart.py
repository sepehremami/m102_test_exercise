from shopping_cart import ShoppingCart
import unittest
# write your tests here

class TestShoppingCart (unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart()
        self.dis_cart = ShoppingCart(20)
        
        
    def test_init(self):
        
        self.assertEqual(self.cart.total, 0)
        self.assertEqual(self.cart.item_count, 0)
        self.assertEqual(self.cart.items, [])
        self.assertEqual(self.cart.emp_discount, None)
        
        
    def test_add_item(self):
        
        self.cart.add_item("laptop", 1000, 2)
        
        self.assertEqual(self.cart.get_item_count(), 2)
        self.assertEqual(self.cart.get_total(), 2000)


    def test_remove_item(self):
        
        self.cart.add_item("laptop",1000, 2)
        self.cart.add_item("phone", 500, 4)
        
        removed_items = self.cart.remove_item("laptop")
        self.assertEqual(removed_items, [("laptop", 1000)])
        
        self.assertEqual(self.cart.get_item_count(), 5)
        self.assertEqual(self.cart.get_total(), 3000)
        
        self.cart.items = []
        removed_items = self.cart.remove_item("laptop")
        self.assertEqual(removed_items, [])
            
        
    def test_mean_item_price(self):
        
        self.cart.add_item("laptop",1000, 10)
        self.cart.add_item("phone", 500, 10)
        
        self.assertEqual(self.cart.mean_item_price(), 750)
    
    def test_median_item_price(self):
        
        self.cart.add_item("laptop",1000, 5)
        self.cart.add_item("phone", 500, 4)
        self.cart.add_item("watch", 200, 10)
        
        self.assertEqual(self.cart.median_item_price(), 200)


    def test_apply_discount(self):
        
        
        self.dis_cart.add_item("laptop",1000, 5)
        self.dis_cart.add_item("phone", 500, 4)
        self.dis_cart.add_item("watch", 200, 10)
        
        self.dis_cart.apply_discount()
        self.assertEquals(self.dis_cart.total, 7200)
        

    def test_void_last_item(self):
        
        self.cart.add_item("laptop",1000, 5)
        self.cart.add_item("phone", 500, 4)
        self.cart.add_item("watch", 200, 10)
        
        self.cart.void_last_item()
        
        self.assertEqual(self.cart.total, 8800)
        self.assertEqual(self.cart.item_count, 18)
    
    
if __name__ == '__main__':
    unittest.main()
    
    
