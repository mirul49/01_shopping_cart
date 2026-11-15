import pytest

from cart_delivery import qualifies_free_delivery
from cart_total import calculate_total


@pytest.mark.parametrize(
    ("unit_price_cents", "quantity", "expected"),
    [
        (250, 3, 750),
        (0, 3, 0),
        (250, 0, 0),
        (0, 0, 0),
    ],
)
def test_calculate_total_valid_inputs(unit_price_cents, quantity, expected):
    assert calculate_total(unit_price_cents, quantity) == expected


@pytest.mark.parametrize(
    ("unit_price_cents", "quantity"),
    [
        (True, 1),
        (100, False),
        (1.5, 1),
        (100, "2"),
    ],
)
def test_calculate_total_rejects_non_integer_inputs(unit_price_cents, quantity):
    with pytest.raises(TypeError):
        calculate_total(unit_price_cents, quantity)


@pytest.mark.parametrize(("unit_price_cents", "quantity"), [(-1, 1), (100, -1)])
def test_calculate_total_rejects_negative_inputs(unit_price_cents, quantity):
    with pytest.raises(ValueError):
        calculate_total(unit_price_cents, quantity)


@pytest.mark.parametrize(
    ("total_cents", "expected"),
    [
        (0, False),
        (4999, False),
        (5000, True),
        (5001, True),
    ],
)
def test_qualifies_free_delivery_threshold(total_cents, expected):
    assert qualifies_free_delivery(total_cents) is expected


@pytest.mark.parametrize("total_cents", [True, 50.0, "5000"])
def test_qualifies_free_delivery_rejects_non_integer_inputs(total_cents):
    with pytest.raises(TypeError):
        qualifies_free_delivery(total_cents)


def test_qualifies_free_delivery_rejects_negative_total():
    with pytest.raises(ValueError):
        qualifies_free_delivery(-1)
