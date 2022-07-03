
import time
from umqttsimple import MQTTClient
import ssd1306
import ubinascii
import machine
from machine import Pin, SoftI2C
import micropython
import network
import json
import esp
esp.osdebug(None)
import gc
gc.collect()


# Usuario 1
# ssid = 'COMTECO-N3791960'
# password = 'CVGUZ50074'

ssid = 'COMTECO-N3791960'
password = 'CVGUZ50074'
mqtt_server = 'research.upb.edu'

port = '21212'

client_id = ubinascii.hexlify(machine.unique_id())

topic_sub = b'control'
topic_pub = b'forward'


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())