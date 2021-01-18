import pytest
import logging
from vend import VendingMachine

log = logging.getLogger()


def data_gen():
    total = 10
    items = (
        ('商品1', total),
        ('商品2', total),
        ('商品3', total),
    )
    return items


def test_in_stock():
    """商品入库"""
    vending_machine = VendingMachine()
    items = data_gen()
    for item in items:
        vending_machine.stock(*item)

    log.info(vending_machine.view_inventory())


def test_view_inventory():
    """入库商品并校验库存"""
    vending_machine = VendingMachine()
    vending_machine.stock('商品1', 10)
    log.info(f"加入商品: (商品1, 10)")

    stock = vending_machine.view_inventory()
    log.info(f"当前库存为: {stock}")
    assert stock == {'商品1': 10}


def test_buy_existing_item():
    """购买商品"""
    # 初始化数据
    vending_machine = VendingMachine()
    items = data_gen()
    for item in items:
        vending_machine.stock(*item)

    item = '商品1'
    total = 10
    qty = 3

    # 调用被测试接口
    vending_machine.buy('商品1', qty)
    left = vending_machine.inventory.get(item)
    log.info(f"当前库存为: {vending_machine.view_inventory()}")

    # 校验数据
    assert left == total - qty


def test_buy_non_existing_item():
    """购买不存在的商品"""
    vending_machine = VendingMachine()
    item = '商品1'
    qty = 10
    vending_machine.stock(item=item, quality=qty)

    # 定义一个不存在的商品
    dummy_item = '商品100'

    # 校验被测试接口是否抛出预期异常类型
    with pytest.raises(Exception) as ex:
        vending_machine.buy(item=dummy_item, quality=1)
    log.info(ex.value)

    # 校验异常信息应包含期望文本
    ex.match(f"没有找到以下商品: '{dummy_item}'")


def test_out_of_stock():
    """商品库存不足时应提示错误信息, 库存不变"""
    vending_machine = VendingMachine()
    item = '商品1'
    qty = 10
    vending_machine.stock(item=item, quality=qty)

    with pytest.raises(Exception) as ex:
        # FIXME: 消除 magic number 11
        vending_machine.buy(item, 11)
    ex.match('库存不足')

    # 校验库存应与初始值一致
    assert vending_machine.inventory.get(item) == qty
