import unittest


class TestCycle(unittest.TestCase):
    def test_of_list(self):
        bremen_musicians = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух']
        print(bremen_musicians[0])
        print(bremen_musicians[1])
        for musician in bremen_musicians:
            print(musician)
        print('Нам дворцов заманчивые своды не заменят никогда свободы!')

    def test_months(self):
        months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                  'Ноябрь', 'Декабрь']
        for month in months:
            print(month)

    def test_invitation(self):
        pigs = ['Ниф-Ниф', 'Наф-Наф', 'Нуф-Нуф']
        print('Дорогие свиньи!')
        for pig in pigs:
            print(pig)
        print('приглашаю вас на ужин!')
        print('Любящий вас Волк.')


if __name__ == '__main__':
    unittest.main()
