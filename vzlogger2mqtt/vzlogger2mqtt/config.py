import yaml
import logging
import logging.config

class Config:
	"""Class for parsing vzlogger2mqtt.yaml."""
	
	def __init__(self):
		"""Initialize Config class."""
		logging.config.fileConfig('logging.conf')
		self._mqtt = {}
		self._vzlogger = {}
	
	
	def read(self, file='vzlogger2mqtt.yaml'):
		"""Read config."""
		logging.debug("Reading %s", file)
		try:
			with open(file, 'r') as filehandle:
				config = yaml.load(filehandle)
				self._parse_mqtt(config)
				self._parse_vzlogger(config)
		except FileNotFoundError as ex:
			logging.error("Error while reading %s: %s", file, ex)


	def _parse_mqtt(self, config):
		"""Parse the mqtt section of vzlogger2mqtt.yaml."""
		if "mqtt" in config:
			self._mqtt = config["mqtt"]
		if not "host" in self._mqtt:
				raise ValueError("MQTT host not set")
		if not "port" in self._mqtt:
				raise ValueError("MQTT port not set")
		if not "user" in self._mqtt:
				raise ValueError("MQTT user not set")
		if not "password" in self._mqtt:
				raise ValueError("MQTT password not set")
		if not "topic" in self._mqtt:
				raise ValueError("MQTT topic not set")


	def _parse_vzlogger(self, config):
		"""Parse the vzlogger section of vzlogger2mqtt.yaml."""
		if "vzlogger" in config:
			self._vzlogger = config["vzlogger"]
		if not "host" in self._vzlogger:
				raise ValueError("vzlogger host not set")
		if not "port" in self._vzlogger:
				raise ValueError("vzlogger port not set")
		if not "devices" in self._vzlogger:
				raise ValueError("vzlogger devices not set")
		for item in self._vzlogger["devices"]:
			if not "uuid" in item:
				raise ValueError("Missing uuid for vzlogger device")
			if not "topic" in item:
				raise ValueError("Missing topic for vzlogger device")


	def mqtt(self):
		return self._mqtt

	def vzlogger(self):
		return self._vzlogger
