from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

ROUTER_LOGIN_PASSWORD = 'yangfan703'
ROUTER_ADDRESS   = 'http://192.168.77.1'

def router_login(browser, pwd):
	try:
		browser.find_element_by_id('password').send_keys(pwd)
		browser.find_element_by_id('btnRtSubmit').click()
	except NoSuchElementException:
		print("[FAILED] login failed.")

def router_logout(browser):
	try:
		browser.find_element_by_id('sysmenu').click()
		browser.find_element_by_link_text(u"注销").click()
	except NoSuchElementException:
		print("[FAILED] logout failed.")

def router_open_browser(address):
	browser = webdriver.Chrome()
	browser.get(address)

	return browser

def router_close_browser(browser):
	browser.quit()

def router_jump_to_normal_setting(browser):
	browser.find_element_by_link_text(u"常用设置").click()
	sleep(1)

def router_enable_wifi_24(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[0].click()
	browser.find_elements_by_xpath(".//button[@type='submit']")[0].click()
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[1]/span").click()

def router_disable_wifi_24(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")[0].click()
	browser.find_elements_by_xpath(".//button[@type='submit']")[0].click()
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[1]/span").click()

def router_enable_wifi_50(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[1].click()
	browser.find_elements_by_xpath(".//button[@type='submit']")[1].click()
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[1]/span").click()

def router_disable_wifi_50(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")[1].click()
	browser.find_elements_by_xpath(".//button[@type='submit']")[1].click()
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[1]/span").click()

def router_enable_wifi_guest(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[2].click()
	browser.find_elements_by_xpath(".//button[@type='submit']")[2].click()
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[1]/span").click()

def router_disable_wifi_guest(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")[2].click()
	browser.find_elements_by_xpath(".//button[@type='submit']")[2].click()
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[1]/span").click()

if __name__ == '__main__':
	browser = router_open_browser(ROUTER_ADDRESS)

	router_login(browser, ROUTER_LOGIN_PASSWORD)

	# wait for web page loading
	sleep(2)

	router_jump_to_normal_setting(browser)

	router_enable_wifi_24(browser)

	#router_logout(browser)
	sleep(30)

	router_close_browser(browser)