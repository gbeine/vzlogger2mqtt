
import json
import urllib.request

class vzlogger:

	def __init__(self, config):
		self._config = config
		self._init_devices()
		self._init_url()


	def update_and_publish(self, mqtt):
		data = self._update()

		mqtt.publish("version", data["version"])
		mqtt.publish("generator", data["generator"])
		for uuid, values in data["data"].items():
			topic = self._devices[uuid]
			mqtt.publish(topic + "/timestamp", values[0])
			mqtt.publish(topic, values[1])

	def _init_devices(self):
		self._devices = {}
		for item in self._config["devices"]:
			if not "uuid" in item:
				raise ValueError("Missing uuid for vzlogger device")
			if not "topic" in item:
				raise ValueError("Missing topic for vzlogger device")
			self._devices[item["uuid"]] = item["topic"]


	def _init_url(self):
		self._url = "http://{}:{}".format(self._config["host"], self._config["port"])


	def _update(self):
		json = self._fetch_json()

		data = {}

		if not "version" in json:
			raise ValueError("Missing version in vzlogger data")
		if not "generator" in json:
			raise ValueError("Missing generator in vzlogger data")
		if not "data" in json:
			raise ValueError("Missing vzlogger data")

		data["version"] = json["version"]
		data["generator"] = json["generator"]
		data["data"] = {}

		for item in json["data"]:
			if not "uuid" in item:
				continue
			if not "tuples" in item:
				continue
				
			data["data"][item["uuid"]] = item["tuples"][0]

		return data


	def _fetch_json(self):
		request = urllib.request.urlopen(self._url)
		return json.loads(request.read().decode())
