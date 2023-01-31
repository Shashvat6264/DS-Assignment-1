from .LockedQueue import LockedQueue
from .Consumer import Consumer
from .Producer import Producer
from .Message import Message
from .exceptions import *

from ..models import *

class Topic:
    def __init__(self, topic_name: str, database=None):
        self.__name = topic_name
        self.__dbId = None
        self.__database = database
        self.__producers = {}
        self.__consumers = {}
        self.__queue = LockedQueue()
        
    async def save(self):
        if self.__database is not None:
            self.__dbId = await self.__database.create(TopicModel, name=self.__name)
            self.__dbId = self.__dbId.id
    
    async def addConsumer(self, consumer: Consumer):
        self.__consumers[consumer.getId()] = consumer
        if self.__database is not None:
            topicInstance = self.__database.getById(TopicModel, self.__dbId)
            topicInstance.consumers.append(self.__database.getById(ConsumerModel, consumer.getId()))
            await self.__database.updateById(TopicModel, self.__dbId, consumers=topicInstance.consumers)
            
    async def addProducer(self, producer: Producer):
        self.__producers[producer.getId()] = producer
        producer.setTopic(self)
        if self.__database is not None:
            topicInstance = self.__database.getById(TopicModel, self.__dbId)
            producerInstance = self.__database.getById(ProducerModel, producer.getId())
            topicInstance.producers.append(producerInstance)
            producerInstance.topic_id = topicInstance.id
            await self.__database.updateById(ProducerModel, producer.getId(), topic_id=producerInstance.topic_id)
            await self.__database.updateById(TopicModel, self.__dbId, producers=topicInstance.producers)
                    
    def __authorizeConsumer(self, id: int) -> bool:
        print(self.__consumers.keys())
        if self.__consumers.get(id) is not None:
            return True
        else:
            return False
    
    def __authorizeProducer(self, id: int) -> bool:
        if self.__producers.get(id) is not None:
            return True
        else:
            return False
    
    async def pushMessage(self, id: int, message: Message):
        if not self.__authorizeProducer(id):
            raise UnauthorizedException(message="Producer not authorized to add message to this topic")
        index = await self.__queue.push(message)
        if self.__database is not None:
            topicInstance = self.__database.getById(TopicModel, self.__dbId)
            messageInstance = self.__database.getById(MessageModel, message.getId())
            topicInstance.messages.append(messageInstance)
            messageInstance.index = index
            messageInstance.topic_id = topicInstance.id
            await self.__database.updateById(MessageModel, message.getId(), index=messageInstance.index, topic_id=messageInstance.topic_id)
            await self.__database.updateById(TopicModel, self.__dbId, messages=topicInstance.messages)
    
    async def popMessage(self, id: int):
        if not self.__authorizeConsumer(id):
            raise UnauthorizedException(message="Consumer is not authorized to consume message of this topic")
        message = await self.__queue.pop()
        if self.__database is not None:
            await self.__database.deleteById(MessageModel, message.getId())
        return message
    
    async def getSize(self, id: int):
        if not self.__authorizeConsumer(id):
            raise UnauthorizedException(message="Consumer is not subscribed to this topics")
        return self.__queue.size()
    
    def modelToObj(instance, database):
        topic = Topic(topic_name=instance.name)
        topic.__dbId = instance.id
        for producerInstance in instance.producers:
            producer = Producer.modelToObj(producerInstance)
            topic.__producers[producer.getId()] = producer
            producer.setTopic(topic)
        
        for consumerInstance in instance.consumers:
            consumer = Consumer.modelToObj(consumerInstance)
            topic.__consumers[consumer.getId()] = consumer
        
        sorted(instance.messages, key=lambda x: x.index)
        messageList = []
        for messageInstance in instance.messages:
            message = Message.modelToObj(messageInstance)
            messageList.append(message)
        
        topic.__queue.inject(messageList)
        topic.__database = database
        return topic
    
    