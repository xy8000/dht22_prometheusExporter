import Adafruit_DHT
import os

DHT_SENSOR = Adafruit_DHT.DHT22

# Will return a dictionary containing the humidity and temperature
def read_sensor(gpio_pin):
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, gpio_pin)

	if humidity is not None and temperature is not None:
		return {"humidity" : humidity,
				"temperature" :temperature}
	else:
		print(f'Failed to retrieve data from humidity sensor. Used GPIO-Pin {gpio_pin}')
