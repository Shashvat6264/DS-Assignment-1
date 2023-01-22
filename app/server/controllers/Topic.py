from .Queue import Queue
from .Consumer import Consumer
from .Producer import Producer
from .Message import Message
from .exceptions import *

class Topic:
    def __init__(self, topic_name: str, database):
        self.__name = topic_name
        self.__database = database
        self.__producer = None
        self.__consumers = {}
        self.__queue = Queue()
    
    def addConsumer(self, consumer: Consumer):
        self.__consumers[consumer.getId()] = consumer
    
    def setProducer(self, producer: Producer):
        self.__producer = producer
        
    def __authorizeConsumer(self, id: int) -> bool:
        if self.__consumers.get(id) is not None:
            return True
        else:
            return False
    
    def __authorizeProducer(self, id: int) -> bool:
        return self.__producer.getId() == id
    
    def pushMessage(self, id: int, message: Message):
        if not self.__authorizeProducer(id):
            raise UnauthorizedException(message="Producer not authorized to add message to this topic")
        self.__queue.push(message)
    
    def popMessage(self, id: int):
        if not self.__authorizeConsumer(id):
            raise UnauthorizedException(message="Consumer is not authorized to consumer message of this topic")
        return self.__queue.pop()
    
    def getSize(self):
        return self.__queue.size()
    
    