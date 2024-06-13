# # # from datetime import datetime
# # # from models import SessionLocal, Event, Guest, EventGuest, EventVenue, Venue

# # # def initialize_database():
# # #     session = SessionLocal()
# # from sqlalchemy import create_engine
# # from sqlalchemy.orm import sessionmaker
# # from models.base import Base  # Ensure base.py exists in models and it defines Base
# # from models.event import Event
# # from models.event_guest import EventGuest
# # from models.guest import Guest
# # from models.venue import Venue
# # from models.event_venue import EventVenue
# # from datetime import datetime 

# # DATABASE_URL = 'sqlite:///event_planner.db'

# # def initialize_database():
# #     engine = create_engine(DATABASE_URL)
# #     Base.metadata.create_all(engine)

     
# #     Session = sessionmaker(bind=engine)
# #     session = Session()


# #     try:
# #         # Example events
# #         events_data = [
# #             Event(name="Tech Summit 2024", description="Annual technology conference showcasing latest innovations.", date=datetime(2024, 9, 20), location="San Francisco"),
# #             Event(name="Music Fest 2024", description="Three-day music festival featuring top artists and bands.", date=datetime(2024, 7, 5), location="Los Angeles"),
# #             Event(name="Product Launch", description="Launch event for new product line with live demos and presentations.", date=datetime(2024, 5, 15), location="New York"),
# #         ]

# #         # Example guests
# #         guests_data = [
# #             Guest(name="Alice Johnson", email="alice@example.com", phone="123-456-7890"),
# #             Guest(name="Bob Smith", email="bob@example.com", phone="234-567-8901"),
# #             Guest(name="Carol Brown", email="carol@example.com", phone="345-678-9012"),
# #         ]

# #         # Example event-guest relationships
# #         event_guests_data = [
# #             EventGuest(event_id=1, guest_id=1, rsvp=True),
# #             EventGuest(event_id=1, guest_id=2, rsvp=False),
# #             EventGuest(event_id=2, guest_id=2, rsvp=True),
# #             EventGuest(event_id=3, guest_id=3, rsvp=True),
# #         ]

# #         # Example event-venue relationships
# #         event_venues_data = [
# #             EventVenue(event_id=1, venue_id=1),
# #             EventVenue(event_id=2, venue_id=2),
# #             EventVenue(event_id=3, venue_id=1),
# #         ]

# #         # Example venues
# #         venues_data = [
# #             Venue(name="Moscone Center", address="747 Howard St, San Francisco, CA", capacity=5000),
# #             Venue(name="Hollywood Bowl", address="2301 N Highland Ave, Los Angeles, CA", capacity=17000),
# #             Venue(name="The Metropolitan Museum of Art", address="1000 5th Ave, New York, NY", capacity=2000),
# #         ]

# #         # Bulk insert data
# #         session.bulk_save_objects(events_data)
# #         session.bulk_save_objects(guests_data)
# #         session.bulk_save_objects(event_guests_data)
# #         session.bulk_save_objects(event_venues_data)
# #         session.bulk_save_objects(venues_data)

# #         session.commit()
# #         print("Data successfully added to the database.")

# #     except Exception as e:
# #         session.rollback()
# #         print(f"Error adding data: {str(e)}")

# #     finally:
# #         session.close()

# # if __name__ == "__main__":
# #     initialize_database()


# # init_db.py

# from models.base import Base
# from models.event import Event
# from models.guest import Guest
# from models.event_guest import EventGuest
# from models.venue import Venue
# from models.event_venue import EventVenue
# from sqlalchemy import create_engine

# DATABASE_URL = 'sqlite:///event_planner.db'
# engine = create_engine(DATABASE_URL)

# Base.metadata.create_all(engine)

# # Populating the database with some initial data
# from models import session

# try:
#     # Adding some events
#     event1 = Event.create(name="Tech Summit 2024", description="Annual technology conference showcasing latest innovations.", date="2024-09-20 00:00:00", location="San Francisco")
#     event2 = Event.create(name="Music Fest 2024", description="Three-day music festival featuring top artists and bands.", date="2024-07-05 00:00:00", location="Los Angeles")
    
#     # Adding some guests
#     guest1 = Guest.create(name="John Doe", email="john@example.com")
#     guest2 = Guest.create(name="Jane Smith", email="jane@example.com")
    
#     # Adding some venues
#     venue1 = Venue.create(name="Convention Center", location="San Francisco", capacity=5000)
#     venue2 = Venue.create(name="Open Air Stadium", location="Los Angeles", capacity=30000)
    
#     # Registering guests for events
#     EventGuest.register_guest_for_event(event1.id, guest1.id)
#     EventGuest.register_guest_for_event(event2.id, guest2.id)

#     # Assigning venues to events
#     EventVenue.assign_venue_to_event(event1.id, venue1.id)
#     EventVenue.assign_venue_to_event(event2.id, venue2.id)
    
# except Exception as e:
#     print(f"Error adding data: {e}")


# init_db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.event import Event
from models.venue import Venue
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
