import requests

class Producer:
    broker = None
    topics = None
    topicIDs = []
    
    def __init__(self, topics, broker):
        self.topics = topics
        self.broker = broker
        for topic in topics:
            registerResponse = requests.post(broker + '/register', data = {'topic': topic}).json()
            print(registerResponse)

        