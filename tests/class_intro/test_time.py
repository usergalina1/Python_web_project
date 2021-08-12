import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2
}


def what_time(city):
    current = dt.datetime.utcnow()
    print(f'UTC: {current}')
    period = dt.timedelta(hours=UTC_OFFSET[city])
    city_time = current + period
    return f'{city} :  {city_time}'
    # return city_time


print(what_time('Екатеринбург'))

# Результат
# UTC: 2021 - 0
# 8 - 10
# 21: 13:48.230221
# 2021 - 0
# 8 - 11
# 02: 13:48.230221

