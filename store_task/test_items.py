import time
def test_alert(browser):
  link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


  browser.get(link)

  item = browser.find_elements_by_class_name('btn.btn-lg.btn-primary')
  assert item, 'no item'



