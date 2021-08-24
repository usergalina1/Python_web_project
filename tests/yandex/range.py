import unittest


class TestRange(unittest.TestCase):
    def test_range(self):
        around_zero = range(-3, 3)
        # Вместо списка в цикл передаётся переменная around_zero,
        # в ней хранится range() от -3 до 3
        for i in around_zero:
            # Перебрать все числа в диапазоне от -3 до 3 и напечатать их:
            print(i)
        # Будет напечатано
        # -3
        # -2
        # -1
        # 0
        # 1
        # 2

    def test_range1(self):
        for i in range(1, 5):
            print("Вагон №" + str(i))

    def test_range2(self):
        for i in range(1,4):
            print('Я расправлюсь с задачей', i)
        print('Я всех победю!')

    def test_range3(self):
        print('Это первый этаж.')
        # Первый этаж построен, начинайте строить со второго
        for i in range(2, 11):
            # Здесь вместо многоточий
            # вставьте номер текущего этажа,
            # вычислите и вставьте номер предыдущего этажа.
            print('А это', i, 'этаж, он на один выше, чем этаж', i-1)


if __name__ == '__main__':
    unittest.main()
