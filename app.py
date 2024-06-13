from models import Event, Guest, EventGuest, EventVenue, Venue, SessionLocal
from datetime import datetime
# from sqlalchemy_setup import SessionLocal

def display_menu():
    print("\n===== Event Management Menu =====")
    print("1. Create Event")
    print("2. Create Guest")
    print("3. Create Venue")
    print("4. Assign Venue to Event")
    print("5. Register Guest for Event")
    print("6. Display All Events")
    print("7. Display All Guests")
    print("8. Display All Venues")
    print("9. View Guests of an Event")
    print("10. Find Event by ID")
    print("11. Find Guest by ID")
    print("12. Exit")

def create_event():
    print("\nEnter Event details:")
    name = input("Name: ")
    description = input("Description: ")
    date_str = input("Date (YYYY-MM-DD HH:MM): ")
    location = input("Location: ")

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        return

    event = Event.create(name=name, description=description, date=date, location=location)
    print(f"\nEvent created successfully: {event}")

def create_guest():
    name = input("Enter guest's name: ")
    email = input("Enter guest's email: ")
    phone = input("Enter guest's phone number: ")
    new_guest = Guest(name=name, email=email, phone=phone)
    session = SessionLocal()

    try:
        # Add the new guest to the session
        session.add(new_guest)
        session.commit()
        print("Guest added successfully!")

    except Exception as e:
        session.rollback()
        print(f"Error adding guest: {str(e)}")

def create_venue():
    name = input("Enter venue's name: ")
    address = input("Enter venue's address: ")
    capacity = int(input("Enter venue's capacity: "))
    new_venue = Venue(name=name, address=address, capacity=capacity)
    session = SessionLocal()

    try:
        # Add the new venue to the session
        session.add(new_venue)
        session.commit()
        print("Venue added successfully!")

    except Exception as e:
        session.rollback()
        print(f"Error adding venue: {str(e)}")



def assign_venue_to_event():
    events = Event.get_all()
    if not events:
        print("No events found.")
        return
    
    print("Select an Event to assign a venue:")
    for idx, event in enumerate(events, start=1):
        print(f"{idx}. {event.name} - {event.date}")

    try:
        event_choice = int(input("Enter the number of the event: ")) - 1
        selected_event = events[event_choice]
    except (IndexError, ValueError):
        print("Invalid selection.")
        return
    
    # Assuming you have a similar method to get all venues
    from models.venue import Venue  
    venues = Venue.get_all()
    if not venues:
        print("No venues found.")
        return
    
    print("Select a Venue:")
    for idx, venue in enumerate(venues, start=1):
        print(f"{idx}. {venue.name} - {venue.location}")

    try:
        venue_choice = int(input("Enter the number of the venue: ")) - 1
        selected_venue = venues[venue_choice]
    except (IndexError, ValueError):
        print("Invalid selection.")
        return
    
    # Assign venue to event
    # Assuming you have a method to assign venue in EventVenue class
    from models.event_venue import EventVenue  
    EventVenue.assign_venue_to_event(selected_event.id, selected_venue.id)
    print(f"Venue '{selected_venue.name}' assigned to event '{selected_event.name}'.")















# def register_guest_for_event():
#     events = Event.get_all()
#     guests = Guest.get_all()

#     if not events:
#         print("\nNo events available. Please create an event first.")
#         return

#     if not guests:
#         print("\nNo guests available. Please create a guest first.")
#         return

#     print("\nAvailable Events:")
#     for event in events:
#         print(f"{event.id}. {event.name}")

#     event_id = input("\nEnter Event ID to register a guest to: ")
#     try:
#         event_id = int(event_id)
#         event = Event.find_by_id(event_id)
#         if event:
#             print("\nAvailable Guests:")
#             for guest in guests:
#                 print(f"{guest.id}. {guest.name}")

#             guest_id = input("\nEnter Guest ID to register for this event: ")
#             try:
#                 guest_id = int(guest_id)
#                 guest = Guest.find_by_id(guest_id)
#                 if guest:
#                     event_guest = EventGuest.create(event_id=event_id, guest_id=guest_id)
#                     print(f"\nGuest '{guest.name}' registered for Event '{event.name}' successfully.")
#                 else:
#                     print(f"\nGuest with ID {guest_id} not found.")
#             except ValueError:
#                 print("\nInvalid input. Please enter a valid Guest ID.")
#         else:
#             print(f"\nEvent with ID {event_id} not found.")
#     except ValueError:
#         print("\nInvalid input. Please enter a valid Event ID.")


def register_guest_for_event():
    events = Event.get_all()
    if not events:
        print("No events found.")
        return
    
    print("Select an Event to register for:")
    for idx, event in enumerate(events, start=1):
        print(f"{idx}. {event.name} - {event.date}")

    try:
        event_choice = int(input("Enter the number of the event: ")) - 1
        selected_event = events[event_choice]
    except (IndexError, ValueError):
        print("Invalid selection.")
        return

    guest_name = input("Enter the guest's name: ")
    guest_email = input("Enter the guest's email: ")

    new_guest = Guest.create(name=guest_name, email=guest_email)
    print(f"Guest '{new_guest.name}' registered for event '{selected_event.name}'.")

    # Assuming you have a method to link guests to events
    from models.event_guest import EventGuest  
    EventGuest.register_guest_for_event(selected_event.id, new_guest.id)
    print(f"Guest '{new_guest.name}' successfully registered for event '{selected_event.name}'.")



def display_all_events():
    session = SessionLocal()
    try:
        events = Event.get_all(session)
        for event in events:
            print(f"Event: {event.name} | Date: {event.date} | Location: {event.location}")
    except Exception as e:
        print(f"Error fetching events: {str(e)}")



def display_all_guests():
    guests = Guest.get_all()
    print("\n===== All Guests =====")
    for guest in guests:
        print(f"{guest.id}. {guest.name} - {guest.email}")



def display_all_venues():
    venues = Venue.get_all()
    print("\n===== All Venues =====")
    for venue in venues:
        print(f"{venue.id}. {venue.name} - {venue.address}")


def view_guests_of_event():
    events = Event.get_all()
    if not events:
        print("\nNo events available. Please create an event first.")
        return

    print("\nAvailable Events:")
    for event in events:
        print(f"{event.id}. {event.name}")

    event_id = input("\nEnter Event ID to view guests: ")
    try:
        event_id = int(event_id)
        event = Event.find_by_id(event_id)
        if event:
            print(f"\n===== Guests of Event '{event.name}' =====")
            for event_guest in event.event_guests:
                print(f"{event_guest.guest.id}. {event_guest.guest.name} - {event_guest.guest.email}")
        else:
            print(f"\nEvent with ID {event_id} not found.")
    except ValueError:
        print("\nInvalid input. Please enter a valid Event ID.")




def find_event_by_id():
    event_id = input("\nEnter Event ID to find: ")
    try:
        event_id = int(event_id)
        event = Event.find_by_id(event_id)
        if event:
            print(f"\nEvent found: {event}")
        else:
            print(f"\nEvent with ID {event_id} not found.")
    except ValueError:
        print("\nInvalid input. Please enter a valid Event ID.")






def find_guest_by_id():
    guest_id = input("\nEnter Guest ID to find: ")
    try:
        
        guest_id = 1
        guest = session.query(Guest).filter_by(id=guest_id).first()
        if guest:
           print(f"Guest {guest.name} is attending events: {[event.name for event in guest.events_attending]}")
        else:
           print(f"Guest with ID {guest_id} not found.")
    # guest_id = int(input("Enter Guest ID to find: "))
    
    
    # session = SessionLocal()
    
    # try:
    #     from models.guest import Guest  
        
        
    #     guest = session.query(Guest).filter_by(id=guest_id).first()
        
    #     if guest:
    #         print(f"Found Guest: {guest.name}")
    #     else:
    #         print(f"No guest found with ID {guest_id}")
    
   
    except ValueError:
        print("\nInvalid input. Please enter a valid Guest ID.")










def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice: ")
        if choice == '1':
            create_event()
        elif choice == '2':
            create_guest()
        elif choice == '3':
            create_venue()
        elif choice == '4':
            assign_venue_to_event()
        elif choice == '5':
            register_guest_for_event()
        elif choice == '6':
            display_all_events()
        elif choice == '7':
            display_all_guests()
        elif choice == '8':
            display_all_venues()
        elif choice == '9':
            view_guests_of_event()
        elif choice == '10':
            find_event_by_id()
        elif choice == '11':
            find_guest_by_id()
        elif choice == '12':
            print("\nExiting the Event Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 12.")

if __name__ == "__main__":
    main()
