from fastapi import APIRouter, Query

from backend.src import http_code
from backend.src.enum import ModulesEnum
from backend.src.house.schema import HouseData, PredictionResponse
from backend.src.house.service import predict_house_price

router = APIRouter(
    prefix=f"/{ModulesEnum.house.value}",
    tags=[ModulesEnum.house],
)


@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Predict the price of a house using HouseData model",
    responses={
        200: http_code.OK200().get_response_body(),
        422: http_code.UnprocessableEntity422().get_response_body(),
    },
)
async def predict_house(house: HouseData) -> PredictionResponse:
    """Predict the price of a house by passing a HouseData object."""
    return predict_house_price(house)


@router.post(
    "/predict/params",
    response_model=PredictionResponse,
    summary="Predict house price using individual parameters",
    responses={
        200: http_code.OK200().get_response_body(),
        417: http_code.ExpectationFailed417().get_response_body(),
        422: http_code.UnprocessableEntity422().get_response_body(),
    },
)
async def predict_house_params(
    zn: float = Query(
        ...,
        ge=0,
        le=100,
        description="Proportion of residential land zoned for lots over 25,000 sq.ft.",
    ),
    chas: int = Query(
        ...,
        ge=0,
        le=1,
        description="Charles River dummy variable (1 if tract bounds river; 0 otherwise)",
    ),
    rm: float = Query(
        ..., ge=3, le=9, description="Average number of rooms per dwelling"
    ),
    age: float = Query(
        ...,
        ge=1,
        le=100,
        description="Proportion of owner-occupied units built prior to 1940 (%)",
    ),
    tax: float = Query(
        ...,
        ge=100,
        le=800,
        description="Full-value property tax rate per $10,000",
    ),
) -> PredictionResponse:
    """Predict house price using individual input parameters."""
    house_data = HouseData(zn=zn, chas=chas, rm=rm, age=age, tax=tax)
    return predict_house_price(house_data)
