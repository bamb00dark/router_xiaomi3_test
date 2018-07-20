from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

ROUTER_LOGIN_PWD = 'yangfan703'
ROUTER_ADDRESS   = 'http://192.168.77.1'

browser = webdriver.Chrome()
browser.get(ROUTER_ADDRESS)

print(browser.title)

# login to router
browser.find_element_by_id('password').send_keys(ROUTER_LOGIN_PWD)
browser.find_element_by_id('btnRtSubmit').click()

# wait for loading the web page 
sleep(2)

try:
	# logout
	browser.find_element_by_id('sysmenu').click()
	browser.find_element_by_link_text(u"注销").click()
except NoSuchElementException:
	print("[FAILED] logout failed.")
finally:
	# close the browser
	browser.quit()