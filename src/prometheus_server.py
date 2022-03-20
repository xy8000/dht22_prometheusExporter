from prometheus_client import start_http_server, Gauge
from sensor_reader import read_sensor
from optparse import OptionParser
import random
import time
import os

#Parsing parameters
parser = OptionParser()
parser.add_option("-p", "--port", dest="port", help="Port of the HTTP-Server", type="int", default=8080)
parser.add_option("-g", "--pin", dest="gpio", help="gpio-data pin", type="int")
(options, args) = parser.parse_args()
port = options.port
gpio = options.gpio

# Preparing Gauges
g_humidity = Gauge('humidity', 'Humidity in percent')
g_temp = Gauge('temperature', 'Temperature in celsius')
g_humidity.set_function(lambda: read_sensor(gpio)["humidity"])
g_temp.set_function(lambda: read_sensor(gpio)["temperature"])


# Decorate function with metric.
def process_request(t):
	time.sleep(t)

if __name__ == '__main__':
	# Start up the server to expose the metrics.
	print(f'Starting Web-Server with port {port}, you may visit http://localhost:{port}/ to view metrics')
	print(f'Script will use GPIO-Pin: {gpio}.')
	start_http_server(port)
	# Generate some requests.
	while True:
		process_request(100)
