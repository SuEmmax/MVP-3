from pydantic import BaseModel

class defineData (BaseModel):
    radius:float
    texture:float
    perimeter: float
    area: float
    smothness: float
    compactness: float
    concavity: float
    concave: float
    symmetry:  float
    fractal: float