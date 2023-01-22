from .Topic import Topic
from .Consumer import Consumer
from .Producer import Producer
from .Message import Message
from .exceptions import *

class DistributedQueue:
    def __init__(self, database = None):
        self.__database = database
        self.__topics = {}
        
    def createTopic(self, topic_name: str):
        self.__topics[topic_name] = Topic(topic_name, self.__database)
    
    def listTopics(self) -> list:
        return self.__topics.keys()
    
    def registerConsumer(self, topic_name: str) -> int:
        consumer = Consumer()
        self.__topics[topic_name].addConsumer(consumer)
        return consumer.getId()
        
    def registerProducer(self, topic_name: str) -> int:
        producer = Producer()
        self.__topics[topic_name].setProducer(producer)
        return producer.getId()
    
    def enqueue(self, topic_name: str, id: int, message: str):
        try:
            msg = Message(message)
            self.__topics[topic_name].pushMessage(id, msg)
        except UnauthorizedException as error:
            print(error)
    
    def dequeue(self, topic_name: str, id: int) -> str:
        try:
            self.__topics[topic_name].popMessage(id)
        except UnauthorizedException as error:
            print(error)
    
    def size(self, topic_name: str) -> int:
        return self.__topics[topic_name].getSize()
    
    