from fastapi import FastAPI
from routers import rates


app = FastAPI()

app.include_router(rates.router, prefix='/rates', tags=['Rates']) # подключаем роутер для документации

@app.get('/')
def main():
    return {'msg': 'API'}