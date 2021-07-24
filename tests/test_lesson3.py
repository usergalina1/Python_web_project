traffic_light = "flashing"
# traffic_light_color = get_color()
traffic_light_color = 'red'

if traffic_light and traffic_light_color == 'red' and traffic_light == 'flashing':
    print("Pause 3 seconds")
elif traffic_light and traffic_light_color == 'red':
    print("Stop until green")
elif traffic_light and traffic_light_color == 'yellow':
    print("Slow down")
else:
    print("Keep going")

data = ["word", 34, False, 0.99]
for count, item in enumerate(data, 5):
    print(f"The value '{item}' is of datatype '{type(item)}' and is located at index '{count}'")


# ls1 = []
    # for item in list1:
    #     ls1.append(str(item))

ls1 = [str(x)*3 for x in data]
print (data)
print(ls1)

for item in {'name': 'Jane', 'age': 12, 'id': '123-45-6789'}.items():
    print(f'{item[0]} is {item[1]}')

for key, value in {'name': 'Jane', 'age': 12, 'id': '123-45-6789'}.items():
    print(f'{key} is {value}')