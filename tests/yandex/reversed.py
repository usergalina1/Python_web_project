import unittest


class TestReversed(unittest.TestCase):
    def test_reversed1(self):
        for i in reversed(range(1, 13)):
            print(i, 'бомм!')
        print('C новым годом!')

    def test_reversed2(self):
        # Можно обратить вспять обычный список:
        seasons = ['зима', 'весна', 'лето', 'осень']
        for season in reversed(seasons):
            # Переменную цикла, в которую
            # будут передаваться элементы "перевёрнутого" списка seasons,
            # назовём season
            print(season)

    def test_reversed3(self):
        months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                  'Ноябрь', 'Декабрь']
        for month in reversed(months):
            print(month)

    def test_reversed4(self):
        bunny_counter = ''  # Создали переменную bunny_counter, её значение - пустая строка.
        for i in range(1, 6):
            # На каждой итерации цикла
            # к переменной bunny_counter будет дописываться
            # очередная цифра, запятая и пробел (чтобы числа в строке не слиплись).
            # Получившееся значение будет присвоено той же переменной bunny_counter
            bunny_counter = bunny_counter + str(i) + ', '
        print(bunny_counter + 'вышел зайчик погулять!')

    def test_reversed5(self):
        countdown_str = ''
        for i in reversed(range(0, 11)):
            countdown_str = countdown_str + str(i) + ','
        countdown_str = countdown_str + "поехали!"
        print(countdown_str)


if __name__ == '__main__':
    unittest.main()
