class Bus:
    def __init__(self, bus_number, total_seats):
        self.bus_number = bus_number
        self.total_seats = total_seats
        self.available_seats = total_seats

    def reserve_seat(self, seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            print(f"Seats reserved successfully. Available seats: {self.available_seats}")
        else:
            print("Sorry, there are not enough seats available.")

    def cancel_reservation(self, seats):
        if seats <= self.total_seats - self.available_seats:
            self.available_seats += seats
            print(f"Reservation cancelled successfully. Available seats: {self.available_seats}")
        else:
            print("Invalid number of seats to cancel.")

    def display_available_seats(self):
        print(f"Available seats: {self.available_seats}")
