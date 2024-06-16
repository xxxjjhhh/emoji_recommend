import json
import math

from ncpApiCall import NcpApiCall

from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel

import uvicorn

ncpApiCall = NcpApiCall()
app = FastAPI()
templates = Jinja2Templates(directory="templates")

def distance(vector1: list, vector2: list) -> float:
    sum_of_squares = sum((v2 - v1) ** 2 for v1, v2 in zip(vector1, vector2))
    return math.sqrt(sum_of_squares)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

class Item(BaseModel):
    title: str

@app.post("/emoji")
async def read_emoji(item: Item):
    title = item.title
    request_data = json.loads(f'{{"text": "{title}"}}', strict=False)
    response_data = ncpApiCall.execute(request_data)

    with open("emoji_vector.json") as file:
        candidate_data = json.load(file)

    dist_list = []
    for row in candidate_data:

        dist_data = {"hexcode": row['hexcode'], "distance": distance(row['vector'], response_data)}
        dist_list.append(dist_data)

    min_distance_row = min(dist_list, key=lambda x: float(x["distance"]))
    min_hexcode = min_distance_row['hexcode']

    return {"hexcode": min_hexcode}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
