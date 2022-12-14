import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received: ", str(message.payload.decode("utf-8")))

broker_address = "mqtt.eclipseprojects.io"

client = mqtt.Client("satgas")

topic = f"/Satgas/Covid"

print("connecting to broker")
client.connect(broker_address, port=1883)


print("Subscribing to topic", topic)
message = ""

while True:
    client.loop_start()
    client.on_message=on_message
    client.publish(topic, message)
    message = input()
    if message == 'exit':
        break
    