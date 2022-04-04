from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

  
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    robot = browser.find_element_by_id("robotCheckbox")
    robot.click()
    rules = browser.find_element_by_id("robotsRule")
    rules.click()
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()
    

finally:
    # успеваем скопировать код за 3 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
