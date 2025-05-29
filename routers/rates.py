from fastapi import APIRouter, HTTPException
from services.rates_service import fetch_currency_rates
from models.currency import CheckCurrency
from typing import List
from fastapi import Query


router = APIRouter()


# Получаем список всех валют с курсами
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

# Конвертация суммы валют
@router.get('/convert')
async def convert_currency(
        amount: float = Query(...,gt=0),
        from_code: str = Query(..., min_length=3, max_length=3),
        to_code: str = Query(..., min_length=3, max_length=3)
):
    try:
        rates = await fetch_currency_rates() # получаем курсы через функцию

        from_rate = None
        to_rate = None

        for i in rates:
            if i.Cur_Abbreviation.upper() == from_code.upper():
                from_rate = i
                break

        for i in rates:
            if i.Cur_Abbreviation.upper() == to_code.upper():
                to_rate = i
                break
        if not from_rate or not to_rate:
            raise HTTPException(status_code=404, detail='Валюта не найдена')

        # Конвертация
        byn_amount = amount * (from_rate.Cur_OfficialRate / from_rate.Cur_Scale) # переводим сумму в BYN
        converted = byn_amount / (to_rate.Cur_OfficialRate / to_rate.Cur_Scale) # из BYN переводим в нужную валюту

        return {
            'from': from_code.upper(),
            'to': to_code.upper(),
            'original_amount': amount,
            'converted_amount': round(converted, )
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))