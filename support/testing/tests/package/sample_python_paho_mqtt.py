from paho.mqtt import publish, subscribe

publish.single(
        'mikoos/test',
        payload="Hello, World!",
        qos=2,
        retain=True,
        hostname="localhost",
        port=1883)

message = subscribe.simple('mikoos/test')
print(message.payload.decode())
