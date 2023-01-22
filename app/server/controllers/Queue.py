from .Message import Message

class Queue:
    def __init__(self):
        self.__queue = []
        
    def push(self, message: Message):
        self.__queue.push(message)
        return
        
    def pop(self) -> Message:
        message = self.__queue[0]
        self.__queue.pop(0)
        return message
    
    def peek(self) -> Message:
        return self.__queue[0]
    
    def size(self) -> int:
        return len(self.__queue)
    
    def isEmpty(self) -> bool:
        return len(self.__queue) == 0