import random

# Parameters
N = 8           # Number of queens (and the size of the board)
POPULATION_SIZE = 500
MUTATION_RATE = 0.05
MAX_GENERATIONS = 5000

class Individual:
    def __init__(self):
        # Randomly initialize a board configuration with N queens.
        # Each index represents a row, and the value at that index represents the column of the queen.
        self.genes = [random.randint(0, N - 1) for _ in range(N)]
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # Calculate the fitness score, which is the number of non-attacking pairs of queens
        non_attacking_pairs = 0
        for i in range(N):
            for j in range(i + 1, N):
                # Check if queens i and j attack each other
                if self.genes[i] != self.genes[j] and abs(self.genes[i] - self.genes[j]) != abs(i - j):
                    non_attacking_pairs += 1
        return non_attacking_pairs

def create_initial_population():
    # Generate the initial population of random individuals
    return [Individual() for _ in range(POPULATION_SIZE)]

def selection(population):
    # Select two individuals based on fitness-proportionate selection (roulette wheel)
    max_fitness = sum(individual.fitness for individual in population)
    selection_probs = [individual.fitness / max_fitness for individual in population]
    return random.choices(population, weights=selection_probs, k=2)

def crossover(parent1, parent2):
    # Perform crossover to create a child individual
    crossover_point = random.randint(0, N - 1)
    child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    child = Individual()
    child.genes = child_genes
    child.fitness = child.calculate_fitness()
    return child

def mutate(individual):
    # Mutate an individual's genes with a small probability
    if random.random() < MUTATION_RATE:
        index = random.randint(0, N - 1)
        individual.genes[index] = random.randint(0, N - 1)
        individual.fitness = individual.calculate_fitness()

def genetic_algorithm():
    population = create_initial_population()
    for generation in range(MAX_GENERATIONS):
        # Sort the population based on fitness (higher is better)
        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        # If we find an individual with the maximum fitness, we've solved the problem
        if population[0].fitness == N * (N - 1) // 2:
            print(f"Solution found in generation {generation + 1}")
            return population[0]

        # Create a new generation
        new_population = []

        # Perform selection, crossover, and mutation to create new individuals
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = selection(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.append(child1)
            new_population.append(child2)

        population = new_population

    print("No solution found within the maximum number of generations.")
    return None

def print_board(individual):
    board = [["." for _ in range(N)] for _ in range(N)]
    for row, col in enumerate(individual.genes):
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))
    print()

# Run the genetic algorithm
solution = genetic_algorithm()
if solution:
    print("Final board configuration:")
    print_board(solution)
