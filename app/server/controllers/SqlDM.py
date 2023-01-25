from .DatabaseManager import DatabaseManager    
import asyncio

class SqlDM(DatabaseManager):
    def __init__(self, db):
        super().__init__()
        self.__db = db
        self.__locks = {}
        
    async def create(self, model, **kwargs):
        if self.__locks.get(model.__name__) is None:
            self.__locks[model.__name__] = asyncio.Lock()
        await self.__locks[model.__name__].acquire()
        instance = model(**kwargs)
        self.__db.add(instance)
        self.__db.commit()
        self.__db.refresh(instance)
        self.__locks[model.__name__].release()
        return instance
        
    def read(self, model):
        return self.__db.query(model)
    
    def getById(self, model, id):
        return self.__db.query(model).filter(model.id == id).first()
    
    async def updateById(self, model, modelId, **kwargs):
        if self.__locks.get(model.__name__) is None:
            self.__locks[model.__name__] = asyncio.Lock()
        await self.__locks[model.__name__].acquire()
        instance = self.getById(model, modelId)
        for var, value in kwargs.items():
            setattr(instance, var, value) if value else None
        self.__db.add(instance)
        self.__db.commit()
        self.__db.refresh(instance)
        self.__locks[model.__name__].release()
        return instance
    
    async def deleteById(self, model, id):
        if self.__locks.get(model.__name__) is None:
            self.__locks[model.__name__] = asyncio.Lock()
        await self.__locks[model.__name__].acquire()
        instance = self.getById(model, id)
        self.__db.delete(instance)
        self.__db.commit()
        self.__locks[model.__name__].release()