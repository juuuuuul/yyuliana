import random
from deap import creator, base, tools, algorithms

def evaluate_max(individual):
    return max(individual),

def main():
    # Инициализация алгоритма
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_bool", random.randint, 0, 1000) 
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=7)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", evaluate_max)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=1000, indpb=0.2) 
    toolbox.register("select", tools.selTournament, tournsize=3)

    population = toolbox.population(n=50)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40

    for gen in range(NGEN):
        offspring = algorithms.varAnd(population, toolbox, cxpb=CXPB, mutpb=MUTPB)
        fits = toolbox.map(toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        population = toolbox.select(offspring, k=len(population))
        top_individual = tools.selBest(population, k=1)[0]
        print("Generation:", gen + 1, " Best Individual:", top_individual)

    best_individual = tools.selBest(population, k=1)[0]
    print("Best Individual:", best_individual)

if __name__ == "__main__":
    main()