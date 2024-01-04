class Ticket:
    def __init__(self, id, booked_tickets, bus_obj, no_of_tickets, fare, customer_id):
        self.id = id
        self.booked_tickets = booked_tickets
        self.bus_obj = bus_obj
        self.no_of_tickets = no_of_tickets
        self.fare = fare
        self.customer_id = customer_id

    def ticket_details(self):
        print("-----------------------")
        print("Ticket details are:")
        print("Bus type:", self.bus_obj.bustype)
        print("Seat type:", self.bus_obj.seattype)
        print("Booked by the customer id:", self.customer_id)
        print("No. of tickets:", self.no_of_tickets)
        print("Booked seats:", self.booked_tickets)
        print("------------------------")
        return self.bus_obj
