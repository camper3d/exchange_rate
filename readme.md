1.
Устанавливаем зависимости при помощи команды:
pip install -r requirements.txt

2. 
Приложение запускаем при помощи команды:
uvicorn main:app --reload

3. 
exchange_rate\main.py - создание приложения FastAPI, подключение роутеров и шаблонов

routers\rates.py - обрабатка запросов на поиск и конвертацию валют

services\rates_service.py - подключение к API банка

models\currency.py - валидация данных валюты

templates\index.html - веб-интерфейс


