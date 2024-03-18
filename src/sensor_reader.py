import adafruit_dht
import os
import board
import time

# Changing pin caused errors. Falling back to hardcoded pin therefore.
dht_device = adafruit_dht.DHT22(board.D4)

# Will return a dictionary containing the humidity and temperature
def read_sensor():
	#dht_device = adafruit_dht.DHT22(board.D4)
	humidity = dht_device.humidity
	temperature = dht_device.temperature
	#dht_device.exit()

	if humidity is not None and temperature is not None:
		return {
			"humidity" : humidity,
			"temperature" :temperature
			}
	else:
		print(f'Failed to retrieve data from humidity sensor. Used GPIO-Pin {gpio_pin}')
