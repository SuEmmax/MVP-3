import numpy as np
import pickle
from schema.definedata_input import defineData

class DataNormalizer:
    def __init__(self):
        filename = './pipelines/scalerML.pkl'
        self.scaler = pickle.load(open(filename, 'rb'))

    def normalizer_data(self, data: defineData):
        input_data = np.array(list(data.model_dump().values()))
        return self.scaler.transform(input_data.reshape(1, -1))
    
    def normalizer_datas(self, datas: list[defineData]):
        output = []
        for c in datas:
           normalized = self.normalizer_data(c)
           output.append(normalized)
        return np.vstack(output)