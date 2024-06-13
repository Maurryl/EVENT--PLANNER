# # models/__init__.py

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./event_management.db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# from .event import Event
# from .guest import Guest
# from .event_guest import EventGuest
# from .event_venue import EventVenue
# from .venue import Venue


# models/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

DATABASE_URL = 'sqlite:///event_planner.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = Session()

# Import all models to ensure they are registered properly
from models.event import Event
from models.guest import Guest
from models.event_guest import EventGuest
from models.venue import Venue
from models.event_venue import EventVenue

Base.metadata.create_all(engine)
