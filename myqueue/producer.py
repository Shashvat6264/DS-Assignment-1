import requests
from .client import Client

class Producer(Client):
    def __init__(self, topics, broker):
        self.broker = broker
        self.register(topics)
        
    def register(self, topics): 
        for topic in topics:
            registerResponse = requests.post(self.broker + '/producer/register', data = {'topic': topic})
            if registerResponse.status_code == 200:
                self.topics.append(topic)
                self.topicIDs[topic] = registerResponse.json()['producer_id']
            else:
                print(registerResponse.json()["message"])
                
    def enqueue(self, topics, message):
        for topic in topics:
            enqueueResponse = requests.post(self.broker + '/producer/produce', data = {'topic': topic, 'producer_id': self.topicIDs[topic], 'message': message})
            if enqueueResponse.status_code == 200:
                print("Message enqueued successfully")
            else :
                print(enqueueResponse.json()["message"])
        