class Customer:
    def __init__(self, customer_id, name, email, phone_number, reservation_history=None):
        if reservation_history is None:
            reservation_history = []
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__reservation_history = reservation_history

    # Getter and Setter methods
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_reservation_history(self):
        return self.__reservation_history

    def add_reservation(self, reservation):
        self.__reservation_history.append(reservation)

    def cancel_reservation(self, reservation_id):
        for reservation in self.__reservation_history:
            if reservation.get_reservation_id() == reservation_id:
                self.__reservation_history.remove(reservation)
                break

class Reservation:
    def __init__(self, reservation_id, room_number, check_in_date, check_out_date, status):
        self.__reservation_id = reservation_id
        self.__room_number = room_number
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status

    def get_reservation_id(self):
        return self.__reservation_id

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def check_availability(self):
        pass

    def modify_reservation(self, new_check_in, new_check_out):
        self.__check_in_date = new_check_in
        self.__check_out_date = new_check_out

    def cancel_reservation(self):
        self.__status = "Cancelled"
class Room:
    def __init__(self, room_number, room_type, price, is_available, max_occupancy):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__price = price
        self.__is_available = is_available
        self.__max_occupancy = max_occupancy

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def is_room_available(self):
        return self.__is_available

    def set_availability(self, is_available):
        self.__is_available = is_available

    def get_max_occupancy(self):
        return self.__max_occupancy

    def set_max_occupancy(self, max_occupancy):
        self.__max_occupancy = max_occupancy

class Payment:
    def __init__(self, payment_id, payment_date, amount, payment_method, reservation_id):
        self.__payment_id = payment_id
        self.__payment_date = payment_date
        self.__amount = amount
        self.__payment_method = payment_method
        self.__reservation_id = reservation_id

    def get_payment_id(self):
        return self.__payment_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_payment_date(self):
        return self.__payment_date

    def set_payment_date(self, payment_date):
        self.__payment_date = payment_date

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_payment_method(self):
        return self.__payment_method

    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

    def process_payment(self):
        pass

# Create a room
room1 = Room(101, "Deluxe", 300, True, 2)

# Create a reservation
reservation1 = Reservation("R001", room1.get_room_number(), "2024-09-15", "2024-09-20", "Confirmed")

# Create a customer and add the reservation
customer1 = Customer("C001", "mohammed", "mohammedali@gmail.cm", "2334567789")
customer1.add_reservation(reservation1)

# Create a payment for the reservation
payment1 = Payment("P001", "2024-09-15", 300, "Credit Card", reservation1.get_reservation_id())
payment1.process_payment()

# Display Customer and Reservation Information
print(f"Customer Name: {customer1.get_name()}")
print(f"Reservation ID: {reservation1.get_reservation_id()}")
print(f"Room Number: {reservation1.get_room_number()}")
print(f"Check-in Date: {reservation1.get_check_in_date()}")
print(f"Check-out Date: {reservation1.get_check_out_date()}")
print(f"Payment Amount: {payment1.get_amount()}")
