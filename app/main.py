from fastapi import FastAPI, Response, Cookie
from datetime import datetime

app = FastAPI()


@app.get("/")
def root(response: Response, last_visit=Cookie()):
    now = datetime.now()
    response.set_cookie(key="model_user", value=now)
    return {"model_user": "куки установлены"}, {"Последний визит на страницу": last_visit}