from unittest import TestCase, main
from Master import _sum, _max, _min, _mult
testList = [1, -1, 2, 3, 4, 5, 6, -7, -7, 23, 3552]
stressList = [1, -1, '2', 3, 4, 5, 6, -7, -7, 23, 3552]


class Tests(TestCase):

    def test_sum(self):
        self.assertEqual(_sum(testList), 3581)

    def test_mult(self):
        self.assertEqual(_mult(testList), -2_882_234_880)

    def test_max(self):
        self.assertEqual(_max(testList), 3552)

    def test_min(self):
        self.assertEqual(_min(testList), -7)

    def test_minstress(self):
        self.assertEqual(_min(stressList), 'Неправильный тип данных')

    def test_maxstress(self):
        self.assertEqual(_max(stressList), 'Неправильный тип данных')

    def test_sumstress(self):
        self.assertEqual(_sum(stressList), 'Неправильный тип данных')

    def test_multstress(self):
        self.assertEqual(_mult(stressList), 'Неправильный тип данных')


if __name__ == '__main__':
    main()
