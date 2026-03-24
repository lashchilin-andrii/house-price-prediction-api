from pydantic import BaseModel, Field
from typing import Literal

class HouseData(BaseModel):
    area: float = Field(ge=500, le=5000, description="Square footage of the house")
    bedrooms: int = Field(ge=1, le=5, description="Number of bedrooms")
    bathrooms: int = Field(ge=1, le=4, description="Number of bathrooms")
    floors: int = Field(ge=1, le=3, description="Number of floors")
    year_built: int = Field(ge=1900, le=2023, description="Year the house was built")
    location: Literal["Downtown", "Urban", "Suburban", "Rural"] = Field(description="Location type")
    condition: Literal["Excellent", "Good", "Fair", "Poor"] = Field(description="House condition")
    garage: bool = Field(description="Availability of garage")

class PredictionResponse(BaseModel):
    price: float = Field(ge=0, description="Predicted house price in dollars")