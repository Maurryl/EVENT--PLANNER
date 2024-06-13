# from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
# from models.base import Base
# from datetime import datetime

# class EventGuest(Base):
#     __tablename__ = "event_guests"

#     event_id = Column(Integer, ForeignKey("events.id"), primary_key=True)
#     guest_id = Column(Integer, ForeignKey("guests.id"), primary_key=True)
#     rsvp = Column(Boolean, default=False)

#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

#     event = relationship("Event", back_populates="event_guests")
#     guest = relationship("Guest", back_populates="event_guests")

#     def __repr__(self):
#         return f"<EventGuest(event_id={self.event_id}, guest_id={self.guest_id}, rsvp={self.rsvp})>"


# models/event_guest.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///event_planner.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()



class EventGuest(Base):
    __tablename__ = 'event_guests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    guest_id = Column(Integer, ForeignKey('guests.id'))

    event = relationship("Event", back_populates="event_guests")
    guest = relationship("Guest", back_populates="event_guests")

    @classmethod
    def register_guest_for_event(cls, event_id, guest_id):
        event_guest = cls(event_id=event_id, guest_id=guest_id)
        session.add(event_guest)
        session.commit()
        return event_guest

    @classmethod
    def get_all(cls):
        return session.query(cls).all()
