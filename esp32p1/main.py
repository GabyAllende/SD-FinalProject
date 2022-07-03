
def sub_cb(topic, msg):
  global client_id
  print("Topico , mensaje")
  print((topic, msg))
  mensaje_rcv = json.loads(msg)
  
  oled_width = 128
  oled_height = 64
  
  i2c_rst = Pin(16, Pin.OUT)
  i2c_rst.value(0)
  time.sleep_ms(5)
  i2c_rst.value(1) 
  # Setup the I2C lines
  i2c_scl = Pin(15, Pin.OUT)
  i2c_sda = Pin(4, Pin.OUT)
  # Create the bus object
  i2c = SoftI2C(scl=i2c_scl, sda=i2c_sda)
  # Create the display object
  oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
  
  oled.text('ID: ' ,0,0)
  oled.text(mensaje_rcv['ID'], 70, 0)
  oled.text('Owner: ' ,0,10)
  oled.text(mensaje_rcv['Owner'], 0, 20)
  
  oled.show()


def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub , port
  client = MQTTClient(client_id, mqtt_server ,port=port,keepalive=60)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(5)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

global client_id, topic_sub
while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      msg = {"ID": client_id}
      msg_json = json.dumps(msg)
      client.publish(topic_pub, msg_json)
      last_message = time.time()
      counter += 1

  except OSError as e:
    restart_and_reconnect()