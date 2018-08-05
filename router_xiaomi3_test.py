from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from device_config import miwifi_config
import time
import json

g_time_wait_apply_config = 30
g_time_wait_reload_page  = 5
g_time_wait_reboot       = 120
g_time_wait_implicitly   = 10

XPATH_WIFI_24_SSID    = ".//form[@id='wifiset24']/div[@class='form-item form-item-input']/span/input"
XPATH_WIFI_50_SSID    = ".//form[@id='wifiset50']/div[@class='form-item form-item-input']/span/input"
XPATH_WIFI_GUEST_SSID = ".//form[@id='wifisetguest']/div[@class='form-item form-item-input']/span/input"

def get_local_time():
	return time.asctime(time.localtime(time.time()))

def miwifi_login(browser):
	config = miwifi_config()
	pwd = config.get_login_pwd()

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

def miwifi_reboot(browser):
	try:
		browser.find_element_by_id('sysmenu').click()
		browser.find_element_by_link_text(u"重启").click()
		browser.find_element_by_id('rebootAction').click()
		browser.find_element_by_xpath(".//div[@class='d-ft']/a[@data-id='ok']/span").click()
		print("[LOG]-[{0}]: start rebooting device.".format(get_local_time()))
	except NoSuchElementException:
		print("[FAILED] reboot failed.")

def miwifi_open_browser():
	config = miwifi_config()
	url = config.get_url()

	browser = webdriver.Chrome()
	browser.get(url)
	print("[LOG]-[{0}]: open the browser.".format(get_local_time()))

	return browser

def miwifi_close_browser(browser):
	browser.quit()
	print("[LOG]-[{0}]: close the browser.".format(get_local_time()))

def miwifi_switch_to_normal_setting(browser):
	browser.find_element_by_link_text(u"常用设置").click()
	print("[LOG]-[{0}]-[status]: switch to normal setting.".format(get_local_time()))

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
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[@data-id='ok']/span").click()
	print("[LOG]-[{0}]-[wifi setting confirm panel] ok button clicked.".format(get_local_time()))

def miwifi_wifi_panel_confirm_cancel(browser):
	browser.find_element_by_xpath(".//div[@class='d-ft']/a[@data-id='cancel']/span").click()
	print("[LOG]-[{0}]-[wifi setting confirm panel] cancel button clicked.".format(get_local_time()))

def miwifi_wifi_panel_confirm_close(browser):
	browser.find_element_by_xpath(".//span[@class='close d-close']").click()
	print("[LOG]-[{0}]-[wifi setting confirm panel] close panel.".format(get_local_time()))

def miwifi_wifi_24_switch_on(browser):
	radio_buttons = browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")
	radio_buttons[0].click()

def miwifi_wifi_24_switch_off(browser):
	radio_buttons = browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")
	radio_buttons[0].click()

def miwifi_wifi_24_input_ssid(browser, ssid):
	ssid_length = len(ssid)
	if (ssid_length < 1 or ssid_length > 31):
		print("[ERROR]-[{0}]-[wifi setting] invalid 2.4G SSID name.".format(get_local_time()))
		return
	
	textbox_ssid_24 = browser.find_element_by_xpath(XPATH_WIFI_24_SSID)
	textbox_ssid_24.clear()
	textbox_ssid_24.send_keys(ssid)
	textbox_ssid_24.click() # make the save button visible
	print("[LOG]-[{0}]-[wifi setting] 2.4G SSID is changed to {1}".format(get_local_time(), ssid))

def miwifi_wifi_50_switch_on(browser):
	radio_buttons = browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")
	radio_buttons[1].click()

def miwifi_wifi_50_switch_off(browser):
	radio_buttons = browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")
	radio_buttons[1].click()

def miwifi_wifi_50_input_ssid(browser, ssid):
	ssid_length = len(ssid)
	if (ssid_length < 1 or ssid_length > 31):
		print("[ERROR]-[{0}]-[wifi setting] invalid 5.0G SSID name.".format(get_local_time()))
		return
	
	textbox_ssid_50 = browser.find_element_by_xpath(XPATH_WIFI_50_SSID)
	textbox_ssid_50.clear()
	textbox_ssid_50.send_keys(ssid)
	textbox_ssid_50.click() # make the save button visible
	print("[LOG]-[{0}]-[wifi setting] 5.0G SSID is changed to {1}".format(get_local_time(), ssid))

def miwifi_wifi_guest_switch_on(browser):
	radio_buttons = browser.find_elements_by_xpath(".//input[@type='radio' and @value='1']")
	radio_buttons[2].click()

def miwifi_wifi_guest_switch_off(browser):
	radio_buttons = browser.find_elements_by_xpath(".//input[@type='radio' and @value='0']")
	radio_buttons[2].click()

def miwifi_wifi_guest_input_ssid(browser, ssid):
	ssid_length = len(ssid)
	if (ssid_length < 1 or ssid_length > 31):
		print("[ERROR]-[{0}]-[wifi setting] invalid guest SSID name.".format(get_local_time()))
		return
	
	textbox_ssid_guest = browser.find_element_by_xpath(XPATH_WIFI_GUEST_SSID)
	textbox_ssid_guest.clear()
	textbox_ssid_guest.send_keys(ssid)
	textbox_ssid_guest.click() # make the save button visible
	print("[LOG]-[{0}]-[wifi setting] guest SSID is changed to {1}".format(get_local_time(), ssid))


def testcase_wifi_24_on_off_switch():
	# switch off the 2.4GHz wifi
	browser = miwifi_open_browser()
	browser.implicitly_wait(g_time_wait_implicitly)
	miwifi_login(browser)
	miwifi_switch_to_normal_setting(browser)
	miwifi_wifi_24_switch_off(browser)
	miwifi_wifi_24_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)
	time.sleep(g_time_wait_apply_config + g_time_wait_reload_page)
	miwifi_logout(browser)
	miwifi_close_browser(browser)

	# switch on the 2.4GHz wifi
	browser = miwifi_open_browser()
	browser.implicitly_wait(g_time_wait_implicitly)
	miwifi_login(browser)
	miwifi_switch_to_normal_setting(browser)
	miwifi_wifi_24_switch_on(browser)
	miwifi_wifi_24_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)
	time.sleep(g_time_wait_apply_config + g_time_wait_reload_page)
	miwifi_logout(browser)
	miwifi_close_browser(browser)

def testcase_wifi_modify_ssid():
	browser = miwifi_open_browser()
	browser.implicitly_wait(g_time_wait_implicitly)
	miwifi_login(browser)
	miwifi_switch_to_normal_setting(browser)
	
	miwifi_wifi_24_input_ssid(browser, "wuxian_2.4G")
	miwifi_wifi_24_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)
	time.sleep(g_time_wait_apply_config + g_time_wait_reload_page)

	miwifi_wifi_guest_input_ssid(browser, "wuxian_guest")
	miwifi_wifi_guest_save_config(browser)
	miwifi_wifi_panel_confirm_ok(browser)
	time.sleep(g_time_wait_apply_config + g_time_wait_reload_page)

	miwifi_logout(browser)
	miwifi_close_browser(browser)

def testcase_reboot_device():
	browser = miwifi_open_browser()
	browser.implicitly_wait(10)
	miwifi_login(browser)
	miwifi_reboot(browser)
	time.sleep(g_time_wait_reboot)
	miwifi_close_browser(browser)

if __name__ == '__main__':
	#testcase_wifi_24_on_off_switch()
	testcase_wifi_modify_ssid()

	#testcase_reboot_device()

	while True:
		time.sleep(1)

