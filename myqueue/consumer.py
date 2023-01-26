import requests
from .client import Client

class Consumer(Client):
    
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
                
    def dequeue(self, topics):
        for topic in topics:
            dequeueResponse = requests.post(self.broker + '/consumer/consume', data = {'topic': topic, 'consumer_id': self.topicIDs[topic]})
            if dequeueResponse.status_code == 200:
                return dequeueResponse.json()["message"]
            else :
                print(dequeueResponse.json()["message"])
                return None
            
    def get_size(self, topic):
        sizeResponse = requests.get(self.broker + "/size", data = {"topic":topic, "consumer_id": self.topicIds[topic]})
        if sizeResponse.status_code == 200:
            return sizeResponse.json()["size"]
        else:
            print(sizeResponse.json()["message"])
            return None
                
    
    def can_dequeue(self, topic):
        curr_size = self.get_size(topic)
        if curr_size == None:
            return False
        return True
        