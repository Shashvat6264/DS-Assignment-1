import asyncio

from ..models import ConsumerModel

async def generate_Consumer(database = None):
    consumer = None
    if database is not None:
        instance = await database.create(ConsumerModel)
        consumer = Consumer(instance.id)
    return consumer

class Consumer:    
    def __init__(self, id):
        self.__id = id
        
    def getId(self) -> int:
        return self.__id
    
    def modelToObj(instance):
        consumer = Consumer(id=instance.id)
        return consumer