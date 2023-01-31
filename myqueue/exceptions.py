class UnauthorizedException(Exception):
    "When the topic access is unauthorized"
    def __init__(self, message: str) -> None:
        super().__init__(message)
        
class TopicDoesNotExist(Exception):
    "When topic does not exist"
    def __init__(self, message: str) -> None:
        super().__init__(message)
        
class TopicAlreadyExists(Exception):
    "When topic already exists"
    def __init__(self, message: str) -> None:
        super().__init__(message)
        
class QueueEmpty(Exception):
    "When the queue is empty but pop is initiated"
    def __init__(self, message: str) -> None:
        super().__init__(message)

class AlreadyRegistered(Exception):
    "When Client is already registered for a topic"
    def __init__(self, message: str) -> None:
        super().__init__(message)