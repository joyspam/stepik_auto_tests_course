from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

  
    x = browser.find_element_by_id("input_value").text
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_class_name('form-control').send_keys(y)
    button2 = browser.find_element_by_tag_name("button").click()
    
    
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
