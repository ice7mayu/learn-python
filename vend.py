"""
商品数据

{
    "item1": 10,
    "item2": 20,
    "item3": 30,
}

"""
import logging

log = logging.getLogger()


class VendingMachine:
    def __init__(self):
        self._version = ''
        self.inventory = {}
        self.hardware = Hardware()

    @property
    def version(self):
        return f"v{self._version}"

    @version.setter
    def version(self, value):
        self._version = value

    def stock(self, item, quality):
        """补充库存, 商品上架

        Args:
            item(str): 商品名称
            quality(int): 商品数量
        """
        self.inventory[item] = quality

    def buy(self, item, quality):
        """售货"""
        cur_stock = self.inventory.get(item, None)

        if not cur_stock:
            raise Exception(f"没有找到以下商品: '{item}'")

        if cur_stock < quality:
            raise Exception(f"商品 '{item}' 库存不足, 仅剩 {cur_stock} 件")

        self.inventory[item] = cur_stock - quality
        self.hardware.push_item(item)
        return None

    def view_inventory(self):
        """返回当前库存"""
        return self.inventory


class Hardware:
    def __init__(self):
        pass

    @staticmethod
    def push_item(item):
        log.info(f'推出商品{item}')
