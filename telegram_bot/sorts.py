import csv
from tradingview_ta import TA_Handler


def find_ticker(message: str):
    """
    Переводит все символы в верхний регистр.
    Сравнивает входящее сообщение с тикерами из файла CSV.
    """
    message = message.upper()
    pure_list = []
    with open('data_new.csv') as f:
        reader = csv.reader(f)
        incl_col = [0]
        for row in reader:
            col = list(str(row[i]) for i in incl_col)
            ticker = ', '.join(map(str, col))
            pure_list.append(ticker)

    if message in pure_list:
        data = TA_Handler(
            symbol=message,
            exchange='MOEX',
            screener='russia',
            interval='1m',
            timeout=10
        )
        analysis = data.get_analysis()
        current_price = (
            analysis.indicators["open"] + analysis.indicators["Mom"]
        )
        return(f'Текущая цена акции {message}: {current_price}\n'
               f'Цена акции {message} при открытии: '
               f'{analysis.indicators["open"]}\n'
               f'Общая рекомендация по акции {message}: {analysis.summary}\n')
    else:
        return(f'Тикер {message} не найден')
