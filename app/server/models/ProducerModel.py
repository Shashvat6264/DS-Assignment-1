from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class ProducerModel(Base):
    __tablename__ = "producer"
    
    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topic.id"))
    
    topic = relationship("TopicModel", back_populates="producers")