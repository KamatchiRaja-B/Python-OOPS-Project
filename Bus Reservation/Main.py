from BusReservationSystem import *
def main():
    bus = Bus("ABC123", 50)

    while True:
        print("\n1. Reserve Seats")
        print("2. Cancel Reservation")
        print("3. Display Available Seats")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            seats = int(input("Enter the number of seats to reserve: "))
            bus.reserve_seat(seats)
        elif choice == "2":
            seats = int(input("Enter the number of seats to cancel: "))
            bus.cancel_reservation(seats)
        elif choice == "3":
            bus.display_available_seats()
        elif choice == "4":
            print("Thank you for using the Bus Reservation System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
