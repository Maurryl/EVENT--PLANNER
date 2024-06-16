# models/guest.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    # Define relationship to EventGuest
    event_guests = relationship("EventGuest", back_populates="guest")

    def __repr__(self):
        return f"<Guest(id={self.id}, name={self.name}, email={self.email}, phone={self.phone})>"
