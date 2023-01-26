import requests

class Client:
    topics = []
    broker = None
    topicIds = {}
    
    def create_topic(self, topics):
        self.topics.extend(topics)
        for topic in topics:
            registerResponse = requests.post(self.broker + '/topics', data = {'topic': topic})
            print(registerResponse.json()["message"])
            
    def list_topics(self):
        topics = requests.get(self.broker + '/topics')
        if topics.status_code == 200:
            return topics.json()["topics"]
        else: 
            print(topics.json()["message"])
        return None
    
    
    