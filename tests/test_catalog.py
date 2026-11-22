from shop.catalog import price_of


def test_price_of():
    assert price_of("cake") == 4.25
