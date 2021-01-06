from load_data import LoadData
from check_solution import CheckSudoku
from brute_force.brute_force import BruteForce
from base_solver.solve_it_like_a_human import SolveItLikeAHuman
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm
import numpy as np
import logging
logger = logging.getLogger('Sudoku Solver')


class SudokuSolver:

    def __init__(self, path, dataset):
        self.data_loader = LoadData()
        self.path = path
        self.dataset = dataset
        self.sudoku_checker = CheckSudoku()

    def run(self):
        initial_matrix, solution = self.data_loader.load_data(self.path, self.dataset)
        logger.info(f'Out of {(9 * 9) ** 9} possibilities this sudoku has {(9 * 9 - np.where(initial_matrix.flatten() == 0)[0].shape[0]) ** 9}')
        logger.info(f'Thd number of filled number is {np.where(initial_matrix.flatten() == 0)[0].shape[0]} out of {9*9}')
        # BruteForce(initial_matrix).run()
        is_feasible, candidate_solution = SolveItLikeAHuman().run(initial_matrix)
        # GeneticAlgorithm().run(initial_matrix)
        self.sudoku_checker.is_correct(solution)  # TODO: Check when is a good idea to use a @staticmethod
        self.sudoku_checker.is_equal(candidate_solution, solution)
