import json

with open("friends_json.txt", "r") as file:
    file_contents = json.load(file)

print(file_contents["friends"][0])

cars = [
    {'make' : 'Ford', 'model' : 'Fiesta'},
    {'make' : 'Ford', 'model' : 'Focus'},
]

with open("cars_json.txt", "w") as file:
    json.dump(cars, file)

my_json_string = '[{"name" : "ALpha", "released" : 2020}]'
my_string = json.loads(my_json_string)

print(my_string)
print(my_string[0]["name"])
