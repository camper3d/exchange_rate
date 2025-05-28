from fastapi import APIRouter, HTTPException
from services.rates_service import fetch_currency_rates
from models.currency import CheckCurrency
from typing import List
from fastapi import Query


router = APIRouter()


#
@router.get('/', response_model=List[CheckCurrency])
async def get_currency_rates():
    try:
        rates = await fetch_currency_rates() # получаем курсы через функцию
        return rates # показываем курсы
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# поиск валюты по 3 символам
@router.get('/search', response_model=CheckCurrency)
async def search_currency(code: str = Query(..., min_length=3,max_length=3)):
    rates = await fetch_currency_rates() # получаем курсы через функцию
    for rate in rates:
        if rate.Cur_Abbreviation.upper() == code.upper(): # если буквы большие,то...
            return rate # возврат валюты
    raise HTTPException(status_code=404, detail='Валюта не найдена')