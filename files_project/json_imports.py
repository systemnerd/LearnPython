import json

file = open("friends_json.txt", "r")
file_contents = json.load(file)

print(file_contents["friends"][0])

cars = [
    {'make' : 'Ford', 'model' : 'Fiesta'},
    {'make' : 'Ford', 'model' : 'Focus'},
]

file = open("cars_json.txt", "w")
json.dump(cars, file)
file.close()

my_json_string = '[{"name" : "ALpha", "released" : 2020}]'
my_string = json.loads(my_json_string)

print(my_string)
print(my_string[0]["name"])
