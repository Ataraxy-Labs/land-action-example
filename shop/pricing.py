TAX_RATES = {"CA": 0.0725, "NY": 0.05, "TX": 0.0625}


def subtotal(items):
    return sum(price * qty for price, qty in items)


def tax_for(amount, region):
    return round(amount * TAX_RATES[region], 2)


def total(items, region):
    s = subtotal(items)
    return round(s + tax_for(s, region), 2)
