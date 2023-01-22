class Producer:
    genId = 0
    
    def __init__(self):
        self.__id = genId
        genId += 1
        
        
    def getId(self) -> int:
        return self.__id