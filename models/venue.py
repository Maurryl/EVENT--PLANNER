from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base
from datetime import datetime

Base = declarative_base()

DATABASE_URL = 'sqlite:///event_planner.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    capacity = Column(Integer)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # def __repr__(self):
    #     return f"<Venue(name='{self.name}', address='{self.address}')>"
    event_venues = relationship("EventVenue", back_populates="venue")

    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

    def __repr__(self):
        return f"<Venue(name='{self.name}', address='{self.address}')>"   


    @classmethod
    def create(cls, **kwargs):
        venue = cls(**kwargs)
        session.add(venue)
        session.commit()
        return venue

    @classmethod
    def delete(cls, venue_id):
        venue = session.query(cls).filter_by(id=venue_id).first()
        if venue:
            session.delete(venue)
            session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, venue_id):
        return session.query(cls).filter_by(id=venue_id).first()
    
    # def __repr__(self):
    #     return f"<Venue(name='{self.name}', address='{self.address}')>"