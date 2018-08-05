import json

class miwifi_config:

	config_file = './config.json'

	def __init__(self):
		self.fp = open(self.config_file)
		self.config = json.load(self.fp)
		self.fp.close()

	def get_login_pwd(self):
		return self.config["login_password"]

	def get_url(self):
		return self.config["miwifi_address"]