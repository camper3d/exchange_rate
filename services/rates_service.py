import httpx
from models.currency import CheckCurrency
from typing import List

NBRB_API_URL = 'https://api.nbrb.by/exrates/rates?periodicity=0'


# функция получения курсов от API
async def fetch_currency_rates() -> List[CheckCurrency]:
    async with httpx.AsyncClient() as client:
        response = await client.get(NBRB_API_URL) # запрос на получение данных от API
        response.raise_for_status() # проверка на успешность запроса
        data = response.json() # json ответ
        return [CheckCurrency(**item) for item in data] # получаем список объектов
