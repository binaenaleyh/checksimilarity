from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from api import apiRouter
from models import *
from fastapi import status


app = FastAPI(
    title="Check Similarity API",
    description="Measure the similarity between the two texts.",
    debug=True
)

app.include_router(apiRouter)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/compare",  include_in_schema=False)
async def compare(
    request: Request,
    text1: str = Form(...),
    text2: str = Form(...),
    similarity: SimilarityMethod = Form(...),
    vectorizing: VectorizingMethod = Form(...)
):
    input = Input(text1=text1, text2=text2,
                  similarity=similarity, vectorizing=vectorizing)

    try:
        result = input.compare()
    except:
        return RedirectResponse("/?error=true", status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse("result.html", {"request": request, "result": result})
