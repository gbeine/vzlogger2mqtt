
import time

from vzlogger2mqtt import mqtt
from vzlogger2mqtt import vzlogger

class Daemon:

	def __init__(self, config):
		self._config = config
		self._init_mqtt()
		self._init_vzlogger()

	def run(self):
		while True:
			self._vzlogger.update_and_publish(self._mqtt)
			time.sleep(5)

	def _init_mqtt(self):
		self._mqtt = mqtt.Mqtt(self._config.mqtt())
		self._mqtt.connect()

	def _init_vzlogger(self):
		self._vzlogger = vzlogger.vzlogger(self._config.vzlogger())
