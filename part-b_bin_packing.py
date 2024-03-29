import random
import matplotlib.pyplot as plt

# Problem instances
instances = [
    '''BPP      1'
          46
        1000
         200         3
         199         1
         198         2
         197         2
         194         2
         193         1
         192         1
         191         3
         190         2
         189         1
         188         2
         187         2
         186         1
         185         4
         184         3
         183         3
         182         3
         181         2
         180         1
         179         4
         178         1
         177         4
         175         1
         174         1
         173         2
         172         1
         171         3
         170         2
         169         3
         167         2
         165         2
         164         1
         163         4
         162         1
         161         1
         160         2
         159         1
         158         3
         157         1
         156         6
         155         3
         154         2
         153         1
         152         3
         151         2
         150         4''',
    '''BPP      2'
          47
        1000
         200         2
         199         4
         198         1
         197         1
         196         2
         195         2
         194         2
         193         1
         191         2
         190         1
         189         2
         188         1
         187         2
         186         1
         185         2
         184         5
         183         1
         182         1
         181         3
         180         2
         179         2
         178         1
         176         1
         175         2
         174         5
         173         1
         172         3
         171         1
         170         4
         169         2
         168         1
         167         5
         165         2
         164         2
         163         3
         162         2
         160         2
         159         2
         158         2
         157         4
         156         3
         155         2
         154         1
         153         3
         152         2
         151         2
         150         2''',
    '''BPP      3'
          44
        1000
         200         1
         199         2
         197         2
         196         2
         193         3
         192         2
         191         2
         190         2
         189         3
         188         1
         187         1
         185         3
         183         2
         182         1
         181         3
         180         3
         179         3
         178         1
         177         5
         176         2
         175         5
         174         4
         173         1
         171         3
         170         1
         169         2
         168         5
         167         1
         166         4
         165         2
         163         1
         162         2
         161         2
         160         3
         159         2
         158         2
         157         1
         156         3
         155         3
         154         1
         153         2
         152         3
         151         2
         150         1''',
    '''BPP      4'
          42
        1000
         200         3
         199         5
         198         4
         197         1
         195         1
         193         4
         192         1
         188         1
         187         1
         186         3
         185         3
         184         2
         183         2
         182         1
         181         1
         180         3
         179         2
         178         6
         177         2
         176         4
         175         1
         173         4
         172         4
         170         1
         169         3
         168         4
         167         1
         165         3
         164         1
         163         2
         162         4
         161         1
         160         3
         159         3
         158         1
         157         3
         155         2
         154         3
         153         1
         152         3
         151         1
         150         1''',
    '''BPP      5'
          44
        1000
         200         5
         199         2
         198         2
         197         2
         196         1
         195         3
         194         2
         193         2
         192         4
         191         2
         190         4
         188         3
         187         2
         186         2
         185         1
         184         1
         183         1
         182         1
         181         3
         180         1
         178         3
         177         2
         176         2
         174         1
         173         1
         172         1
         171         3
         168         2
         167         1
         165         1
         164         1
         163         1
         162         3
         161         3
         160         3
         159         2
         158         3
         157         3
         156         2
         155         5
         154         3
         153         3
         151         5
         150         2'''
]


def parse_instance(instance):
    lines = instance.split('\n')
    capacity = int(lines[2])
    items = []
    for line in lines[3:]:
        if line.strip():
            weight, value = map(int, line.split())
            items.append((weight, value))
    return capacity, items


def create_bin(capacity, items):
    bins = [[]]
    bin_info = []

    for weight, count in items:
        placed = False
        for b in bins:
            if sum(b) + weight <= capacity:
                b.append(weight)
                placed = True
                break
        if not placed:
            bin_info.append((sum(b), b[:]))
            bins.append([weight])
    bin_info.append((sum(bins[-1]), bins[-1][:]))

    return bin_info


def calculate_fitness(individual):
    return len(individual)


def one_point_crossover(p1, p2):
    crossover_point = random.randint(1, min(len(p1), len(p2)) - 1)
    c1 = p1[:crossover_point] + p2[crossover_point:]
    c2 = p2[:crossover_point] + p1[crossover_point:]
    return c1, c2


def standard_mutation(individual, rate_mutation):
    for bin_value, bin_items in individual:
        if random.random() < rate_mutation:
            item_index = random.randint(0, len(bin_items) - 1)
            bin_items[item_index] = random.choice(bin_items)
    return individual


def selection(population, rate_mutation):
    next_generation = []
    total_fitness = sum(calculate_fitness(ind) for ind in population)
    average_fitness = total_fitness / len(population)

    for _ in range(len(population) // 2):
        parents = random.choices(population, k=2, weights=[calculate_fitness(ind) for ind in population])
        child1, child2 = one_point_crossover(parents[0], parents[1])
        child1 = standard_mutation(child1, rate_mutation)
        child2 = standard_mutation(child2, rate_mutation)
        next_generation.extend([child1, child2])

    return next_generation, average_fitness


def genetic_algorithm(instances, population_size, num_generations, rate_mutation):
    avg_fitnesses = []
    bin_counts = []

    for instance in instances:
        capacity, items = parse_instance(instance)
        population = [create_bin(capacity, items) for _ in range(population_size)]
        for generation in range(num_generations):
            population, average_fitness = selection(population, rate_mutation)
            avg_fitnesses.append(average_fitness)

        bin_counts.append(len(population[0]))
        
        print(f"Number of bins used for instance: {len(population[0])}")

    plt.plot(range(1, len(bin_counts) + 1), bin_counts, marker='o', linestyle='-')
    plt.xlabel('Instance Number')
    plt.ylabel('Number of Bins Used')
    plt.title('Number of Bins Used for Each Instance')
    plt.grid(True)
    plt.show()

    return avg_fitnesses


pop_size = 100
num_gens = 100
rate_mut = 0.01

avg_fitnesses = genetic_algorithm(instances, pop_size, num_gens, rate_mut)
