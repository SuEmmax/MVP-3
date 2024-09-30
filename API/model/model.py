import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import pickle
from pickle import load

class MLClassifier:
    def __init__(self):
        filename = './pipelines/modeloML.pkl'
        self.model = joblib.load(open(filename, 'rb'))

    def forecast_data(self, input_data):
        return self.model.predict(input_data)