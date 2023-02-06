# Price share telegram bot

## Проект telegram-бота, который информирует о цене акции  
При введении тикера российской акции отправляет в ответ:
* текущую цену,
* цену открытия,
* сводный анализ аналитиков.

### Чтобы развернуть проект локально, нужно:  
Клонировать проект с репозитория.  
> git clone  
Установить виртуальное окружение.  
> python -m venv venv  
Активировать виртуальное окружение.  
> . venv/scripts/activate  
Установить зависимости.  
> pip install -r requirements.txt  
Зарегистрировать своего бота в BotFather в Telegram. Скопировать его токен и вставить в файл .env в формате:  
> TELEGRAM_TOKEN=<Ваш токен>  

#### Автор проекта - Кузнецов Антон.