#!/usr/bin/python
#Author: Florian Ströger

import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  /  Luftfeuchtigkeit={1:0.1f}%'.format(temperature, h$
else:
    print('Sensorfehler')
    sys.exit(1)
