import logging

timeout = 3

log = logging.getLogger()


def plus_one(a):
    return a + 1


def test_when_input_is_3_result_should_be_4():
    log.debug("debug message")
    log.info("info message")
    assert plus_one(3) == 4


def test_change_global_vairable():
    global timeout
    timeout = 5
    log.info(timeout)


def test_echo_global_timeout():
    log.info(timeout)
