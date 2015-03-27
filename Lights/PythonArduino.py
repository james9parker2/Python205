import mosquitto
client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1")

client.subscribe("simon/test")

def messageReceived(broker, obj, msg):
global client
print("Message " + msg.topic + " containing: " + msg.payload)

client = None

client.on_message = messageReceived


while (client != None): client.loop()