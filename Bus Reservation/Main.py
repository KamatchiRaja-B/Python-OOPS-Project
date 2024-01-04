from Bus import *
from Customer import *
from Ticket import *
class Main:
    def __init__(self):
        self.customer_obj = []
        self.bus_obj = [Bus("AC", "seater"), Bus("AC", "sleeper"), Bus("Non-AC", "seater"), Bus("Non-AC", "sleeper")]
        self.ticket_obj = []

    def customer_sign_up(self):
        print("Enter id, name, password, age, gender to sign-up")
        id_num = int(input())
        name = input()
        password = input()
        age = int(input())
        gender = input().upper()

        for c in self.customer_obj:
            if c.id == id_num:
                print("User id already exists.")
                return

        self.customer_obj.append(Customer(id_num, name, password, age, gender))
        print("Back to the home page")

    def customer_login(self):
        print("Enter id, password to login")
        id_num = int(input())
        password = input()

        for c in self.customer_obj:
            if c.id == id_num and c.password == password:
                current_customer = c
                break
        else:
            print("Invalid login or password.")
            return

        while True:
            print("\n1)Book Tickets\n2)View Tickets\n3)Cancel Tickets\n4)Summary\n5)Logout")
            choice_after_login = int(input())

            if choice_after_login == 1:
                print("Choose bus type, seat type")
                bus_type = input()
                seat_type = input()

                for b in self.bus_obj:
                    if b.bustype.lower() == bus_type.lower() and b.seattype.lower() == seat_type.lower():
                        booked_seats = b.book()
                        no_of_tickets = b.nooftick
                        fare = b.calculate_fare()
                        ticket_id = len(self.ticket_obj)
                        print("-------------------------------")
                        self.ticket_obj.append(Ticket(ticket_id, booked_seats, b, no_of_tickets, fare, current_customer.id))
                        print(f"Your Ticket id: {ticket_id}\nYou have to pay Rs.{fare}\nYour Tickets were booked\n"
                              "!!!!Happy Journey!!!!")
                        print("-------------------------------")
                        break
                else:
                    print("Bus not found.")

            elif choice_after_login == 2:
                print("Enter bus type, seat type")
                bus_type = input()

if __name__ == "__main__":
    choice = 0
    m = Main()
    m.createObj()
    while True:
        print("1)Customer Sign-up\n2)Customer Login\n3)Stop Program")
        choice = int(input())
        if choice == 1:
            m.customerSignUp()
        elif choice == 2:
            m.customerLogin()
        elif choice == 3:
            exit(0)
