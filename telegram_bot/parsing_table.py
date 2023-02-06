"""Парсит тикеры из таблицы на сайте в файл CSV data_new.csv"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox()
browser = driver.get('https://tvdb.brianthe.dev/')
select_el = driver.find_element(By.NAME, 'screener')
select = Select(select_el)
option_list = select.options
selected_option_list = select.all_selected_options
select.select_by_visible_text('Russia')


xpath_screen = '//*[@id="search"]'
brows = driver.find_element(By.XPATH, value='//*[@id="search"]').click()
for_search = driver.find_element(
    By.XPATH,
    value='//*[@id="search"]'
    ).send_keys('MOEX')
time.sleep(4)
# Количество строк в таблице
lines = driver.find_elements(By.XPATH, '//*[@id="result"]/tr')
# Количество столбцов в таблице
rows = driver.find_elements(By.XPATH, '//*[@id="result"]/tr[1]/td')
# Получим из первой строки таблицы ее заголовки
lines_zag = driver.find_elements(By.XPATH, "/html/body/table/thead/tr")
rc = len(lines)
# получим количество столбцов
cc = len(rows)
# в цикле перебираем список со строками за исключением строки с заголовками
data = []
for i in range(1, rc + 1):
    # Получаем содержимое ячейки с помощью метода text
    d = driver.find_element(By.XPATH, "//tr["+str(i)+"]/td[3]").text
    data.append(d)
with open('data_new.csv', 'w') as f:
    for line in data:
        f.write(line)
        f.write('\n')
for i in range(1, 18):
    brows_2 = driver.find_element(
        By.XPATH,
        value='//*[@id="pagination"]/button[2]'
        ).click()
    time.sleep(1)
    lines_zag = driver.find_elements(By.XPATH, "/html/body/table/thead/tr")
    # перебираем список заголовков таблицы
    # в цикле перебираем список со строками за исключением строки с заголовками
    for i in range(2, rc + 1):
        # в цикле перебираем список столбцов из текущей строки
        # получаем содержимое ячейки с помощью метода text
        d = driver.find_element(By.XPATH, "//tr["+str(i)+"]/td[3]").text
        data.append(d)
        with open('data_new.csv', 'w') as f:
            for line in data:
                f.write(line)
                f.write('\n')

driver.quit()
