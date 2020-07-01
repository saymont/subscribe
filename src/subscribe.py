import paho.mqtt.client as mqtt
import time
import os
import json

from .services import mongo

from .env import BROKER_ADDRESS


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with Broker")
    else:
        print("Connection fail")


def on_message(client, userdata, message):
    data = json.loads(message.payload)
    print(data)
    mongo.test.mqttpy.insert_one(data)

broker_address = BROKER_ADDRESS

print("creating new instance")
client = mqtt.Client("P1", True, None, mqtt.MQTTv31)
client.on_connect = on_connect
client.on_message = on_message

print("connecting to broker")
client.connect(broker_address)


print("Subscribing to topic", "trabalhoSD")
client.subscribe("trabalhoSD")


client.loop_forever()
