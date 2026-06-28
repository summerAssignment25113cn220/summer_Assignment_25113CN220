def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Please enter a whole number.")

def get_string(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Invalid! Cannot be empty.")
        else:
            return value

# ─────────────────────────────────────────
print("=== Ticket Booking System ===")

tickets      = []
total_seats  = 10
booked_seats = 0

while True:
    print(f"\n--- MENU --- (Seats available: {total_seats - booked_seats}/{total_seats})")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Check Booking by ID")
    print("4. Show All Bookings")
    print("5. Exit")

    choice = get_int("Enter choice: ")

    if choice == 1:
        if booked_seats >= total_seats:
            print("Sorry! All seats are booked.")
        else:
            booking_id = get_int("Booking ID: ")
            exists     = any(t["id"] == booking_id for t in tickets)
            if exists:
                print("Booking ID already exists!")
            else:
                name  = get_string("Passenger Name: ")
                dest  = get_string("Destination: ")
                booked_seats += 1
                tickets.append({
                    "id":     booking_id,
                    "name":   name,
                    "dest":   dest,
                    "seat":   booked_seats,
                    "status": "Confirmed"
                })
                print(f"Ticket booked! Seat No.: {booked_seats}")

    elif choice == 2:
        booking_id = get_int("Enter Booking ID to cancel: ")
        found      = next((t for t in tickets if t["id"] == booking_id), None)
        if found:
            if found["status"] == "Cancelled":
                print("Ticket already cancelled!")
            else:
                found["status"] = "Cancelled"
                booked_seats   -= 1
                print(f"Ticket {booking_id} cancelled successfully!")
        else:
            print("Booking ID not found!")

    elif choice == 3:
        booking_id = get_int("Enter Booking ID: ")
        found      = next((t for t in tickets if t["id"] == booking_id), None)
        if found:
            print(f"\nBooking ID  : {found['id']}")
            print(f"Name        : {found['name']}")
            print(f"Destination : {found['dest']}")
            print(f"Seat No.    : {found['seat']}")
            print(f"Status      : {found['status']}")
        else:
            print("Booking not found!")

    elif choice == 4:
        if len(tickets) == 0:
            print("No bookings yet!")
        else:
            print(f"\n--- All Bookings ({len(tickets)} total) ---")
            for t in tickets:
                print(f"ID: {t['id']}  Name: {t['name']}  "
                      f"Dest: {t['dest']}  Seat: {t['seat']}  [{t['status']}]")

    elif choice == 5:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")