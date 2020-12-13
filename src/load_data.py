import pandas as pd
import numpy as np


class LoadData:

    def load_data(self, path, dataset):
        data = pd.read_csv(f'{path}/{dataset}')
        initial_matrix = np.array(list(map(int, list(data['puzzle'][0])))).reshape(9, 9)
        solution = np.array(list(map(int, list(data['solution'][0])))).reshape(9, 9)
        return initial_matrix, solution