import requests
from .exceptions import *
from .utils import *

class Client:
    def __init__(self):
        self.broker = None
        self.topicIds = {}
    
    @convertToList
    def create_topic(self, topics):
        for topic in topics:
            registerResponse = requests.post(self.broker + '/topics', json = {'name': topic})
            if registerResponse.status_code != 201:
                raise TopicAlreadyExists(registerResponse.json()["message"])
            
    def list_topics(self):
        response = requests.get(self.broker + '/topics')
        if response.status_code == 200:
            return response.json()["topics"]
        else:
            raise Exception(response.json()["message"])
    
    
    