from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class MessageModel(Base):
    __tablename__ = "message"
    
    id = Column(Integer, primary_key=True, index=True)
    index = Column(Integer, index=True)
    message = Column(String, index=True)
    topic_id = Column(Integer, ForeignKey("topic.id"))
    
    topic = relationship("TopicModel", back_populates="messages")