from load_data import LoadData
from check_solution import CheckSudoku
from sudoku_solver_with_linear_programation.linear_solver import LinearProgramingSolver


class SudokuSolver:

    def __init__(self, path, dataset):
        self.data_loader = LoadData()
        self.path = path
        self.dataset = dataset
        self.sudoku_checker = CheckSudoku()

    def run(self):
        initial_matrix, solution = self.data_loader.load_data(self.path, self.dataset)
        LinearProgramingSolver(initial_matrix).run()
        self.sudoku_checker.is_correct(solution)  # TODO: Check when is a good idea to use a @staticmethod
        self.sudoku_checker.is_equal(solution, solution)
