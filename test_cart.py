import pytest
from cart import ShoppingCart


def test_add_item_adds_product_to_cart():
    cart = ShoppingCart()

    cart.add_item("Apple", 10.0, 2)

    assert cart.get_total() == 20.0
    assert cart.get_item_count() == 2


def test_add_item_increases_quantity_when_item_exists():
    cart = ShoppingCart()

    cart.add_item("Apple", 10.0, 2)
    cart.add_item("Apple", 10.0, 3)

    assert cart.get_item_count() == 5
    assert cart.get_total() == 50.0


def test_add_item_with_negative_price_raises_error():
    cart = ShoppingCart()

    with pytest.raises(ValueError):
        cart.add_item("Apple", -5.0, 1)


def test_add_item_with_zero_quantity_raises_error():
    cart = ShoppingCart()

    with pytest.raises(ValueError):
        cart.add_item("Apple", 10.0, 0)


def test_remove_item_removes_product_from_cart():
    cart = ShoppingCart()

    cart.add_item("Apple", 10.0, 2)
    cart.remove_item("Apple")

    assert cart.get_item_count() == 0
    assert cart.get_total() == 0.0


def test_remove_item_that_does_not_exist_raises_error():
    cart = ShoppingCart()

    with pytest.raises(KeyError):
        cart.remove_item("Apple")


def test_apply_percent_discount_save10():
    cart = ShoppingCart()

    cart.add_item("Book", 100.0, 1)
    cart.apply_discount("SAVE10")

    assert cart.get_total() == 90.0


def test_apply_percent_discount_save20():
    cart = ShoppingCart()

    cart.add_item("Book", 100.0, 1)
    cart.apply_discount("SAVE20")

    assert cart.get_total() == 80.0


def test_apply_fixed_discount_flat5():
    cart = ShoppingCart()

    cart.add_item("Book", 40.0, 1)
    cart.apply_discount("FLAT5")

    assert cart.get_total() == 35.0


def test_invalid_discount_code_raises_error():
    cart = ShoppingCart()

    cart.add_item("Book", 40.0, 1)

    with pytest.raises(ValueError):
        cart.apply_discount("INVALID")


def test_clear_removes_all_items():
    cart = ShoppingCart()

    cart.add_item("Apple", 10.0, 2)
    cart.add_item("Book", 20.0, 1)
    cart.clear()

    assert cart.get_item_count() == 0
    assert cart.get_total() == 0.0
