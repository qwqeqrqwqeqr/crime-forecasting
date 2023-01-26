
def calculate_life_population_average(life_population):
    return life_population.groupby('집계구코드').mean().reset_index()


