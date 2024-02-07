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


def selection(population):
    next_generation = []
    total_fitness = 0

    # calculate the fitness of the population
    for ind in population:
        total_fitness += calculate_fitness(ind)

    average_fitness = total_fitness / len(population)

    # perform one-point crossover
    for _ in range(len(population) // 2):
        parents = []
        weights = []

        # get the weights
        for ind in population:
            weights.append(calculate_fitness(ind))

        # select the parents
        for _ in range(2):
            selected_parent = random.choices(population, weights=weights)[0]
            parents.append(selected_parent)
        parent1, parent2 = parents

        child1, child2 = one_point_crossover(parent1, parent2)
        next_generation.extend([child1, child2])

    return next_generation, average_fitness


def genetic_algorithm(str_len, population_size, num_generations):
    population = []
    average_fitnesses = []

    # generate the initial population
    for _ in range(population_size):
        population.append(create_string(str_len))

    # evolve the population
    for generation in range(num_generations):
        population, average_fitness = selection(population)
        average_fitnesses.append(average_fitness)

    return average_fitnesses


ind_len = 30
num_gens = 100
pop_size = 100

avg_fitnesses = genetic_algorithm(ind_len, pop_size, num_gens)

# plot the average fitness over each generation
plt.plot(range(num_gens), avg_fitnesses)

plt.xlabel('no. of generations')
plt.ylabel('fitness')
plt.title('avg fitness')

plt.show()