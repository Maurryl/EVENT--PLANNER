# models/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = 'sqlite:///event_management.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Import all models to ensure they are registered with Base
from .event import Event
from .guest import Guest
from .venue import Venue
from .event_guest import EventGuest
from .event_venue import EventVenue

# Define relationships after all models are imported and defined
Event.event_guests = relationship("EventGuest", back_populates="event")
Guest.event_guests = relationship("EventGuest", back_populates="guest")
Event.event_venues = relationship("EventVenue", back_populates="event")
Venue.event_venues = relationship("EventVenue", back_populates="venue")

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
