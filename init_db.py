

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.event import Event
from models.venue import Base, Venue
from models.guest import Guest
from models.event_guest import EventGuest
from models.event_venue import EventVenue
from datetime import datetime

# Define your database URL
DATABASE_URL = 'sqlite:///event_planner.db'

# Create an engine that connects to the database
engine = create_engine(DATABASE_URL)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Initialize your data
event_data = [
    {
        'name': 'Tech Summit 2024',
        'description': 'Annual technology conference showcasing latest innovations.',
        'date': '2024-09-20 00:00:00',
        'location': 'San Francisco',
    },
    {
        'name': 'Music Fest 2024',
        'description': 'Three-day music festival featuring top artists and bands.',
        'date': '2024-07-05 00:00:00',
        'location': 'Los Angeles',
    },
    {
        'name': 'Product Launch',
        'description': 'Launch event for new product line with live demos and presentations.',
        'date': '2024-05-15 00:00:00',
        'location': 'New York',
    },
]

venue_data = [
    {
        'name': 'Convention Center',
        'location': 'San Francisco',
        'capacity': 1000,
        'created_at': datetime.now(),
        'updated_at': datetime.now(),
    },
    {
        'name': 'Stadium Arena',
        'location': 'Los Angeles',
        'capacity': 5000,
        'created_at': datetime.now(),
        'updated_at': datetime.now(),
    },
    {
        'name': 'Exhibition Hall',
        'location': 'New York',
        'capacity': 1500,
        'created_at': datetime.now(),
        'updated_at': datetime.now(),
    },
]

guest_data = [
    {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '123-456-7890',
    },
    {
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com',
        'phone': '987-654-3210',
    },
]

# Convert date string to datetime object for events
for event in event_data:
    event['date'] = datetime.strptime(event['date'], '%Y-%m-%d %H:%M:%S')

# Add events to the database
for event in event_data:
    new_event = Event(
        name=event['name'],
        description=event['description'],
        date=event['date'],
        location=event['location'],
    )
    session.add(new_event)

# Add venues to the database
for venue in venue_data:
    new_venue = Venue(
        name=venue['name'],
        location=venue['location'],
        capacity=venue['capacity'],
        created_at=venue['created_at'],
        updated_at=venue['updated_at'],
    )
    session.add(new_venue)

# Add guests to the database
for guest in guest_data:
    new_guest = Guest(
        name=guest['name'],
        email=guest['email'],
        phone=guest['phone'],
    )
    session.add(new_guest)

# Create EventGuest relationships (manually for demonstration)
event_guest_data = [
    {
        'event_id': 1,  # Assuming event_id 1 corresponds to 'Tech Summit 2024'
        'guest_id': 1,  # John Doe
    },
    {
        'event_id': 2,  # Assuming event_id 2 corresponds to 'Music Fest 2024'
        'guest_id': 2,  # Jane Smith
    },
]

for eg_data in event_guest_data:
    event_guest = EventGuest(
        event_id=eg_data['event_id'],
        guest_id=eg_data['guest_id'],
    )
    session.add(event_guest)

# Create EventVenue relationships (manually for demonstration)
event_venue_data = [
    {
        'event_id': 1,  # Tech Summit 2024
        'venue_id': 1,  # Convention Center
    },
    {
        'event_id': 2,  # Music Fest 2024
        'venue_id': 2,  # Stadium Arena
    },
]

for ev_data in event_venue_data:
    event_venue = EventVenue(
        event_id=ev_data['event_id'],
        venue_id=ev_data['venue_id'],
    )
    session.add(event_venue)

# Commit the session to persist changes
session.commit()

# Close the session
session.close()

print("Database initialized and populated successfully.")
