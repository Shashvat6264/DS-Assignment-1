from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

from .TopicModel import consumer_association_table

class ConsumerModel(Base):
    __tablename__ = "consumer"
    
    id = Column(Integer, primary_key=True, index=True)
    
    topics = relationship("TopicModel", secondary=consumer_association_table, back_populates="consumers")
    