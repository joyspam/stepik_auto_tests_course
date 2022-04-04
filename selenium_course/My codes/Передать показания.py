print('Ввести показания за ВОДУ и нажать ENTER')
water = input()
print('Ввести показания за ГАЗ и нажать ENTER')
gaz = input()
print('Ввести показания за СВЕТ и нажать ENTER')
power = input()
print('Идёт передача показаний...')

from selenium import webdriver
import time




try:

    #код передачи показаний за воду
    link = "https://xn--80a6aab2a.xn--p1ai/person/status/"
    browser = webdriver.Chrome()
    browser.get(link)

    inputclear = browser.find_element_by_id('number').clear()
    inputid = browser.find_element_by_id('number').send_keys('0130199786')

  


    button = browser.find_element_by_css_selector(".darken-2")
    button.click()

    time.sleep(3)

    
    inputclear = browser.find_element_by_class_name('input-field_address').clear()
    inputadress = browser.find_element_by_class_name('input-field_address').send_keys('г. Саратов, туп Кавказский 1-й, д. 8, кв. 27')

    button = browser.find_element_by_id("address-ok").click()
    
    # ждем загрузки страницы
    time.sleep(3)
    datap = browser.find_element_by_xpath('//div/*[@class="sendIpuData__item-input"]')
    datap.send_keys(water)
    

    button = browser.find_element_by_id("ipu-send").click()
    time.sleep(3)


    noerr1 = browser.find_element_by_class_name('request-ipu__header').text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    voda = 0
    if "Мы приняли Ваши показания. Спасибо за обращение!" == noerr1:
        print('Показания за воду приняты')
        voda = 1
    else:
        print('Ошибка передачи показаний за воду')
    browser.quit()

        

    #код передачи показаний за газ

    link = "https://www.sargc.ru/counters.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputid = browser.find_element_by_name('account').send_keys('720021114670')
    inputind = browser.find_element_by_name('indication').send_keys(gaz)
    eltext = browser.find_element_by_id('ctrl_11').get_attribute('placeholder')
    s = []
    for i in eltext:
        if i.isdigit():
            s+=i
    s = int(s[0])+int(s[1])

    inputans = browser.find_element_by_id('ctrl_11').send_keys(s)
    time.sleep(3)

    button = browser.find_element_by_id("ctrl_6").click()

    time.sleep(3)

    noerr2 = browser.find_element_by_tag_name('h1').text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    g = 0
    if "Спасибо" == noerr2:
        print('Показания за газ приняты')
        g = 1
    else:
        print('Ошибка передачи показаний за газ')
    browser.quit()


    #код передачи показаний за свет


    link = "http://www.spges.ru/index.php/voprosy/pokazaniya-priborov-ucheta-elektroenergii"
    browser = webdriver.Chrome()
    browser.get(link)

    inputid = browser.find_element_by_name('input_text_1').send_keys('24810980')
    inputadress = browser.find_element_by_name('input_text_2').send_keys('Кавказский 1-й тупик, дом 8, кв 27')
    inputind = browser.find_element_by_name('input_text_3').send_keys(power)
    inputtel = browser.find_element_by_name('input_text_4').send_keys('89063075095')

    seq = browser.find_element_by_xpath('//*[@id="chrono_security_answer1_container_div"]/label').text
  
    s = []
    s += seq
    if s[2] == '*':
        ans = (int(s[0])*int(s[4]))
    elif s[2] == '/':
        ans = (int(s[0])/int(s[4]))
    elif s[2] == '+':
        ans = (int(s[0])+int(s[4]))
    elif s[2] == '-':
        ans = (int(s[0])-int(s[4]))
    inputans = browser.find_element_by_name('chrono_security_answer').send_keys(ans)
    butpower = browser.find_element_by_name('input_submit_5').click()

    time.sleep(3)

    noerr3 = browser.find_element_by_xpath('//*[@id="col1"]/div[2]/div[1]/p[8]/span').text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    svet = 0
    if "Спасибо! Ваши показания приборов отправлены." == noerr3:
        print('Показания за свет приняты')
        svet = 1
    else:
        print('Ошибка передачи показаний за свет')

    



finally:
    if voda == 1 and g == 1 and svet == 1:
        print('Завершено успешно')
    else:
        print('Ошибка при выполнении')
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
