from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from _datetime import datetime 
from . import Base

class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    phone = Column(String)

    created_at = Column(DateTime, default=datetime.now)

    event_guests = relationship("EventGuest", back_populates="guest")

    def __repr__(self):
        return f"<Guest(name='{self.name}', email='{self.email}')>"
