import pandas as pd
import numpy as np
import random


class LoadData:

    def load_data(self, path, dataset):
        # data = pd.read_csv(f'{path}/{dataset}')
        data = pd.read_csv(f'/Users/maialenberrondo/Desktop/sudoku.csv')
        print(data.shape)
        row_number = random.randint(0, 9000001)
        print(row_number)
        initial_matrix = np.array(list(map(int, list(data['puzzle'][row_number])))).reshape(9, 9)
        solution = np.array(list(map(int, list(data['solution'][row_number])))).reshape(9, 9)
        return initial_matrix, solution