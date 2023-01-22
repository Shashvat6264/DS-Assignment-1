class Message:
    def __init__(self, message) -> None:
        self.__message = message
        
    def getMessage(self):
        return self.__message