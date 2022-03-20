# dht22_prometheusExporter
Repository to export the DHT22-metrics to prometheus with a raspberrypi

# Setup

## with python
Simply run this command to start the Server:
`python3 ./src/prometheus_server.py -p [SERVER_PORT] -g [GPIO_PIN]`

## with Docker
Simply run this command to start the Server:
`docker build .`

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
