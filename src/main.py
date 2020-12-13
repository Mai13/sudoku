from set_logger import create_logger
import traceback
import pathlib
from sudoku_solver import SudokuSolver

path = pathlib.Path(__file__).parent.parent.absolute()
logger = create_logger(f'{path}/results', 'INFO')

dataset = 'head_sudoku.csv'

if __name__ == '__main__':
    sudoku_solver = SudokuSolver(path=f'{path}/data',
                                 dataset=dataset)
    logger.info(f"Program starts here")
    try:
        sudoku_solver.run()
    except Exception as e:
        track = traceback.format_exc()
        logger.error(f"There was an error while executing the promgram {track}")
    logger.info('Ends program')
