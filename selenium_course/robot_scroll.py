from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

  
    x_element = browser.find_element_by_class_name("form-group .nowrap:nth-child(2)")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_class_name('form-control')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    
    input1.send_keys(y)
    robot = browser.find_element_by_class_name("form-check-input")
    robot.click()
    rules = browser.find_element_by_class_name("form-check.form-radio-custom .form-check-label")
    rules.click()
    button = browser.find_element_by_tag_name("button")
    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
