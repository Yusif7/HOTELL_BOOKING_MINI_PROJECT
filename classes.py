import pandas

# Dtype helps us to change type of columns
df = pandas.read_csv('hotels.csv', dtype={'id': str})


class Hotel():
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        # Extract name column from our data frame
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        # Book a hotel by changing its availability to no
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # Here, we are saving the file with no index number.
        df.to_csv('hotels.csv', index=False)

    def available(self):
        # Check if the hotel is available
        # You should convert type to integer
        # In current case we have value of id column and want to find the value of available column
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket():
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        # We create hotel instance and inside the __init__ method have hotel name, here we extract this data and show to user
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter the id of the hotel : ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")


