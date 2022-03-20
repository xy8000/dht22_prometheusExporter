# dht22_prometheusExporter
Repository to export the DHT22-metrics to prometheus with a raspberrypi

# Setup

## with python

Simply run this command to start the Server:
`python3 ./src/prometheus_server.py -p [SERVER_PORT] -g [GPIO_PIN]`

## with Docker

Simply run this command to start the Server: `docker build .`

## with Docker-Compose

[TBD]

# Requirements

## System

* May only run on **RaspberryPi**. Tested on V4 and V3

## Python

* prometheus_client
* Adafruit-DHT

full versions will be documented here: [requirements.txt](./requirements.txt)

## Dockerfile
* Image [python](https://hub.docker.com/_/python/)
* The container should have access to the GPIO

# Troubleshooting

## Timeout reading GPIO:

* Log will contain `_bake_output`
* Check Sensor-Connection

Log-Example:
```File "/usr/lib/python3.7/wsgiref/handlers.py", line 137, in run
    self.result = application(self.environ, self.start_response)
  File "/usr/local/lib/python3.7/dist-packages/prometheus_client/exposition.py", line 118, in prometheus_app
    status, header, output = _bake_output(registry, accept_header, params)
  File "/usr/local/lib/python3.7/dist-packages/prometheus_client/exposition.py", line 100, in _bake_output
    output = encoder(registry)
  File "/usr/local/lib/python3.7/dist-packages/prometheus_client/exposition.py", line 171, in generate_latest
    for metric in registry.collect():
  File "/usr/local/lib/python3.7/dist-packages/prometheus_client/registry.py", line 83, in collect
    yield from collector.collect()
  File "/usr/local/lib/python3.7/dist-packages/prometheus_client/metrics.py", line 92, in collect
    for suffix, labels, value, timestamp, exemplar in self._samples():
  File "/usr/local/lib/python3.7/dist-packages/prometheus_client/metrics.py", line 211, in _samples
    return self._child_samples()
  File "/usr/local/lib/python3.7/dist-packages/prometheus_client/metrics.py", line 417, in samples
    return (Sample('', {}, float(f()), None, None),)
  File "./src/prometheus_server.py", line 19, in <lambda>
    g_humidity.set_function(lambda: read_sensor(gpio)["humidity"])```

## Cannot read GPIO
* Log will contain `RuntimeError: Error accessing GPIO`
* Check GPIO access (user-privileges)

Log-Example:
```Traceback (most recent call last):
  File "/usr/lib/python3.7/wsgiref/handlers.py", line 137, in run
    self.result = application(self.environ, self.start_response)
  File "/home/sshuser/.local/lib/python3.7/site-packages/prometheus_client/exposition.py", line 118, in prometheus_app
    status, header, output = _bake_output(registry, accept_header, params)
  File "/home/sshuser/.local/lib/python3.7/site-packages/prometheus_client/exposition.py", line 100, in _bake_output
    output = encoder(registry)
  File "/home/sshuser/.local/lib/python3.7/site-packages/prometheus_client/exposition.py", line 171, in generate_latest
    for metric in registry.collect():
  File "/home/sshuser/.local/lib/python3.7/site-packages/prometheus_client/registry.py", line 83, in collect
    yield from collector.collect()
  File "/home/sshuser/.local/lib/python3.7/site-packages/prometheus_client/metrics.py", line 92, in collect
    for suffix, labels, value, timestamp, exemplar in self._samples():
  File "/home/sshuser/.local/lib/python3.7/site-packages/prometheus_client/metrics.py", line 211, in _samples
    return self._child_samples()
  File "/home/sshuser/.local/lib/python3.7/site-packages/prometheus_client/metrics.py", line 417, in samples
    return (Sample('', {}, float(f()), None, None),)
  File "./src/prometheus_server.py", line 19, in <lambda>
    g_humidity.set_function(lambda: read_sensor(gpio)["humidity"])
  File "/home/sshuser/git_repos/dht22_prometheusExporter/src/sensor_reader.py", line 8, in read_sensor
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, gpio_pin)
  File "/home/sshuser/.local/lib/python3.7/site-packages/Adafruit_DHT/common.py", line 94, in read_retry
    humidity, temperature = read(sensor, pin, platform)
  File "/home/sshuser/.local/lib/python3.7/site-packages/Adafruit_DHT/common.py", line 81, in read
    return platform.read(sensor, pin)
  File "/home/sshuser/.local/lib/python3.7/site-packages/Adafruit_DHT/Raspberry_Pi_2.py", line 34, in read
    raise RuntimeError('Error accessing GPIO.')
RuntimeError: Error accessing GPIO.```
