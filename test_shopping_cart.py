from shopping_cart import ShoppingCart
import unittest

obj1 = ShoppingCart(50)
obj1.add_item("ff", 100)
obj1.add_item("jj", 300)
obj1.median_item_price()


# write your tests here

class MyTestCase(unittest.TestCase):
    def test_mean_item(self):
        self.assertEqual(obj1.mean_item_price(), obj1.total / obj1.item_count)

    def test_median_item(self):
        self.assertEqual(obj1.median_item_price(), 200)

    def test_void_last_item(self):
        self.assertEqual(obj1.void_last_item(), 100)

    def test_apply_discount(self):
        self.assertEqual(obj1.apply_discount(), 200)


if __name__ == "__main__":
    unittest.main()
