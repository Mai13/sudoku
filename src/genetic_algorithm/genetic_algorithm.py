import numpy as np
import pygad


class GeneticAlgorithm:

    def __init__(self):
        pass

    @staticmethod
    def __is_number_valid_in_grid(number, grid, row_position, column_position):
        grid_row = row_position // 3
        grid_column = column_position // 3
        return number in grid[grid_row: 3 * grid_row + 3, grid_column: 3 * grid_column + 3]

    @staticmethod
    def __is_number_valid(number, grid, row_position, column_position):
        result = True
        if number in grid[row_position, :]:
            result = False
        elif number in grid[:, column_position]:
            result = False
        elif GeneticAlgorithm.__is_number_valid_in_grid(number, grid, row_position, column_position):
            result = False
        return result

    def __create_grid(self, sudoku):
        grid_list = sudoku.flatten().reshape(-1, 1)[sudoku.flatten().reshape(-1, 1) == 0]
        positions = np.where(sudoku.flatten().reshape(-1, 1) == 0)
        return grid_list, positions[0]

    def __how_many_numbers_are_okey(self):
        pass

    def __fitness_function(self, solution):
        pass

    def run(self, sudoku):

        fitness_function = self.__fitness_function

        num_generations = 50
        num_parents_mating = 4

        sol_per_pop = 8
        num_genes = len(self.__create_grid(sudoku)[0])

        init_range_low = -2
        init_range_high = 5

        parent_selection_type = "sss"
        keep_parents = 1

        crossover_type = "single_point"

        mutation_type = "random"
        mutation_percent_genes = 10

        ga_instance = pygad.GA(num_generations=num_generations,
                               num_parents_mating=num_parents_mating,
                               fitness_func=fitness_function,
                               sol_per_pop=sol_per_pop,
                               num_genes=num_genes,
                               init_range_low=init_range_low,
                               init_range_high=init_range_high,
                               parent_selection_type=parent_selection_type,
                               keep_parents=keep_parents,
                               crossover_type=crossover_type,
                               mutation_type=mutation_type,
                               mutation_percent_genes=mutation_percent_genes)
        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        print("Parameters of the best solution : {solution}".format(solution=solution))
        print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))


