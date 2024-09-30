from flask_openapi3 import OpenAPI, Info
from flask import redirect
from schema.definedata_input import defineData
from model.data_normalizer import DataNormalizer
from model.model import MLClassifier
from flask_cors import CORS

info = Info(title="Machine Learning Model for breast illnes prediction", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

normalizer = DataNormalizer()
classifier = MLClassifier()

@app.get("/")
def home():
    """Documentação.
    """
    return redirect('/openapi/swagger')

@app.post("/classify")
def classify(body: defineData):
    """Breast health forecasting.
    """
    input_normalizedata = normalizer.normalizer_data(body)
    classification = classifier.forecast_data(input_normalizedata)
    return {"classification": classification[0]}
