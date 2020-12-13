import pandas as pd
import numpy as np
from load_data import LoadData
from check_solution import CheckSudoku


class SudokuSolver:

    def __init__(self, path, dataset):
        self.data_loader = LoadData()
        self.path = path
        self.dataset = dataset
        self.sudoku_checker = CheckSudoku()

    def run(self):
        initial_matrix, solution = self.data_loader.load_data(self.path, self.dataset)
        self.sudoku_checker.is_correct(solution)
