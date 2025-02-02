import pytest

from src.teller import Teller
from src.model_objects import Product, ProductUnit
from src.shopping_cart import ShoppingCart
from tests.fake_catalog import FakeCatalog


@pytest.fixture
def catalog():
    """Fixture to provide a catalog with common products."""
    catalog = FakeCatalog()
    return catalog

@pytest.fixture
def toothbrush(catalog):
    """Fixture to add a toothbrush product to the catalog."""
    product = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(product, 0.99)
    return product

@pytest.fixture
def apples(catalog):
    """Fixture to add apples product to the catalog."""
    product = Product("apples", ProductUnit.KILO)
    catalog.add_product(product, 1.99)
    return product

@pytest.fixture
def teller(catalog):
    """Fixture to provide a Teller instance with the catalog."""
    return Teller(catalog)

@pytest.fixture
def cart():
    """Fixture to provide an empty shopping cart."""
    return ShoppingCart()
