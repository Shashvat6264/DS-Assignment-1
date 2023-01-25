from .controllers import *

from .database import get_db, engine

from . import models

models.Base.metadata.create_all(bind=engine)

main_dq = DistributedQueue(database=get_db())
main_dq.loadPersistence()




