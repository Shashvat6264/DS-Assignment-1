from fastapi import APIRouter, Body, status, Query
from .producer import router as producerRouter
from .consumer import router as consumerRouter

from ..system import main_dq
from ..utils import *

router = APIRouter()

@router.post('/topics')
async def createTopic(topic_name: str = Body(..., embed=True)):
    await main_dq.createTopic(topic_name)
    return generic_Response(data={
        "status": "success",
        "message": f"Topic '{topic_name}' created successfully",
    }, status_code=status.HTTP_201_CREATED)
    
@router.get('/topics')
async def listTopics():
    topics = await main_dq.listTopics()
    return generic_Response(data={
        "status": "success",
        "topics": topics
    }, status_code=status.HTTP_200_OK)

@router.get('/size')
async def getSize(topic: str = Query(default=...), consumer_id: int = Query(default=...)):
    topic_size = await main_dq.size(topic, consumer_id)
    return generic_Response(data={
        "status": "success",
        "size": topic_size
    }, status_code=status.HTTP_200_OK)
    

router.include_router(consumerRouter, tags=["consumer"], prefix='/consumer')
router.include_router(producerRouter, tags=["producer"], prefix='/producer')
