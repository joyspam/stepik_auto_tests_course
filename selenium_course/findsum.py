from selenium import webdriver
import time

import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля




    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sm = int(num1) + int(num2)
    s = str(sm)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s) # ищем элемент с текстом "Python"
    button = browser.find_element_by_class_name('btn.btn-default').click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
