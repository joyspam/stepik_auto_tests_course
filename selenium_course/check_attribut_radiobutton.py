from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

  
    x_element = browser.find_element_by_class_name("form-group .nowrap:nth-child(2)")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_class_name('form-control')
    input1.send_keys(y)
    robot = browser.find_element_by_class_name("form-check-input")
    robot.click()
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_radio.click()
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked == 'true', 'WRONG'
    assert robots_checked is None, 'no errors'
    

finally:
    # успеваем скопировать код за 3 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
