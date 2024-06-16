# models/venue.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)

    # Define relationship to EventVenue
    event_venues = relationship("EventVenue", back_populates="venue")

    def __repr__(self):
        return f"<Venue(id={self.id}, name={self.name}, address={self.address}, capacity={self.capacity})>"
