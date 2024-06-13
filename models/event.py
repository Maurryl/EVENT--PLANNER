from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from _datetime import datetime 
from . import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    date = Column(DateTime)
    location = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    event_guests = relationship("EventGuest", back_populates="event")
    event_venues = relationship("EventVenue", back_populates="event")

    def __repr__(self):
        return f"<Event(name='{self.name}', date='{self.date}')>"
