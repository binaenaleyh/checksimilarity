from fastapi import APIRouter
from models import Input, Result

apiRouter = APIRouter(
    prefix="/api",
    tags=["main"],
    responses={404: {"description": "Not found"}},
)


@apiRouter.post("/measure")
async def measure(input: Input):

    result = input.compare()

    return {"value": result.value}
