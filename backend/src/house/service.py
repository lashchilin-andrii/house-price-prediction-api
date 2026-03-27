import pickle
from pathlib import Path

import pandas as pd

from backend.src.house.schema import HouseData, PredictionResponse
from backend.src.http_code import ExpectationFailed417

current_path = Path(__file__).parent
model_path = current_path / "static" / "model.pkl"

with model_path.open("rb") as f:
    model = pickle.load(f)


def preprocess_input(house: HouseData) -> pd.DataFrame:
    """Convert HouseData into DataFrame for model prediction."""
    data = {
        "zn": house.zn,
        "chas": house.chas,
        "rm": house.rm,
        "age": house.age,
        "tax": house.tax,
    }
    df = pd.DataFrame([data])
    return df


def predict_house_price(house: HouseData) -> PredictionResponse:
    """Predict house price using the pre-trained model."""
    X = preprocess_input(house)
    prediction = model.predict(X)[0]

    if prediction < 0:
        raise ExpectationFailed417(
            detail=f"Invalid prediction: model output {prediction:.2f} is less than 0."
        )

    prediction = round(float(prediction), 1)
    return PredictionResponse(medv=prediction)
