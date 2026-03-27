from pydantic import BaseModel, Field, field_validator


class HouseData(BaseModel):
    zn: float = Field(
        ge=0,
        le=100,
        description="Proportion of residential land zoned for lots over 25,000 sq.ft.",
    )
    chas: int = Field(
        ge=0,
        le=1,
        description="Charles River dummy variable (1 if tract bounds river; 0 otherwise)",
    )
    rm: float = Field(
        ge=3, le=9, description="Average number of rooms per dwelling"
    )
    age: float = Field(
        ge=0,
        le=120,
        description="Proportion of owner-occupied units built prior to 1940 (%)",
    )
    tax: float = Field(
        ge=100, le=800, description="Full-value property tax rate per $10,000"
    )


class PredictionResponse(BaseModel):
    medv: float = Field(description="Predicted house price (MEDV) in $1000s")

    @field_validator("medv", mode="after")
    @classmethod
    def round_medv(cls, v):
        return round(v, 1)
