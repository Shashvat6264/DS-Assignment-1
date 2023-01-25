from .Message import Message
from .exceptions import *

class Queue:
    def __init__(self):
        self.__queue = []
        
    def inject(self, queue):
        self.__queue = queue.copy()
        
    def push(self, message: Message) -> int:
        self.__queue.append(message)
        return len(self.__queue) - 1
        
    def pop(self) -> Message:
        if self.isEmpty():
            raise QueueEmpty(message="Queue is empty")
        message = self.__queue[0]
        self.__queue.pop(0)
        return message
    
    def peek(self) -> Message:
        if self.isEmpty():
            raise QueueEmpty(message="Queue is empty")
        return self.__queue[0]
    
    def size(self) -> int:
        return len(self.__queue)
    
    def isEmpty(self) -> bool:
        return len(self.__queue) == 0