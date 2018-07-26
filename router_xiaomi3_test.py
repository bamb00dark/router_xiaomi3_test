from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import json

CONFIG_FILE_PATH      = './config.json'

def config_get_pwd_from_file(file):
	config = json.load(file)
	return config["login_password"]

def config_get_addr_from_file(file):
	config = json.load(file)
	return config["miwifi_address"]

def get_local_time():
	return time.asctime(time.localtime(time.time()))

def miwifi_login(browser):
	file = open(CONFIG_FILE_PATH)
	pwd = config_get_pwd_from_file(file)

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

def miwifi_open_browser():
	file = open(CONFIG_FILE_PATH)
	config = json.load(file)
	address = config["miwifi_address"]

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
	print("[LOG]-[{0}]-[wifi setting]: save the 2.4GHz configuration.".format(get_local_time()))

def miwifi_wifi_50_save_config(browser):
	browser.find_elements_by_xpath(".//button[@type='submit']")[1].click()
	print("[LOG]-[{0}]-[wifi setting]: save the 5.0GHz configuration.".format(get_local_time()))

def miwifi_wifi_guest_save_config(browser):
	browser.find_elements_by_xpath(".//button[@type='submit']")[2].click()
	print("[LOG]-[{0}]-[wifi setting]: save the guest wifi configuration.".format(get_local_time()))

def miwifi_wifi_panel_confirm_ok(browser):
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[1]/span").click()
	print("[LOG]-[{0}]-[wifi setting confirm panel] ok button clicked.".format(get_local_time()))
	time.sleep(30)

def miwifi_wifi_panel_confirm_cancel(browser):
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[2]/span").click()
	print("[LOG]-[{0}]-[wifi setting confirm panel] cancel button clicked.".format(get_local_time()))

def miwifi_wifi_panel_confirm_close(browser):
	browser.find_element_by_xpath(".//span[@class='close d-close']").click()
	print("[LOG]-[{0}]-[wifi setting confirm panel] close panel.".format(get_local_time()))

def miwifi_wifi_24_switch_on(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[0].click()

def miwifi_wifi_24_switch_off(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")[0].click()

def miwifi_wifi_24_input_ssid(browser, ssid):
	ssid_length = len(ssid)
	if (ssid_length < 1 or ssid_length > 31):
		print("[ERROR]-[{0}]-[wifi setting] invalid 2.4G SSID name.".format(get_local_time()))
		return
	
	textbox_ssid_24 = browser.find_elements_by_xpath(".//input[@type='text' and @name='ssid']")[0]
	textbox_ssid_24.clear()
	textbox_ssid_24.send_keys(ssid)
	textbox_ssid_24.click() # make the save button visible
	print("[LOG]-[{0}]-[wifi setting] 2.4G SSID is changed to {1}".format(get_local_time(), ssid))

def miwifi_wifi_50_switch_on(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[1].click()

def miwifi_wifi_50_switch_off(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")[1].click()

def miwifi_wifi_50_input_ssid(browser, ssid):
	ssid_length = len(ssid)
	if (ssid_length < 1 or ssid_length > 31):
		print("[ERROR]-[{0}]-[wifi setting] invalid 5.0G SSID name.".format(get_local_time()))
		return
	
	textbox_ssid_50 = browser.find_elements_by_xpath(".//input[@type='text' and @name='ssid']")[1]
	textbox_ssid_50.clear()
	textbox_ssid_50.send_keys(ssid)
	textbox_ssid_50.click() # make the save button visible
	print("[LOG]-[{0}]-[wifi setting] 5.0G SSID is changed to {1}".format(get_local_time(), ssid))

def miwifi_wifi_guest_switch_on(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[2].click()

def miwifi_wifi_guest_switch_off(browser):
	browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")[2].click()

def miwifi_wifi_guest_input_ssid(browser, ssid):
	ssid_length = len(ssid)
	if (ssid_length < 1 or ssid_length > 31):
		print("[ERROR]-[{0}]-[wifi setting] invalid guest SSID name.".format(get_local_time()))
		return
	
	textbox_ssid_guest = browser.find_elements_by_xpath(".//input[@type='text' and @name='ssid']")[2]
	textbox_ssid_guest.clear()
	textbox_ssid_guest.send_keys(ssid)
	textbox_ssid_guest.click() # make the save button visible
	print("[LOG]-[{0}]-[wifi setting] guest SSID is changed to {1}".format(get_local_time(), ssid))


def testcase_wifi_24_on_off_switch():
	browser = miwifi_open_browser()
	miwifi_login(browser)
	time.sleep(2) # wait for web page loading
	miwifi_switch_to_normal_setting(browser)
	miwifi_wifi_24_switch_off(browser)
	miwifi_wifi_24_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)
	miwifi_close_browser(browser)

	browser = miwifi_open_browser()
	miwifi_login(browser)
	time.sleep(2) # wait for web page loading
	miwifi_switch_to_normal_setting(browser)
	miwifi_wifi_24_switch_on(browser)
	miwifi_wifi_24_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)
	miwifi_close_browser(browser)

def testcase_wifi_modify_ssid():
	browser = miwifi_open_browser()
	miwifi_login(browser)
	time.sleep(2) # wait for web page loading
	miwifi_switch_to_normal_setting(browser)
	
	miwifi_wifi_24_input_ssid(browser, "wuxian_2.4G")
	miwifi_wifi_24_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)

	time.sleep(1) # wait for web page reloading
	
	miwifi_wifi_guest_input_ssid(browser, "wuxian_guest")
	miwifi_wifi_guest_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)

	miwifi_close_browser(browser)

if __name__ == '__main__':
	testcase_wifi_24_on_off_switch()
	testcase_wifi_24_modify_ssid()

