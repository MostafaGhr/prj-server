import paho.mqtt.client as mqtt

import threading
import json

from trashcan.models import Occupancy, DoorUsage, Can


client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    client.subscribe('trashcan/+/door')  #trashcan/ID/door  ==> {"id":1}
    client.subscribe('trashcan/+/internal_status')  #trashcan/ID/internal_status  ==> {"id":1, "percentage":72}

    client.message_callback_add('trashcan/+/door', door_open)
    client.message_callback_add('trashcan/+/internal_status', internal_status)

    print("Connected with result code "+str(rc))

def on_disconnect(client, userdata, rc):
    print("disconnecting reason  "  +str(rc))

def on_log(client, userdata, level, buf):
    print("#### mqtt log: ",buf)

def door_open(client, userdata, message):
    try:
        payload = json.loads(message.payload)
    except Exception:
        print("Error in parsing json message")
        return False

    DoorUsage(can=Can.objects.get(id=payload['id'])).save()
    print('door_open recieved')

def internal_status(client, userdata, message):
    try:
        payload = json.loads(message.payload)
    except Exception:
        print("Error in parsing json message")
        return False

    Occupancy(can=Can.objects.get(id=payload['id']), percentage=payload['percentage']).save()
    print('percentage recieved')

client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.connect('mqtt.dev.eganje.com')
# threading.Thread(target=client.loop_forever(), args=[], daemon=True).start()