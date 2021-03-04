import random
import string
import Logger.Logger as L

def generate_random_number(start, end):
    number = random.randint(start, end)
    return number


def generator(size):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def assert_test(condition, fail_str, success_str = "********************** Completed successfully **********************"):
    assert condition, L.logging.error(fail_str)
    L.logging.info(success_str)
