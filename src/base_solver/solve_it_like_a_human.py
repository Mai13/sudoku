import numpy as np
import logging
logger = logging.getLogger('Solve it like a human')


class SolveItLikeAHuman:

    """
    The idea behind this algorithm is to emulate how would a human being solve a sudoku
    """

    def __is_number_valid_in_grid(self, number, grid, row_position, column_position):
        grid_row = row_position // 3
        grid_column = column_position // 3
        return number in grid[grid_row * 3: 3 * grid_row + 3, grid_column * 3: 3 * grid_column + 3]

    def __is_number_valid(self, number, grid, row_position, column_position):
        result = True
        if number in grid[row_position, :]:
            result = False
        elif number in grid[:, column_position]:
            result = False
        elif self.__is_number_valid_in_grid(number, grid, row_position, column_position):
            result = False
        return result

    def __get_matrix_of_possibilities(self, grid):

        matrix_of_possibilities = list()
        for row_position in range(grid.shape[0]):
            for column_position in range(grid.shape[1]):
                if grid[row_position, column_position] == 0:
                    list_of_candidate_numbers = list()
                    for candidate_number in range(10):
                        if self.__is_number_valid(number=candidate_number,
                                                  grid=grid,
                                                  row_position=row_position,
                                                  column_position=column_position):
                            list_of_candidate_numbers.append(candidate_number)
                    matrix_of_possibilities.append([(row_position, column_position),
                                                    list_of_candidate_numbers,
                                                    len(list_of_candidate_numbers)])
        return matrix_of_possibilities

    def __select_from_matrix(self, matrix_of_possibilities, grid):

        array_matrix_of_possibilities = np.array(matrix_of_possibilities)
        is_feasible = True

        if array_matrix_of_possibilities[array_matrix_of_possibilities[:, 2] == 1].shape[0] == 0:
            is_feasible = False
            logger.error(f'It is not possible to fill the sudoku with this method, the grid is: {grid}')

        for row_with_single_candidate in array_matrix_of_possibilities[array_matrix_of_possibilities[:, 2] == 1]:
            grid[row_with_single_candidate[0][0], row_with_single_candidate[0][1]] = row_with_single_candidate[1][0]

        return is_feasible, grid

    def run(self, grid):

        is_feasible = True

        while grid[grid == 0].shape[0] >= 1:
            matrix_of_possibilities = self.__get_matrix_of_possibilities(grid)
            is_feasible, grid = self.__select_from_matrix(matrix_of_possibilities, grid)
            if not is_feasible:
                logger.error(f'It was not posible to get a solution with this method')
                is_feasible = False
                break

        return is_feasible, grid


