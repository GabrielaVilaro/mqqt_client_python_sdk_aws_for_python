import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT


class MqttConnect:

    def __init__(self, endpoint, client_id, path_to_cert, path_to_key, path_to_root, message, topic):
        self.endpoint = endpoint  # "customEndpointUrl"
        self.client_id = client_id  # "testDevice"
        self.path_to_cert = path_to_cert  # "certificates/a1b23cd45e-certificate.pem.crt"
        self.path_to_key = path_to_key  # "certificates/a1b23cd45e-private.pem.key"
        self.path_to_root = path_to_root  # "certificates/root.pem"
        self.message = message  # "Hello World"
        self.topic = topic  # "test/testing"
        self.myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(self.client_id)

    def connection(self):
        # endpoint and port
        self.myAWSIoTMQTTClient.configureEndpoint(self.endpoint, 8883)
        self.myAWSIoTMQTTClient.configureCredentials(self.path_to_root, self.path_to_key, self.path_to_cert)
        self.myAWSIoTMQTTClient.connect()

    def publish_message(self):
        print('Begin Publish')
        data = self.message
        self.message = {"message": data}
        self.myAWSIoTMQTTClient.publish(self.topic, json.dumps(self.message), 1)
        print("Published: '" + json.dumps(self.message) + "' to the topic: " + "'test/testing'")
        t.sleep(0.1)
        print('Publish End')

        # disconnect
        self.myAWSIoTMQTTClient.disconnect()
