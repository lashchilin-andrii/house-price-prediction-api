from fastapi import APIRouter

from backend.src import http_code
from backend.src.enum import ModulesEnum
from backend.src.house.schema import HouseData, PredictionResponse

router = APIRouter(
    prefix=f"/{ModulesEnum.house.value}",
    tags=[ModulesEnum.house],
)


@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Predict the price of a house by the given parameters",
    responses={
        200: http_code.OK200().get_response_body(),
        404: http_code.NotFound404().get_response_body(),
    },
)
async def get_predicted_house_price(house: HouseData) -> PredictionResponse:
    """Predict the price of a house by the given parameters."""
    return PredictionResponse(price=1200)
