import random
from itertools import product


def create_string():
    return ''.join(str(random.randint(0, 1)) for _ in range(30))


def calculate_fitness(individual):
    count = 0

    for i in range(len(individual)):
        if individual[i] == "1":
            count += 1

    return count


new = create_string()
count = calculate_fitness(new)
print(new)
print(count)
