from models import Event, Guest, EventGuest, EventVenue, Venue, SessionLocal
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
    location = input("Location: ")

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        return

    event = Event.create(name=name, description=description, date=date, location=location)
    print(f"\nEvent created successfully: {event}")

def create_guest():
    print("\nEnter Guest details:")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    guest = Guest.create(name=name, email=email, phone=phone)
    print(f"\nGuest created successfully: {guest}")

def create_venue():
    print("\nEnter Venue details:")
    name = input("Name: ")
    address = input("Address: ")
    capacity = input("Capacity: ")

    venue = Venue.create(name=name, address=address, capacity=capacity)
    print(f"\nVenue created successfully: {venue}")

def assign_venue_to_event():
    events = Event.get_all()
    venues = Venue.get_all()

    if not events:
        print("\nNo events available. Please create an event first.")
        return

    if not venues:
        print("\nNo venues available. Please create a venue first.")
        return

    print("\nAvailable Events:")
    for event in events:
        print(f"{event.id}. {event.name}")

    event_id = input("\nEnter Event ID to assign a venue to: ")
    try:
        event_id = int(event_id)
        event = Event.find_by_id(event_id)
        if event:
            print("\nAvailable Venues:")
            for venue in venues:
                print(f"{venue.id}. {venue.name}")

            venue_id = input("\nEnter Venue ID to assign to this event: ")
            try:
                venue_id = int(venue_id)
                venue = Venue.find_by_id(venue_id)
                if venue:
                    event_venue = EventVenue.create(event_id=event_id, venue_id=venue_id)
                    print(f"\nVenue '{venue.name}' assigned to Event '{event.name}' successfully.")
                else:
                    print(f"\nVenue with ID {venue_id} not found.")
            except ValueError:
                print("\nInvalid input. Please enter a valid Venue ID.")
        else:
            print(f"\nEvent with ID {event_id} not found.")
    except ValueError:
        print("\nInvalid input. Please enter a valid Event ID.")

def register_guest_for_event():
    events = Event.get_all()
    guests = Guest.get_all()

    if not events:
        print("\nNo events available. Please create an event first.")
        return

    if not guests:
        print("\nNo guests available. Please create a guest first.")
        return

    print("\nAvailable Events:")
    for event in events:
        print(f"{event.id}. {event.name}")

    event_id = input("\nEnter Event ID to register a guest to: ")
    try:
        event_id = int(event_id)
        event = Event.find_by_id(event_id)
        if event:
            print("\nAvailable Guests:")
            for guest in guests:
                print(f"{guest.id}. {guest.name}")

            guest_id = input("\nEnter Guest ID to register for this event: ")
            try:
                guest_id = int(guest_id)
                guest = Guest.find_by_id(guest_id)
                if guest:
                    event_guest = EventGuest.create(event_id=event_id, guest_id=guest_id)
                    print(f"\nGuest '{guest.name}' registered for Event '{event.name}' successfully.")
                else:
                    print(f"\nGuest with ID {guest_id} not found.")
            except ValueError:
                print("\nInvalid input. Please enter a valid Guest ID.")
        else:
            print(f"\nEvent with ID {event_id} not found.")
    except ValueError:
        print("\nInvalid input. Please enter a valid Event ID.")

def display_all_events():
    events = Event.get_all()
    print("\n===== All Events =====")
    for event in events:
        print(f"{event.id}. {event.name} - {event.date}")

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
        guest_id = int(guest_id)
        guest = Guest.find_by_id(guest_id)
        if guest:
            print(f"\nGuest found: {guest}")
        else:
            print(f"\nGuest with ID {guest_id} not found.")
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
