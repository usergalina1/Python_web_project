import unittest


class TestConditions(unittest.TestCase):
    def test_condition1(self):
        for messages_count in range(6):
            if messages_count > 0:
                print('Новых сообщений: ' + str(messages_count))
            else:
                print("У вас нет сообщений")

    def test_condition2(self):
        for current_hour in range(24):
            if current_hour < 12:
                print('Доброе утро!')
            else:
                print("Добрый день!")

    def test_condition3(self):
        for messages_count in range(0, 21):
            if messages_count == 0:
                print('У вас нет новых сообщений')
            elif messages_count == 1:
                print('У вас 1 новое сообщение')
            elif messages_count <= 4:
                print('У вас', messages_count, 'новых сообщения')
            else:
                print('У вас', messages_count, 'новых сообщений')

    def test_condition4(self):
        for current_hour in range(0, 24):
            print("На часах " + str(current_hour) + ":00.")
            if current_hour < 6:
                print("Доброй ночи!")
            elif current_hour < 12:
                print('Доброе утро!')
            elif current_hour < 18:
                print('Добрый день!')
            elif current_hour < 23:
                print('Добрый вечер!')
            else:
                print('Доброй ночи!')

    def test_condition5(self):
        for current_hour in range(0, 24):
            print("На часах " + str(current_hour) + ":00.")
            if current_hour >= 6 and current_hour <= 11:
                print('Доброе утро!')
            elif current_hour >= 12 and current_hour <= 17:
                print('Добрый день!')
            elif current_hour >= 18 and current_hour <= 22:
                print('Добрый вечер!')
            elif current_hour <= 5 or current_hour >= 23:
                print('Доброй ночи!')

    def test_condition6(self):
        for messages_count in range(0, 21):
            if messages_count == 0:
                print('У вас нет новых сообщений')
            elif messages_count == 1:
                print('У вас', messages_count, 'новое сообщение')
            elif messages_count >= 2 and messages_count <= 4:
                print('У вас', messages_count, 'новых сообщения')
            else:
                print('У вас', messages_count, 'новых сообщений')

    def test_condition7(self):
        good_boy = True  # мальчик-то неплохой
        if not good_boy:
            print('Этот в грязь полез')
            print('и рад,')
            print('что грязна рубаха.')
            print('Про такого говорят:')
            print('он плохой, неряха.')
        else:
            print('Этот чистит валенки,')
            print('моет сам галоши.')
            print('Он хотя и маленький,')
            print('но вполне хороший.')

    def test_condition8(self):
        milk = True
        cereals = False
        eggs = not False

        if milk or cereals or eggs:
            if eggs:
                if milk:
                    breakfast = '- омлет'
                else:
                    breakfast = '- яичница'
            else:
                breakfast = '- хлопья с молоком'
        else:
            if milk:
                breakfast = '- стакан молока'
            elif cereals:
                breakfast = 'можно погрызть сухих хлопьев'
            else:
                breakfast = 'ничего не будет: разгрузочный день'

        print('Сегодня на завтрак', breakfast)


if __name__ == '__main__':
    unittest.main()
