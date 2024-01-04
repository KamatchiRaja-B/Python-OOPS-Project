class Bus:
    def __init__(self, bustype, seattype):
        self.bustype = bustype
        self.seattype = seattype
        self.totalseats = 12
        self.nooftick = 0
        self.bookedseats = 0
        self.seatview = [[i + 1 for i in range(3)] for _ in range(4)]

    def view_seats(self):
        print("*->Driver")
        for i in range(4):
            for j in range(3):
                if self.seatview[i][j] > 0:
                    print(f" {self.seatview[i][j]} ", end=" ")
                elif self.seatview[i][j] == -1:
                    print(" M ", end=" ")
                else:
                    print(" F ", end=" ")
            print()
            if i == 1:
                print("  ------>")
            print("  ")

    def check_avail(self, seatno):
        for i in range(4):
            for j in range(3):
                if self.seatview[i][j] == seatno:
                    return self.seatview[i][j] == -1 or self.seatview[i][j] == -2

    def book(self):
        print("Enter no of tickets want to book")
        self.nooftick = int(input())
        booked_seats = []
        for _ in range(self.nooftick):
            print("Enter seat number want to be booked:")
            seatno = int(input())
            print("Enter gender M or F:")
            gender = input().upper()

            if seatno < 1 or seatno > 12 or not self.check_avail(seatno):
                print("Invalid seat number or seat already booked. Please choose another seat.")
                continue

            gender_code = -2 if gender == 'F' else -1

            for i in range(4):
                for j in range(3):
                    if self.seatview[i][j] == seatno:
                        if gender_code == -2:
                            self.seatview[i][j] = gender_code
                        else:
                            if (i + 1) % 2 != 0 and self.seatview[i + 1][j] == -2:
                                print("Cannot book seat. Please choose male seat neighbour.")
                            else:
                                self.seatview[i][j] = gender_code
                        booked_seats.append(seatno)

        self.bookedseats += len(booked_seats)
        return booked_seats

    def delete_seats(self, booked_tickets):
        for t in booked_tickets:
            seat = 1
            for i in range(4):
                for j in range(3):
                    if seat == t:
                        self.seatview[i][j] = seat
                        self.bookedseats -= 1
                        break
                    seat += 1


    def calculate_fare(self):
        if self.bustype.lower() == "ac" and self.seattype.lower() == "sleeper":
            return self.nooftick * 1000.00
        elif self.bustype.lower() == "ac" and self.seattype.lower() == "seater":
            return self.nooftick * 650.00
        elif self.bustype.lower() == "non-ac" and self.seattype.lower() == "sleeper":
            return self.nooftick * 750.00
        else:
            return self.nooftick * 500.00
