import requests
from .client import Client
from .exceptions import *
from .utils import *

class Consumer(Client):
    def __init__(self, topics, broker):
        super().__init__()
        self.broker = broker
        self.register(topics)
    
    @convertToList
    def register(self, topics):
        for topic in topics:
            if topic in self.topicIds.keys():
                raise AlreadyRegistered('Consumer has already registered for topic: ' + topic)
            registerResponse = requests.post(self.broker + '/consumer/register', json = {'topic': topic})
            if registerResponse.status_code == 200:
                self.topicIds[topic] = registerResponse.json()['consumer_id']
            else:
                raise TopicDoesNotExist(registerResponse.json()["message"])
            
    @convertToList
    def dequeue(self, topics):
        responses = []
        for topic in topics:
            if topic not in self.topicIds.keys():
                raise UnauthorizedException("This consumer is not authorized to pull messages from topic: " + topic)
            dequeueResponse = requests.get(self.broker + '/consumer/consume', params = {'topic': topic, 'consumer_id': self.topicIds[topic]})
            if dequeueResponse.status_code == 200:
                responses.append(dequeueResponse.json()["message"])
            elif dequeueResponse.status_code == 401:
                raise UnauthorizedException(dequeueResponse.json()["message"])
            else:
                raise Exception(dequeueResponse.json()["message"])
        return responses
            
    def get_size(self, topic):
        if topic not in self.topicIds.keys():
            raise UnauthorizedException("This consumer is not authorized to pull messages from topic: " + topic)
        sizeResponse = requests.get(self.broker + "/size", params = {"topic":topic, "consumer_id": self.topicIds[topic]})
        if sizeResponse.status_code == 200:
            return sizeResponse.json()["size"]
        elif sizeResponse.status_code == 401:
            raise UnauthorizedException(sizeResponse.json()["message"])
        else:
            raise TopicDoesNotExist(sizeResponse.json()["message"])
                
    def can_dequeue(self, topic):
        curr_size = self.get_size(topic)
        if curr_size == None or curr_size == 0:
            return False
        return True
        