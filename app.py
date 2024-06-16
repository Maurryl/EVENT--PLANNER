from models import Event, Guest, Venue, EventGuest, EventVenue, SessionLocal
from datetime import datetime

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

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        return

    location = input("Location: ")

    session = SessionLocal()
    try:
        new_event = Event(name=name, description=description, date=date, location=location)
        session.add(new_event)
        session.commit()
        print(f"Event '{name}' created successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error creating event: {str(e)}")
    finally:
        session.close()

def create_guest():
    name = input("Enter guest's name: ")
    email = input("Enter guest's email: ")
    phone = input("Enter guest's phone number: ")

    session = SessionLocal()
    try:
        new_guest = Guest(name=name, email=email, phone=phone)
        session.add(new_guest)
        session.commit()
        print("Guest added successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error adding guest: {str(e)}")
    finally:
        session.close()

def create_venue():
    name = input("Enter venue's name: ")
    address = input("Enter venue's address: ")
    capacity = int(input("Enter venue's capacity: "))

    session = SessionLocal()
    try:
        new_venue = Venue(name=name, address=address, capacity=capacity)
        session.add(new_venue)
        session.commit()
        print("Venue added successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error adding venue: {str(e)}")
    finally:
        session.close()

def assign_venue_to_event():
    session = SessionLocal()

    events = session.query(Event).all()
    if not events:
        print("No events found.")
        session.close()
        return

    print("Select an Event to assign a venue:")
    for idx, event in enumerate(events, start=1):
        print(f"{idx}. {event.name} - {event.date}")

    try:
        event_choice = int(input("Enter the number of the event: ")) - 1
        selected_event = events[event_choice]
    except (IndexError, ValueError):
        print("Invalid selection.")
        session.close()
        return

    venues = session.query(Venue).all()
    if not venues:
        print("No venues found.")
        session.close()
        return

    print("Select a Venue:")
    for idx, venue in enumerate(venues, start=1):
        print(f"{idx}. {venue.name} - {venue.address}")

    try:
        venue_choice = int(input("Enter the number of the venue: ")) - 1
        selected_venue = venues[venue_choice]
    except (IndexError, ValueError):
        print("Invalid selection.")
        session.close()
        return

    try:
        new_event_venue = EventVenue(event_id=selected_event.id, venue_id=selected_venue.id)
        session.add(new_event_venue)
        session.commit()
        print(f"Venue '{selected_venue.name}' assigned to event '{selected_event.name}'.")
    except Exception as e:
        session.rollback()
        print(f"Error assigning venue to event: {str(e)}")
    finally:
        session.close()

def register_guest_for_event():
    session = SessionLocal()

    events = session.query(Event).all()
    if not events:
        print("No events found.")
        session.close()
        return
    
    print("Select an Event to register for:")
    for idx, event in enumerate(events, start=1):
        print(f"{idx}. {event.name} - {event.date}")

    try:
        event_choice = int(input("Enter the number of the event: ")) - 1
        selected_event = events[event_choice]
    except (IndexError, ValueError):
        print("Invalid selection.")
        session.close()
        return

    guest_name = input("Enter the guest's name: ")
    guest_email = input("Enter the guest's email: ")
    guest_phone = input("Enter the guest's phone: ")

    try:
        new_guest = Guest(name=guest_name, email=guest_email, phone=guest_phone)
        session.add(new_guest)
        session.commit()

        new_event_guest = EventGuest(event_id=selected_event.id, guest_id=new_guest.id)
        session.add(new_event_guest)
        session.commit()

        print(f"Guest '{new_guest.name}' registered for event '{selected_event.name}'.")
    except Exception as e:
        session.rollback()
        print(f"Error registering guest for event: {str(e)}")
    finally:
        session.close()

def display_all_events():
    session = SessionLocal()
    events = session.query(Event).all()
    session.close()

    print("\n===== All Events =====")
    for event in events:
        print(f"{event.id}. {event.name} - {event.date} - {event.location}")

def display_all_guests():
    session = SessionLocal()
    guests = session.query(Guest).all()
    session.close()

    print("\n===== All Guests =====")
    for guest in guests:
        print(f"{guest.id}. {guest.name} - {guest.email} - {guest.phone}")

def display_all_venues():
    session = SessionLocal()
    venues = session.query(Venue).all()
    session.close()

    print("\n===== All Venues =====")
    for venue in venues:
        print(f"{venue.id}. {venue.name} - {venue.address} - Capacity: {venue.capacity}")

def view_guests_of_event():
    session = SessionLocal()

    events = session.query(Event).all()
    if not events:
        print("No events found.")
        session.close()
        return

    print("Select an Event to view guests:")
    for idx, event in enumerate(events, start=1):
        print(f"{idx}. {event.name} - {event.date}")

    try:
        event_choice = int(input("Enter the number of the event: ")) - 1
        selected_event = events[event_choice]
    except (IndexError, ValueError):
        print("Invalid selection.")
        session.close()
        return

    print(f"\n===== Guests of Event '{selected_event.name}' =====")
    guests = session.query(Guest).join(EventGuest).filter(EventGuest.event_id == selected_event.id).all()
    for guest in guests:
        print(f"{guest.id}. {guest.name} - {guest.email}")

    session.close()

def find_event_by_id():
    session = SessionLocal()

    event_id = input("\nEnter Event ID to find: ")
    try:
        event_id = int(event_id)
        event = session.query(Event).filter(Event.id == event_id).first()
        if event:
            print(f"\nEvent found: {event.name} - {event.date} - {event.location}")
        else:
            print(f"\nEvent with ID {event_id} not found.")
    except ValueError:
        print("\nInvalid input. Please enter a valid Event ID.")
    finally:
        session.close()

def find_guest_by_id():
    session = SessionLocal()

    guest_id = input("\nEnter Guest ID to find: ")
    try:
        guest_id = int(guest_id)
        guest = session.query(Guest).filter(Guest.id == guest_id).first()
        if guest:
            print(f"\nGuest found: {guest.name} - {guest.email} - {guest.phone}")
        else:
            print(f"\nGuest with ID {guest_id} not found.")
    except ValueError:
        print("\nInvalid input. Please enter a valid Guest ID.")
    finally:
        session.close()

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
