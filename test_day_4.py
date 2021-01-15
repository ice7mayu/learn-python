"""
Day 4 大纲
module & package
__init__.py

from ... import ...
class
self, cls
function vs method
@property, @staticmethod
isinstance
issubclass
"""
import logging

from mylib import *

log = logging.getLogger()


def test_import_built_in_module():
    import os
    import sys
    log.info(os.name)
    log.info(sys.getwindowsversion())
    log.info(sys.path)


def test_import_self_defined_module():
    import mylib
    msg = mylib.welcome('sam')
    log.info(msg)


def test_import_star():
    from mylib import welcome
    welcome('')
    goodbye('')


def test_import_item_from_module():
    from mylib import welcome
    msg = welcome('anna')
    log.info(msg)


def test_import_from_package_directly():
    from mypkg import say_hi

    log.info(say_hi())


def test_import_function_from_package():
    from mypkg.greeting import say_goodbye
    log.info(say_goodbye())


def test_import_module_from_package():
    from mypkg import greeting
    greeting.say_goodbye()


def test_pay():
    from pay import deposit
    from pay import with_draw


def test_define_a_class():
    class Card:
        def __init__(self, card_no='n/a'):
            # 定一个实例的字段
            self.card_no = card_no

    card1 = Card()
    card2 = Card(card_no="002")

    # log.info(f"{card1.card_no=}")
    # log.info(f"{card2.card_no=}")

    # 实例支持动态字段(field)
    card1.user_name = 'john'
    # log.info(f"{card1.user_name=}")
    # log.info(f"{card2.user_name=}") # 在访问属性时必须提前预定义字段(field)
    #
    # card1_has_user_name = hasattr(card1, 'user_name')
    # card2_has_user_name = hasattr(card2, 'user_name')
    # log.info(f"{card1_has_user_name=}")
    # log.info(f"{card2_has_user_name=}")

    cards = [card1, card2]
    for c in cards:
        if hasattr(c, 'user_name'):
            print(c.user_name)


def test_the_self_and_cls_keywords():
    class Person:
        def __init__(self, name):
            self.name = name

        def play(self, game):
            log.info(f"{self.name} is playing {game}")

        @classmethod
        def echo_type(cls):
            log.info(f"My type is {cls}")

    p1 = Person('p1')
    p2 = Person('p2')

    # p1.play('need for speed')
    # p2.play('formula one')
    # Person.play(p1, 'need for speed')
    # Person.play(p2, 'formula one')
    #
    p1.echo_type()
    p2.echo_type()
    Person.echo_type()


def test_instance_field_vs_class_field():
    class Person:
        count = 0

        def __init__(self, name):
            self.name = name
            Person.count += 1

        @classmethod
        def echo_count(cls):
            log.info(f"{Person.count=}")

    Person.echo_count()
    p1 = Person('p1')
    p2 = Person('p2')
    # Person.echo_count()
    # log.info(Person.count)

    log.info(f"{p1.count=}")
    p1.count = 100
    log.info(f"after {p1.count=}")
    Person.count = 500
    log.info(f"{p2.count=}")
    Person.count = 600
    log.info(f"{p2.count=}")


def test_static_method():
    class Person:
        def __init__(self, name):
            self.name = name

        @staticmethod
        def usage():
            log.info('帮助文档')

    Person.usage()
    Person('').usage()


def test_inheritance():
    class Calculation1:
        def echo(self):
            print(self)
            log.info('in Calculation1')

        def summation(self, a, b):
            log.info(self)
            return a + b

    class Calculation2:
        def multiplication(self, a, b):
            log.info(self)
            return a * b

    class Derived(Calculation1, Calculation2):
        def divide(self, a, b):
            log.info(self)
            return a / b

        def echo(self):
            print(self)
            log.info('in Derived')

    d = Derived()
    print(isinstance(d, Derived))
    print(isinstance(d, Calculation2))

    d.echo()


def test_str_():
    class Person:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f'My name is {self.name}'

    p = Person('person1')
    log.info(p.name)
    log.info(p)
    print(p)


