from pydantic import BaseModel

# валидация данных для валюты
class CheckCurrency(BaseModel):
    Cur_ID: int
    Date: str
    Cur_Abbreviation: str
    Cur_Scale: int
    Cur_Name: str
    Cur_OfficialRate: float
