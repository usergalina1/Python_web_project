# Здесь объявите функцию say_about()
def say_about():
    # Код, написанный ниже, переместите в тело объявленной функции
    print('Привет, я Анфиса!')
    print('Я персональный помощник.')
    print('Я ещё маленькая,')
    print('но постоянно расту и умнею:')
    print('ведь мой код каждый день дописывают!')


# Ниже вызовите объявленную вами функцию say_about()
say_about()


# Объявите функцию здесь
def print_friends_count(friends_count):
    # Код, написанный ниже, переместите внутрь объявленной вами функции
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)


print_friends_count(1)
print_friends_count(2)
print_friends_count(6)
print_friends_count(20)


def print_friends_count(friends_count):
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)


# Ниже напишите цикл, в котором будет вызываться функция print_friends_count
# с аргументам от 0 до 20 включительно
for friends_count in range(0, 21):
    print_friends_count(friends_count)
