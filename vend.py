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
        cur_stock = self.inventory.get(item, None)

        if not cur_stock:
            raise Exception(f"没有找到以下商品: '{item}'")

        if cur_stock < quality:
            raise Exception(f"商品 '{item}' 库存不足, 仅剩 {cur_stock} 件")

        self.inventory[item] = cur_stock - quality
        # TODO: 调用出货功能
        return None

    def view_inventory(self):
        """返回当前库存"""
        return self.inventory
