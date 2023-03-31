from shopping import ShoppingCart
from pytest import raises,fixture

@fixture
def cart() -> ShoppingCart:
    return ShoppingCart("My_cart",3)


def test_add_item(cart) -> None:
    cart.add("Apple", 2)
    assert cart.get_items() == ["Apple"]

def test_create_item(cart) -> None:
    assert cart.name == "My_cart"

def test_check_max_size(cart) -> None:
    with raises(ValueError):
        for i in range(4):
            cart.add(f"item_{i}",i)
