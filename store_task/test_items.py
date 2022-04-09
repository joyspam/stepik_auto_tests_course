import time
def test_add_to_cart_button_is_displayed(browser):
  link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


  browser.get(link)
  time.sleep(30)

  item = browser.find_elements_by_class_name('btn.btn-lg.btn-primary')
  assert item, 'no item'

  
