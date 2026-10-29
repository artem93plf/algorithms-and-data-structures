import random


def route_length(route, distances):
    # Замыкаем маршрут: из последнего города в первый.
    return sum(distances[route[i - 1]][route[i]]
               for i in range(len(route)))


def crossover(parent1, parent2, rng):
    # Сохраняем префикс и дополняем без повторов городов.
    cut = rng.randrange(1, len(parent1))
    prefix = parent1[:cut]
    used = set(prefix)
    return prefix + [city for city in parent2
                     if city not in used]


def mutate(route, rng):
    # Меняем местами два различных города.
    i, j = rng.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]


def genetic_tsp(distances, population_size=50,
                generations=100, mutation_rate=0.1, seed=42):
    n = len(distances)
    if n < 2 or any(len(row) != n for row in distances):
        raise ValueError('Нужна квадратная матрица, n >= 2')
    if population_size < 3 or generations < 0:
        raise ValueError('Популяция >= 3, поколения >= 0')
    if not 0 <= mutation_rate <= 1:
        raise ValueError('Вероятность мутации: от 0 до 1')
    rng = random.Random(seed)
    population = [rng.sample(range(n), n)
                  for _ in range(population_size)]

    history = []
    for step in range(generations + 1):
        # Оцениваем каждую особь один раз за поколение.
        scores = [route_length(r, distances)
                  for r in population]
        best_index = min(range(population_size),
                         key=scores.__getitem__)
        best = population[best_index][:]
        history.append(scores[best_index])
        if step == generations:
            return best, scores[best_index], history

        def select_parent():
            # Турнир: лучший из трёх случайных кандидатов.
            candidates = rng.sample(range(population_size), 3)
            winner = min(candidates, key=scores.__getitem__)
            return population[winner]

        # Элитизм: лучший маршрут копируется без изменений.
        new_population = [best]
        while len(new_population) < population_size:
            child = crossover(select_parent(),
                              select_parent(), rng)
            if rng.random() < mutation_rate:
                mutate(child, rng)
            new_population.append(child)
        population = new_population


if __name__ == '__main__':
    distances = [
        [0, 10, 15, 25],
        [10, 0, 20, 35],
        [15, 20, 0, 30],
        [25, 35, 30, 0],
    ]
    route, length, history = genetic_tsp(distances)
    closed = route + [route[0]]
    print('Маршрут:', ' -> '.join(str(x + 1) for x in closed))
    print('Длина:', length)
    print('Число оценённых популяций:', len(history))