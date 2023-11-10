from shopping_cart import ShoppingCart
import pytest
@pytest.fixture
def shopng_cart():
    test_total=ShoppingCart(emp_discount=50)
    return test_total
# @pytest.mark.parametrize("name","price","quantity",[("ps5",25,2),("ps4", 30, 2)])
# def test_add_item2(shopng_cart,name,price, quantity):
#     shopng_cart.add_item(name,price,quantity=quantity)
#     assert shopng_cart.item_count == 3
def test_add_item(shopng_cart):
    shopng_cart.add_item("ps5",25,quantity=2)
    assert shopng_cart.total==50

def test_add_item2(shopng_cart):
    shopng_cart.add_item("ps5", 25, quantity=2)
    assert shopng_cart.item_count == 2

def test_remove_item(shopng_cart):
    shopng_cart.add_item("ps5", 25, quantity=2)
    shopng_cart.add_item("ps4", 30, quantity=2)
    shopng_cart.remove_item("ps5")
    assert shopng_cart.total == 60

def test_mean_time(shopng_cart):
    shopng_cart.add_item("ps5", 25, quantity=2)
    shopng_cart.add_item("ps6", 100, quantity=1)
    shopng_cart.add_item("ps4", 50, quantity=1)
    assert shopng_cart.mean_item_price() == 50
def test_median_item_price(shopng_cart):
    shopng_cart.add_item("ps5", 25, quantity=2)
    shopng_cart.add_item("ps6", 100, quantity=1)
    shopng_cart.add_item("ps4", 50, quantity=2)
    assert shopng_cart.median_item_price() == 50

def test_apply_dis(shopng_cart):
    shopng_cart.add_item("ps5", 25, quantity=2)
    shopng_cart.add_item("ps4", 50, quantity=2)
    shopng_cart.apply_discount()
    assert shopng_cart.total == 75

def test_void_last_item(shopng_cart):
    shopng_cart.add_item("ps5", 25, quantity=2)
    shopng_cart.add_item("ps4", 50, quantity=2)
    shopng_cart.void_last_item()
    assert shopng_cart.total == 100

def test_item_count(shopng_cart):
    shopng_cart.add_item("ps5", 25, quantity=2)
    shopng_cart.add_item("ps4", 50, quantity=2)
    shopng_cart.void_last_item()
    result = shopng_cart.get_item_count()
    assert result == 3

def test_get_total(shopng_cart):
    shopng_cart.add_item("ps5", 25, quantity=2)
    shopng_cart.add_item("ps4", 50, quantity=2)
    result = shopng_cart.get_total()
    assert result == 150


def test_empty_cart(shopng_cart):
    shopng_cart.add_item("ps5", 25, quantity=1)
    shopng_cart.add_item("ps4", 50, quantity=2)
    shopng_cart.empty_cart()
    assert shopng_cart.total == 0
