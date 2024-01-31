import random
import matplotlib.pyplot as plt
from itertools import product


def create_string():
    return ''.join(str(random.randint(0, 1)) for _ in range(30))


def calculate_fitness(individual):
    count = 0

    for i in range(len(individual)):
        if individual[i] == "1":
            count += 1

    return count


gen_len = 100
pop_len = 100

avg_fitness = []

for i in range(gen_len):
    total_pop_fitness = 0

    for j in range(pop_len):
        x = create_string()
        x_fitness = calculate_fitness(x)
        total_pop_fitness += x_fitness

    total_pop_fitness = total_pop_fitness / pop_len
    avg_fitness.append(total_pop_fitness)

# plot average fitness over generations
plt.plot(range(gen_len), avg_fitness)

plt.xlabel('no. of generations')
plt.ylabel('fitness')
plt.title('avg fitness')

plt.show()
