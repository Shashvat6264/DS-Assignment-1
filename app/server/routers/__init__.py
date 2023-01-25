from fastapi import APIRouter, Body, status
from .producer import router as producerRouter
from .consumer import router as consumerRouter

from ..system import main_dq
from ..utils import *

router = APIRouter()

@router.post('/topics')
async def createTopic(name: str = Body()):
    main_dq.createTopic(name)
    return generic_Response(data={
        "status": "success",
        "message": f"Topic '{name}' created successfully",
    }, status_code=status.HTTP_201_CREATED)
    
@router.get('/topics')
async def listTopics():
    topics = main_dq.listTopics()
    return generic_Response(data={
        "status": "success",
        "topics": topics
    }, status_code=status.HTTP_200_OK)

@router.get('/size')
async def getSize(topic: str = Body(), consumer_id: int = Body()):
    topic_size = main_dq.size(topic, consumer_id)
    return generic_Response(data={
        "status": "success",
        "size": topic_size
    }, status_code=status.HTTP_200_OK)
    

router.include_router(consumerRouter, tags=["consumer"], prefix='/consumer')
router.include_router(producerRouter, tags=["producer"], prefix='/producer')
