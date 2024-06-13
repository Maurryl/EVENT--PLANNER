from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from _datetime import datetime 
from . import Base

class EventGuest(Base):
    __tablename__ = "event_guests"

    event_id = Column(Integer, ForeignKey("events.id"), primary_key=True)
    guest_id = Column(Integer, ForeignKey("guests.id"), primary_key=True)
    rsvp = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    event = relationship("Event", back_populates="event_guests")
    guest = relationship("Guest", back_populates="event_guests")

    def __repr__(self):
        return f"<EventGuest(event_id={self.event_id}, guest_id={self.guest_id}, rsvp={self.rsvp})>"
