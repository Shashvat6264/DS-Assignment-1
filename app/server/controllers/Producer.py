import asyncio

from ..models import ProducerModel

async def generate_Producer(database = None):
    producer = None
    if database is not None:
        instance = await database.create(ProducerModel)
        producer = Producer(instance.id)
    return producer

class Producer:
    genId = 0
    lock = asyncio.Lock()
    
    def __init__(self, id):
        self.__topic = None
        self.__id = id
        
    def setTopic(self, topic):
        self.__topic = topic        
        
    def getId(self) -> int:
        return self.__id
    
    def modelToObj(instance):
        producer = Producer(id=instance.id)
        return producer