'p4a example service using oscpy to communicate with main application.'
from random import sample, randint
from string import ascii_letters
from time import localtime, asctime, sleep
import paho.mqtt.client as mqtt

from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient

CLIENT = OSCClient('localhost', 3002)


def ping(*_):
    mqttBroker ="test.mosquitto.org"
    clientmqtt = mqtt.Client("Smartphone")
    try:
        clientmqtt.connect(mqttBroker, port=1883, keepalive=60)
        mqtt_status="connected"
    except:
        mqtt_status="Not connected"
    'answer to ping messages'
    CLIENT.send_message(
        b'/message',
        [
            ''.join(mqtt_status)
            .encode('utf8'),
        ],
    )


def send_date():
    'send date to the application'
    CLIENT.send_message(
        b'/date',
        [asctime(localtime()).encode('utf8'), ],
    )


if __name__ == '__main__':
    SERVER = OSCThreadServer()
    SERVER.listen('localhost', port=3000, default=True)
    SERVER.bind(b'/ping', ping)
    while True:
        sleep(1)
        send_date()
