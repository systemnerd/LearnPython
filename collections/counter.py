from collections import Counter

values = [23.43, 32.0, 2, 4, 32, 32, 12.43, 4, 2, 4]

values_counter = Counter(values)
print(values_counter[2])
print(values_counter)

greetings = {
    'hello' : "hola",
    'hi': "namsthe",
}

greeting_counter = Counter(greetings)
print(greeting_counter)
print(greeting_counter['hello'])

# not so useful for a dictionary
