import paho.mqtt.client as mqtt  # import the client1
import time

from .services import mongo

from .env import BROKER_ADRESS


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

    mongo.test.mqttpy.insert_one({message.topic: str(message.payload.decode("utf-8"))})



broker_address = BROKER_ADRESS
# broker_address="iot.eclipse.org"
print("creating new instance")
# client = mqtt.Client("P1") #create new instance
client = mqtt.Client("P1", True, None, mqtt.MQTTv31)
client.on_message = on_message  # attach function to callback
print("connecting to broker")
client.connect(broker_address)  # connect to broker

client.loop_start()  # start the loop
print("Subscribing to topic", "COVID-19/mortes/BR")
client.subscribe("COVID-19/mortes/BR")

print("Publishing message to topic", "COVID-19/mortes/BR")
client.publish("COVID-19/mortes/BR", "1")

print("Publishing message to topic", "COVID-19/mortes/BR")
client.publish("COVID-19/mortes/BR", "2")

time.sleep(4)  # wait
client.loop_stop()  # stop the loop
