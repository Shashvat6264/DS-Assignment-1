from fastapi import APIRouter, Body, status

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
    
@router.post('/consume', response_description="Consume message")
async def consume(topic: str = Body(), consumer_id: int = Body()):
    message = await main_dq.dequeue(topic_name = topic, id = consumer_id)
    return generic_Response(data = {
        "status": "success",
        "message": message
    }, status_code = status.HTTP_200_OK)
    