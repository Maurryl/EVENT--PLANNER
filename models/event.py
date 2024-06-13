

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


DATABASE_URL = 'sqlite:///event_planner.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    # event_guests = relationship("EventGuest", back_populates="event")
    event_venues = relationship("EventVenue", back_populates="event")
    guests_attending = relationship("Guest", secondary="event_guest", back_populates="events")
    events_attending = relationship("Event", secondary="event_guest", back_populates="guests")




    @classmethod
    def create(cls, **kwargs):
        event = cls(**kwargs)
        session.add(event)
        session.commit()
        return event

    @classmethod
    def delete(cls, event_id):
        event = session.query(cls).filter_by(id=event_id).first()
        if event:
            session.delete(event)
            session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, event_id):
        return session.query(cls).filter_by(id=event_id).first()
