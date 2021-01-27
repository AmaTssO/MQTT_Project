import paho.mqtt.client as paho
import sys
import bmpsensor
import time
 
client = paho.Client()

if client.connect("mojito.homedruon.com",1883,60)!=0:
    print("no connexion")
    sys.exit(-1)
    
while True:
    temp, pressure, altitude = bmpsensor.readBmp180()
    print("Temperature is ",temp)  # degC
    print("Pressure is ",pressure) # Pressure in Pa 
    print("Altitude is ",altitude) # Altitude in meters
    print("\n")
    client.publish("DataInfo",temp,0)
    time.sleep(2)
    
client.disconnect()