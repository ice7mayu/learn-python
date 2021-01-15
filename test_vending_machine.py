from vend import VendingMachine


def test_in_stock():
    pass


def test_buy_item():
    pass


def test_view_inventory():
    vd = VendingMachine()
    vd.stock('农夫山泉', 10)
    print(vd.view_inventory())
