class UnauthorizedException(Exception):
    "When Enqueue or Dequeue is unauthorized"
    def __init__(self, message: str) -> None:
        super().__init__(message)
        
class TopicDoesNotExist(Exception):
    "When topic does not exist"
    def __init__(self, topic: str, message: str) -> None:
        message += " -> Topic Name: " + topic
        super().__init__(message)
        
class QueueEmpty(Exception):
    "When the queue is empty but pop is initiated"
    def __init__(self, message: str) -> None:
        super().__init__(message)