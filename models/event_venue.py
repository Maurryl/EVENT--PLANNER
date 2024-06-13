from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from datetime import datetime


DATABASE_URL = 'sqlite:///event_planner.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


class EventVenue(Base):
    __tablename__ = "event_venues"

    event_id = Column(Integer, ForeignKey("events.id"), primary_key=True)
    venue_id = Column(Integer, ForeignKey("venues.id"), primary_key=True)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    event = relationship("Event", back_populates="event_venues")
    venue = relationship("Venue")

    # def __repr__(self):
    #     return f"<EventVenue(event_id={self.event_id}, venue_id={self.venue_id})>"
    

    @classmethod
    def assign_venue_to_event(cls, event_id, venue_id):
        event_venue = cls(event_id=event_id, venue_id=venue_id)
        session.add(event_venue)
        session.commit()
        return event_venue

    @classmethod
    def get_all(cls):
        return session.query(cls).all()
