import random


def create_string():
    str = []
    for x in range(30):
        str.append(random.choice(["0","1"]))

    return str

def create_string_wrong():
    str = []
    for x in range(30):
        str.append(''.join(random.choice(["0","1"])))

    return str

newstr = create_string()
print(newstr)

def calculate_fitness(individual):
    return 1