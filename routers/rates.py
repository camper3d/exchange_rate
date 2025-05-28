from fastapi import APIRouter, HTTPException
from services.rates_service import fetch_currency_rates
from models.currency import CheckCurrency
from typing import List


router = APIRouter()

@router.get('/', response_model=List[CheckCurrency])
async def get_currency_rates():
    try:
        rates = await fetch_currency_rates() # получаем курсы через функцию
        return rates # показываем курсы
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
