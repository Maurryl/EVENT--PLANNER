from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from _datetime import datetime 
from . import Base

class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    capacity = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Venue(name='{self.name}', address='{self.address}')>"
