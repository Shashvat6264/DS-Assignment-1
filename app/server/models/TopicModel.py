from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from ..database import Base

consumer_association_table = Table(
    "consumer_association_table",
    Base.metadata,
    Column("topic", ForeignKey("topic.id")),
    Column("consumer", ForeignKey("consumer.id")),
)

class TopicModel(Base):
    __tablename__ = "topic"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer, unique=True, index=True)

    producers = relationship("ProducerModel", back_populates="topic")
    messages = relationship("MessageModel", back_populates="topic")
    
    consumers = relationship("ConsumerModel", secondary=consumer_association_table, back_populates="topics")
    