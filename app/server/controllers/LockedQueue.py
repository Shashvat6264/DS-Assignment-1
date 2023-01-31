from .Queue import Queue
from .Message import Message
from .exceptions import *
import asyncio


class LockedQueue(Queue):
    def __init__(self):
        super().__init__()
        self.__lock = asyncio.Lock()
        
    async def push(self, message: Message) -> int:
        await self.__lock.acquire()
        id = super().push(message)
        self.__lock.release()
        return id
        
    async def pop(self) -> Message:
        await self.__lock.acquire()
        if self.isEmpty():
            self.__lock.release()
            raise QueueEmpty(message="Queue is empty")
        message = super().pop()
        self.__lock.release()
        return message
    
    async def size(self) -> int:
        await self.__lock.acquire()
        size = super().size()
        self.__lock.release()
        return size