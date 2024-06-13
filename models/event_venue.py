from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from _datetime import datetime 
from . import Base

class EventVenue(Base):
    __tablename__ = "event_venues"

    event_id = Column(Integer, ForeignKey("events.id"), primary_key=True)
    venue_id = Column(Integer, ForeignKey("venues.id"), primary_key=True)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    event = relationship("Event", back_populates="event_venues")
    venue = relationship("Venue")

    def __repr__(self):
        return f"<EventVenue(event_id={self.event_id}, venue_id={self.venue_id})>"
