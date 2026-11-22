from shop.receipt import line


def test_line():
    assert line("tea", 3.5) == "tea: $3.50"
