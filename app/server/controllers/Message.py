from ..models import MessageModel

class Message:
    def __init__(self, message) -> None:
        self.__message = message
        
    async def save(self, database = None):
        if database is not None:
            self.__id = await database.create(MessageModel, message=self.__message)
            self.__id = self.__id.id
        
    def setId(self, id):
        self.__id = id
    
    def getMessage(self):
        return self.__message
    
    def getId(self):
        return self.__id
    
    def modelToObj(instance):
        message = Message(message=instance.message)
        message.setId(instance.id)
        return message