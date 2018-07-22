from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

ROUTER_LOGIN_PASSWORD = 'yangfan703'
ROUTER_ADDRESS   = 'http://192.168.77.1'

def get_local_time():
	return time.asctime(time.localtime(time.time()))

def miwifi_login(browser, pwd):
	try:
		browser.find_element_by_id('password').send_keys(pwd)
		browser.find_element_by_id('btnRtSubmit').click()
		print("[LOG]-[{0}]: login.".format(get_local_time()))
	except NoSuchElementException:
		print("[FAILED] login failed.")

def miwifi_logout(browser):
	try:
		browser.find_element_by_id('sysmenu').click()
		browser.find_element_by_link_text(u"注销").click()		
		print("[LOG]-[{0}]: logout.".format(get_local_time()))
	except NoSuchElementException:
		print("[FAILED] logout failed.")

def miwifi_open_browser(address):
	browser = webdriver.Chrome()
	browser.get(address)
	print("[LOG]-[{0}]: open the browser.".format(get_local_time()))

	return browser

def miwifi_close_browser(browser):
	browser.quit()
	print("[LOG]-[{0}]: close the browser.".format(get_local_time()))

def miwifi_switch_to_normal_setting(browser):
	browser.find_element_by_link_text(u"常用设置").click()
	print("[LOG]-[{0}]-[status]: switch to normal setting.".format(get_local_time()))
	time.sleep(1)

def miwifi_wifi_24_save_config(browser):
	browser.find_elements_by_xpath(".//button[@type='submit']")[0].click()
	print("[LOG]-[{0}]-[wifi setting]: save the configuration of 2.4GHz wifi.".format(get_local_time()))

def miwifi_wifi_50_save_config(browser):
	browser.find_elements_by_xpath(".//button[@type='submit']")[1].click()
	print("[LOG]-[{0}]-[wifi setting]: save the configuration of 5.0GHz wifi.".format(get_local_time()))

def miwifi_wifi_guest_save_config(browser):
	browser.find_elements_by_xpath(".//button[@type='submit']")[2].click()
	print("[LOG]-[{0}]-[wifi setting]: save the configuration of guest wifi.".format(get_local_time()))

def miwifi_wifi_panel_confirm_ok(browser):
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[1]/span").click()
	print("[LOG]-[{0}]-[wifi setting confirm panel] OK.".format(get_local_time()))
	time.sleep(30)

def miwifi_wifi_panel_confirm_cancel(browser):
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[2]/span").click()
	print("[LOG]-[{0}]-[wifi setting confirm panel] Cancel.".format(get_local_time()))

def miwifi_wifi_panel_confirm_close(browser):
	browser.find_element_by_xpath(".//span[@class='close d-close']").click()
	print("[LOG]-[{0}]-[wifi setting confirm panel] Close.".format(get_local_time()))

def miwifi_wifi_24_switch_on(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[0].click()

def miwifi_wifi_24_switch_off(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")[0].click()

def miwifi_wifi_50_switch_on(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[1].click()

def miwifi_wifi_50_switch_off(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")[1].click()

def miwifi_wifi_guest_switch_on(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[2].click()

def miwifi_wifi_guest_switch_off(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")[2].click()


def testcase_wifi_24_on_off_switch():
	browser = miwifi_open_browser(ROUTER_ADDRESS)
	miwifi_login(browser, ROUTER_LOGIN_PASSWORD)
	time.sleep(2) # wait for web page loading
	miwifi_switch_to_normal_setting(browser)
	miwifi_wifi_24_switch_off(browser)
	miwifi_wifi_24_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)
	miwifi_close_browser(browser)

	browser = miwifi_open_browser(ROUTER_ADDRESS)
	miwifi_login(browser, ROUTER_LOGIN_PASSWORD)
	time.sleep(2) # wait for web page loading
	miwifi_switch_to_normal_setting(browser)
	miwifi_wifi_24_switch_on(browser)
	miwifi_wifi_24_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)
	miwifi_close_browser(browser)

if __name__ == '__main__':
	testcase_wifi_24_on_off_switch()
