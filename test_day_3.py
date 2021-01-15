"""
Day 3

https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
doc string

error first
function实例方法
lambda 表达式
map
reduce
filter
"""
import logging

log = logging.getLogger()


def doc_str_demo(a, b):
    """Google 样式文档注释示例

    Args:
        a(str): 第一个参数
        b(int): 第二个参数

    Returns:
        bool: 返回结果为一个布尔值

    """
    pass


def test_return_as_a_tuple():
    """函数只能有一个返回值
    如果需要返回多个值的话, 返回成一个元组"""

    def get_base_url():
        """获取 base_url, 并返回 ip 和 端口

        Returns:
            IP and port as a tuple
        """
        return "127.0.0.1", 8080

    base_url = get_base_url()
    log.info(f"{base_url=}, type of base_url is {type(base_url)}")


def test_error_first():
    """定义方法时, 先校验必要条件, 不符合条件优先退出该方法"""

    def minus(a, b):
        if a < b:
            log.warning("建议a大于b")
            return None
        return a - b

    result1 = minus(2, 1)
    result2 = minus(1, 2)

    log.debug(f"{result1=}")
    log.debug(f"{result2=}")


def test_function_instance():
    """方法实例
    方法本身也是一个实例, 可以访问方法的一些常用属性
    """

    def dummy_function(a, b=1, c=2):
        """这是一个示例方法, 参数列表包含位置参数和关键字参数

        Args:
            a(str): 第1个参数
            b(int): 第2个参数
            c(int): 第3个参数

        Returns:
            tuple: 以元组形式返回输入的参数列表
        """
        return a, b, c

    log.info(dummy_function.__name__)
    log.info(dummy_function.__doc__)


def test_lambda_expression():
    """lambda 表达式用来定义一个函数, 省略def, return 等关键字"""

    # 虽然可以这样使用, 但是不符合 PEP8 编码规范

    add = lambda x, y: x + y

    result = add(1, 2)
    log.info(f"{result=}")


def test_lambda():
    """lambda 表达式用于定义方法体简单的匿名方法, 从而使代码更简洁
    一般在方法需要被当做参数时使用
    """

    def qualified(score):
        if score >= 60:
            return True
        else:
            return False

    def print_leaderboards(qa, *scores):
        for score in scores:
            good_enough = qa(score)
            log.debug(f"{score=}, {'good' if good_enough else 'not good'}")

    print_leaderboards(qualified, 50, 60, 70, 80, 90, 100)

    log.info("\nlambda demo\n")
    print_leaderboards(lambda score: score >= 90, 70, 80, 90, 100)


def test_map():
    """map 用于将集合里的元素按照统一的方法进行变换从而得到一个全新的集合"""

    scores = (60, 70, 80, 90)

    def plus_10(score):
        return score + 10

    final_scores = map(plus_10, scores)

    log.info(f"{scores=}")
    log.info(f"{tuple(final_scores)=}")
    log.info(f"{scores=}")  # map不会修改原始数据

    # 使用 lambda 表达式
    double_scores = (map(lambda x: x * 2, scores))
    for score in double_scores:
        log.info(score)


def test_filter():
    """filter 函数用于从集合中过滤筛选符合条件的元素"""

    numbers = [x for x in range(10)]

    odds = tuple(filter(lambda x: x % 2 != 0, numbers))
    log.info(f"{numbers=}")
    log.info(f"{odds=}")


def test_reduce():
    """reduce 先计算集合里的前2个元素的结果, 然后将结果跟第3个元素计算, 以此类推等到一个最终的结果"""
    from functools import reduce

    # 实现 1~100 求和
    sum_100 = reduce(lambda x, y: x + y, range(1, 101))
    log.info(f"{sum_100=}")
    log.info(f"{sum(range(101))=}")  # 注意取值范围, 起始值从 0 开始


def test_exception_handling():
    def check_phone_number(phone_number: str) -> int:
        prefix = phone_number[:3]
        valid_prefix = ('158', '159')
        db_log = ''

        log.debug(f"{prefix=}")
        try:
            if prefix in valid_prefix:
                db_log = f"{phone_number} 是有效号段"
                return 200
            else:
                raise Exception("无效的号码段")
        except Exception as ex:
            log.warning(ex)
            db_log = str(ex)
            return 400
        finally:
            log.info(f"写入log: {db_log}")

    code1 = check_phone_number("15812345678")
    code2 = check_phone_number("18812345678")

    log.info(f"{code1=}")
    log.info(f"{code2=}")


# region 作业

def test_symmetrical_string():
    """判断对称字符"""

    # abc => False
    # aba => True
    # 1221 => True

    def symmetrical1(s):
        """方案1: 翻转字符串"""
        reversed_str = "".join(reversed(s))
        return s == reversed_str

    def symmetrical2(s):
        """方案2: 判断收尾字符"""
        if len(s) == 1:
            return True

        start = 0
        end = -1
        stop = len(s) // 2

        for i in range(stop):
            head = start + i
            tail = end - i
            if s[head] != s[tail]:
                return False
        return True

    def check(symmetrical_func, *data):
        for s in data:
            log.info(f"{s=}, 是否对称: {symmetrical_func(s)}")

    # 准备测试数据
    test_cases = ("a", "abc", "aba", "1221")

    check(symmetrical1, *test_cases)
    log.info(f"{'-' * 20}split{'-' * 20}")
    check(symmetrical2, *test_cases)


def test_example_filter_failed_students():
    """
    lambda arg1, arg2...: return_value

    过滤分数, 使用map, reduce, filter"""

    student_scores = [
        {"name": "name1", "score": 40},
        {"name": "name2", "score": 45},
        {"name": "name3", "score": 50},
        {"name": "name4", "score": 60},
        {"name": "name5", "score": 70},
    ]

    # 问题1: 统计平均成绩 avg
    # 问题2: 给所有学生统一加 bonus=10 分
    # 问题3: 筛选出增加了10分后, 仍然不及格的(低于60分)学生信息

    # region answer
    # 统计平均分
    from functools import reduce

    scores = map(lambda x: x["score"], student_scores)
    total = reduce(lambda x, y: x + y, scores)

    avg = total / len(student_scores)
    log.info(f"平均成绩为: {avg}")

    # 将每个学生的成绩统一加 10 分
    bonus = 10

    boosted_scores = list(
        map(lambda x: x.update(score=x["score"] + bonus) or x, student_scores)
    )
    log.info(f"统一提升10分后的成绩: {boosted_scores}")

    # 列出不及格的(分数小于60分)学生信息

    failed_student_scores = list(
        filter(lambda x: x["score"] < 60, boosted_scores)
    )

    log.info(f"未及格的学生成绩: {failed_student_scores}")
    # endregion

# endregion
