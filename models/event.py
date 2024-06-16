# models/event.py

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from . import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    date = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)

    # Define relationship to EventGuest
    event_guests = relationship("EventGuest", back_populates="event")

    # Define relationship to EventVenue
    event_venues = relationship("EventVenue", back_populates="event")

    def __repr__(self):
        return f"<Event(id={self.id}, name={self.name}, date={self.date}, location={self.location})>"
