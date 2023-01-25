from fastapi import APIRouter, Body, status

from ..system import *
from ..utils import *

router = APIRouter()

@router.post('/register', response_description="Register Producer")
async def register(topic: str = Body()):
    producer_id = await main_dq.registerProducer(topic)
    return generic_Response(data = {
        "status": "success",
        "producer_id": producer_id
    }, status_code = status.HTTP_200_OK)
    
@router.post('/produce', response_description="Produce message")
async def produce(topic: str = Body(), producer_id: int = Body(), message: str = Body()):
    await main_dq.enqueue(topic_name = topic, id = producer_id, message = message)
    return generic_Response(data={
        "status": "success",
    }, status_code = status.HTTP_200_OK)
    