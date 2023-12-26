"""This is a Hotel booking system that allows users to book a hotel and make reservations
This uses OOP and is CLI """

import pandas

df = pandas.read_csv('hotels.csv', dtype={"id": str})
df_cards = pandas.read_csv('cards.csv', dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv('cards_security.csv', dtype=str)


class Hotel:
    """ Hotel Class that allows booking and available of Hotel"""

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books a hotel by changing its available to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if Hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()

        return availability == "yes"


class ReservationTicket:
    """Creates a Reservation Ticket ones an available hotel is booked"""

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        """Generates the ticket info"""
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


class CreditCard:
    """This Class is used to check credit data against what user has entered"""
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        """Validates the data user has entered"""
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    """Inherits from CreditCard Class"""

    def authenticate(self, given_password):
        """Used to check if account is authenticated via password"""
        password = df_cards_security.loc[df_cards_security["number"]
                                         == self.number, "password"].squeeze()
        if password == given_password:
            return True


print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    card_number = input("Please enter the credit card number: ")
    credit_card = SecureCreditCard(number=card_number)
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        password = input("Please enter the credit card password: ")
        if credit_card.authenticate(given_password=password):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(
                customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit Card authentication failed")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not available. ")
