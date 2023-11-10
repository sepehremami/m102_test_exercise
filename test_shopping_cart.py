from shopping_cart import ShoppingCart
import unittest
shoppingcart = ShoppingCart(10)
obj_2 = ShoppingCart(50)
obj_2.add_item("pencile", 200)
obj_2.add_item("book", 300)
obj_2.add_item("pen", 400)
obj_2.add_item("notebook", 400)

obj_2.void_last_item()


class my_test(unittest.TestCase):

    def test_mean_item_price(self):
        self.assertEqual(obj_2.mean_item_price(),
                         obj_2.total//obj_2.item_count)

    def test_median_item_price(self):
        self.assertEqual(obj_2.median_item_price(), 350)

    def test_apply_discount(self):
        self.assertEqual(obj_2.apply_discount(), 650)

    def test_void_last_item(self):
        self.assertEqual(obj_2.void_last_item(), 3)


if __name__ == "__main__":
    unittest.main()
