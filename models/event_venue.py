from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class EventVenue(Base):
    __tablename__ = 'event_venues'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    event = relationship("Event", back_populates="event_venues")
    venue = relationship("Venue", back_populates="event_venues")

    def __repr__(self):
        return f"<EventVenue(id={self.id}, event_id={self.event_id}, venue_id={self.venue_id})>"
