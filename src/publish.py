import paho.mqtt.client as mqtt

from .env import BROKER_ADRESS

broker_address = BROKER_ADRESS
# broker_address="iot.eclipse.org" #use external broker

client = mqtt.Client("P1")  # create new instance

client.connect(broker_address)  # connect to broker

client.publish("house/main-light", "OFF")  # publish
