# -*- encoding:UTF-8 -*-

from retrying import retry

# 就算报错, 也会尝试运行三次
@retry(stop_max_attempt_number=3)
def fun1():
    print("this is fun1 running.")
    raise ValueError("fun1 error")


if __name__ == '__main__':
    fun1()

