from classes import *

print(df)
hotel_id = input("Enter the id of the hotel : ")
hotel = Hotel(hotel_id)
if hotel.available():
    # The number argument using by parent class CreditCard because we inherit it in our CardSecure class
    credit_card = CardSecurity(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment.")
else:
    print("Hotel is not free.")
