def _sum(lst):
    summ = 0
    try:
        for i in lst:
            summ += i
        return summ
    except TypeError:
        return 'Неправильный тип данных'


def _mult(lst):
    mult = 1
    for i in lst:
        if isinstance(i, str):
            return 'Неправильный тип данных'
        else:
            mult *= i
    return mult


def _max(lst):
    maxx = lst[0]
    try:
        for i in lst:
            if i > maxx:
                maxx = i
        return maxx
    except TypeError:
        return 'Неправильный тип данных'


def _min(lst):
    minn = 0
    try:
        for i in lst:
            if i < minn:
                minn = i
        return minn
    except TypeError:
        return 'Неправильный тип данных'


def read_file(filename):
    f = open(f'{filename}', encoding='utf-8')
    file = list(map(int, f.read().split(' ')))
    f.close()
    return file


def Master():
    pass


if __name__ == '__main__':
    Master()
