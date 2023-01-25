from .Topic import Topic
from .Consumer import generate_Consumer
from .Producer import generate_Producer
from .Message import Message
from .exceptions import *

from ..models import *

class DistributedQueue:
    def __init__(self, database = None):
        self.__database = database
        self.__topics = {}

    def loadPersistence(self):
        if self.__database is not None:
            topicList = self.__database.read(TopicModel)
            for topicInstance in topicList:
                self.__topics[topicInstance.name] = Topic.modelToObj(topicInstance, self.__database)
    
    async def createTopic(self, topic_name: str):
        self.__topics[topic_name] = Topic(topic_name, self.__database)
        await self.__topics[topic_name].save()
    
    async def listTopics(self) -> list:
        return list(self.__topics.keys())
    
    async def registerConsumer(self, topic_name: str) -> int:
        if self.__topics.get(topic_name) is None:
            raise TopicDoesNotExist(topic=topic_name, message="Requested Topic Name does not exist")
        consumer = await generate_Consumer(database=self.__database)
        await self.__topics[topic_name].addConsumer(consumer)
        return consumer.getId()
        
    async def registerProducer(self, topic_name: str) -> int:
        if self.__topics.get(topic_name) is None:
            await self.createTopic(topic_name)
        producer = await generate_Producer(database=self.__database)
        await self.__topics[topic_name].addProducer(producer)
        return producer.getId()
    
    async def enqueue(self, topic_name: str, id: int, message: str):
        msg = Message(message)
        await msg.save(self.__database)
        await self.__topics[topic_name].pushMessage(id, msg)
    
    async def dequeue(self, topic_name: str, id: int) -> str:
        message = await self.__topics[topic_name].popMessage(id)
        return message.getMessage()
        
    async def size(self, topic_name: str, id: int) -> int:
        return await self.__topics[topic_name].getSize(id)
    
    