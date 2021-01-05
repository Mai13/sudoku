import numpy as np


class SolveItLikeAHuman:

    """
    The idea behind this algorithm is to emulate how would a human being solve a sudoku
    """

    def __is_number_valid_in_grid(self, number, grid, row_position, column_position):
        grid_row = row_position // 3
        grid_column = column_position // 3
        return number in grid[grid_row: 3 * grid_row + 3, grid_column: 3 * grid_column + 3]

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
        print(matrix_of_possibilities)

    def run(self, grid):

        # while np.where(grid.flatten() == 0)[0].shape[0]) >= 1:


        print(grid)
        print(grid.shape)

        self.__get_matrix_of_possibilities(grid)


