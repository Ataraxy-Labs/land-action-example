from shop.pricing import subtotal, tax_for, total


def test_subtotal():
    assert subtotal([(10, 2), (5, 1)]) == 25


def test_tax():
    assert tax_for(100, "NY") == 4.0


def test_total():
    assert total([(10, 2)], "CA") == 21.45
