from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# SQLite database (you can change the path)
SQLALCHEMY_DATABASE_URL = "sqlite:///./event_management.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

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

    @classmethod
    def create(cls, name, address, capacity):
        session = SessionLocal()
        venue = cls(name=name, address=address, capacity=capacity)
        session.add(venue)
        session.commit()
        return venue

    @classmethod
    def get_all(cls):
        session = SessionLocal()
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, venue_id):
        session = SessionLocal()
        return session.query(cls).filter_by(id=venue_id).first()


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    date = Column(DateTime)
    location = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    event_venues = relationship("EventVenue", back_populates="event")
    event_guests = relationship("EventGuest", back_populates="event")

    def __repr__(self):
        return f"<Event(name='{self.name}', date='{self.date}')>"

    @classmethod
    def create(cls, name, description, date, location):
        session = SessionLocal()
        event = cls(name=name, description=description, date=date, location=location)
        session.add(event)
        session.commit()
        return event

    @classmethod
    def get_all(cls):
        session = SessionLocal()
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, event_id):
        session = SessionLocal()
        return session.query(cls).filter_by(id=event_id).first()


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

    @classmethod
    def create(cls, name, email, phone):
        session = SessionLocal()
        guest = cls(name=name, email=email, phone=phone)
        session.add(guest)
        session.commit()
        return guest

    @classmethod
    def get_all(cls):
        session = SessionLocal()
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, guest_id):
        session = SessionLocal()
        return session.query(cls).filter_by(id=guest_id).first()


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

    @classmethod
    def create(cls, event_id, guest_id, rsvp=False):
        session = SessionLocal()
        event_guest = cls(event_id=event_id, guest_id=guest_id, rsvp=rsvp)
        session.add(event_guest)
        session.commit()
        return event_guest


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

    @classmethod
    def create(cls, event_id, venue_id):
        session = SessionLocal()
        event_venue = cls(event_id=event_id, venue_id=venue_id)
        session.add(event_venue)
        session.commit()
        return event_venue


# Create the database tables
Base.metadata.create_all(bind=engine)
