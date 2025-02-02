import pytest

from src.model_objects import SpecialOfferType
from approvaltests.approvals import verify
from src.receipt_printer import ReceiptPrinter


def test_ten_percent_discount(toothbrush, apples, teller, cart):
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

    cart.add_item_quantity(apples, 2.5)

    receipt = teller.checks_out_articles_from(cart)

    assert 4.975 == pytest.approx(receipt.total_price(), 0.01)
    assert [] == receipt.discounts
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert apples == receipt_item.product
    assert 1.99 == receipt_item.price
    assert 2.5 * 1.99 == pytest.approx(receipt_item.total_price, 0.01)
    assert 2.5 == receipt_item.quantity

def test_three_for_two(toothbrush, apples, teller, cart):
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 0.0)

    cart.add_item_quantity(toothbrush, 3)
    cart.add_item_quantity(apples, 2.5)

    receipt = teller.checks_out_articles_from(cart)
    
    verify(ReceiptPrinter().print_receipt(receipt))

def test_five_for_two(toothbrush, teller, cart):
    teller.add_special_offer(SpecialOfferType.FIVE_FOR_AMOUNT, toothbrush, 4)

    cart.add_item_quantity(toothbrush, 5)

    receipt = teller.checks_out_articles_from(cart)
    
    verify(ReceiptPrinter().print_receipt(receipt))
