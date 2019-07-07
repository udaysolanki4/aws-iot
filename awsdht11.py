import paho.mqtt.client as mqtt
import ssl
import time
import random
import json
import Adafruit_DHT

rootca=r'C:\Users\AmazonRootCA1.pem.txt'  #add location address of root certificate
certificate=r'C:\Users\certificate.pem.crt'   #add location address of certificate
keyfile=r'C:\Users\private.pem.key'     #add location address of private key
c=mqtt.Client()
c.tls_set(rootca,certfile=certificate,keyfile=keyfile,cert_reqs=ssl.CERT_REQUIRED,
          tls_version=ssl.PROTOCOL_TLSv1_2,ciphers=None)

c.connect('dakdk23-northeast-1.amazonaws.com',8883) #http api

def onc(c,userdata,flags,rc):
    print("successfully connected to Amazon with RC",rc)

c.on_connect=onc

sensor = Adafruit_DHT.DHT11
sensor_pin = 4
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    m=json.dumps (dict (DateTime=45, Temperature=temperature, Moisture=humidity))

    c.publish("mytopic/iot1",m)
    time.sleep(1)


c.loop_forever()


