"""
商品数据

{
    "item1": 10,
    "item2": 20,
    "item3": 30,
}

"""


class VendingMachine:
    def __init__(self):
        self.inventory = {}

    def stock(self, item, quality):
        """补充库存, 商品上架"""
        self.inventory[item] = quality

    def buy(self, item, quality):
        """售货"""
        pass

    def view_inventory(self):
        """查看当前库存"""
        return self.inventory
