# from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.orm import relationship
# from models.base import Base
# from datetime import datetime


# class Guest(Base):
#     __tablename__ = "guests"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String)
#     phone = Column(String)

#     created_at = Column(DateTime, default=datetime.now)

#     event_guests = relationship("EventGuest", back_populates="guest")

#     def __repr__(self):
#         return f"<Guest(name='{self.name}', email='{self.email}')>"
# models/guest.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///event_planner.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String(20), nullable=False)

    event_guests = relationship("EventGuest", back_populates="guest")

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


    @classmethod
    def create(cls, **kwargs):
        guest = cls(**kwargs)
        session.add(guest)
        session.commit()
        return guest

    @classmethod
    def delete(cls, guest_id):
        guest = session.query(cls).filter_by(id=guest_id).first()
        if guest:
            session.delete(guest)
            session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, guest_id):
        return session.query(cls).filter_by(id=guest_id).first()
