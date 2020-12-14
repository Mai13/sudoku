import numpy as np
import logging
logger = logging.getLogger('Check Sudoku')


class CheckSudoku:

    def __init__(self):
        self.grid = np.array(range(1, 10))

    def is_equal(self, proposed_solution, solution):
        if np.array_equal(proposed_solution, solution):
            logger.info(f'The two solutions are equal')
        else:
            logger.info(f'The two solutions are not equal:')
            logger.info(f'Proposed solution: {proposed_solution}')
            logger.info(f'Proposed solution: {solution}')

    def __row_constraint(self, solution):
        result = True
        for row in range(solution.shape[0]):
            if set(solution[row]) != set(self.grid):
                result = False
                logger.info(f'The row {row}, does not fill the row constraint')
                break
        return result

    def __column_constraint(self, solution):
        result = True
        for column in range(solution.shape[1]):
            if set(solution[:, 1]) != set(self.grid):
                result = False
                logger.info(f'The column {column}, does not fill the column constraint')
                break
        return result

    def __check_squares(self, solution):
        result = True
        matrix_3x3 = [solution[3 * i:3 * i + 3, 3 * j:3 * j + 3] for i in range(3) for j in range(3)]
        for grid_number in range(len(matrix_3x3)):
            if set(matrix_3x3[0].flatten()) != set(self.grid):
                result = False
                logger.info(f'The grid {grid_number}, does not fill grid constraint')
                break
        return result

    def is_correct(self, proposed_solution):
        if self.__row_constraint(proposed_solution) and self.__column_constraint(proposed_solution) and self.__check_squares(proposed_solution):
            logger.info(f'The solution proposed in correct')
        else:
            logger.info(f'The solution is wrong')

