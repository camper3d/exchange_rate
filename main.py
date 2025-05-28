from fastapi import FastAPI
from routers import rates
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

templates = Jinja2Templates(directory='templates') # подключаем шаблонизатор


app = FastAPI()

app.include_router(rates.router, prefix='/rates', tags=['Rates']) # подключаем роутер для документации

@app.get('/')
def main():
    return {'msg': 'API'}


@app.get('/interface')
async def web_interface(request: Request):
    return templates.TemplateResponse('index.html', {'request': request}) # возвращение шаблона