import numpy as np
import logging
logger = logging.getLogger('Brute Force')


class BruteForce:
    def __init__(self, grid):
        self.grid = grid

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
        elif BruteForce.__is_number_valid_in_grid(number, grid, row_position, column_position):
            result = False
        return result

    def run(self):
        current_grid = self.grid.copy()
        for row in range(self.grid.shape[0]):
            for column in range(self.grid.shape[1]):
                if self.grid[row][column] == 0:
                    candidate_numbers = list(range(1, 10))
                    for candidate_number in candidate_numbers:
                        if not BruteForce.__is_number_valid(candidate_number,
                                                            current_grid,
                                                            row,
                                                            column):
                            candidate_numbers.remove(candidate_number)