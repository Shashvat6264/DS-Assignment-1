from fastapi import APIRouter, Body, status, Query

from ..system import main_dq
from ..utils import *

router = APIRouter()

@router.post('/register', response_description="Register Consumer")
async def register(topic: str = Body()):
    customer_id = await main_dq.registerConsumer(topic)
    return generic_Response(data = {
        "status": "success",
        "consumer_id": customer_id
    }, status_code = status.HTTP_200_OK)
    
@router.get('/consume', response_description="Consume message")
async def consume(topic: str = Query(default=...), consumer_id: int = Query(default=...)):
    message = await main_dq.dequeue(topic_name = topic, id = consumer_id)
    return generic_Response(data = {
        "status": "success",
        "message": message
    }, status_code = status.HTTP_200_OK)
    