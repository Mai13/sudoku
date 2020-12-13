import numpy as np
import logging
logger = logging.getLogger('Check Sudoku')


class CheckSudoku:

    def __init__(self):
        self.grid = np.array(range(1, 10))

    def is_equal(self, proposed_solution, solution):
        pass

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

        # matrix_3x3 = [solution[3 * i:3 * i + 3] for i in range(3)]
        # matrix_3x3 = [solution[3 * i:3 * i + 3] for i in range(3)]
        solution
        print(solution[0:])
        print(mats_3x3x9)

    def is_correct(self, proposed_solution):
        print(self.__row_constraint(proposed_solution))
        print(self.__column_constraint(proposed_solution))
        print(self.__check_squares(proposed_solution))

