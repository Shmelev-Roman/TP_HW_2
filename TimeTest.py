from time import perf_counter
from random import randint
from Master import _max, _min, _sum, _mult
lst = [randint(-1000, 1000) for i in range(100_000_000)]


def time_test(lst):
    for i in range(1, 11):
        start = perf_counter()
        # вставьте любую функцию
        _max(lst[:i * 10_000_000])
        finish = perf_counter()
        print(f'{i}0 млн. чисел: ' + str(finish - start) + ' секунд')


if __name__ == '__main__':
    time_test(lst)
