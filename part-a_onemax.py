import random
import matplotlib.pyplot as plt


# generates a random string
def create_string(length):
    return ''.join(str(random.randint(0, 1)) for _ in range(length))


# calculates the fitness of a string by counting the number of 1s present
def calculate_fitness(string):
    return string.count('1')


# performs one point crossover
def one_point_crossover(p1, p2):
    crossover_point = random.randint(1, len(p1) - 1)
    c1 = p1[:crossover_point] + p2[crossover_point:]
    c2 = p2[:crossover_point] + p1[crossover_point:]
    return c1, c2


ind_len = 30
num_gens = 100
pop_size = 100
population = []
next_pop = []

# create the initial population
for _ in range(pop_size):
    population.append(create_string(ind_len))

# perform one point crossover
for _ in range(len(population) // 2):
    parents = []
    weights = []

    for ind in population:
        weights.append(calculate_fitness(ind))

    for _ in range(2):
        selected_parent = random.choices(population, weights=weights)[0]
        parents.append(selected_parent)
    parent1, parent2 = parents

    child1, child2 = one_point_crossover(parent1, parent2)
    next_pop.extend([child1, child2])

# calculate the fitness of the generations
total_fitness_init = 0
total_fitness_crossed = 0

for ind in population:
    total_fitness_init += calculate_fitness(ind)

average_fitness_init = total_fitness_init / pop_size

for ind in next_pop:
    total_fitness_crossed += calculate_fitness(ind)
average_fitness_crossed = total_fitness_crossed / pop_size

print(average_fitness_init)
print(average_fitness_crossed)

# plt.xlabel('no. of generations')
# plt.ylabel('fitness')
# plt.title('avg fitness')
#
# plt.show()
