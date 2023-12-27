import pandas

# Dtype helps us to change type of columns
df = pandas.read_csv('hotels.csv', dtype={'id': str})
# records' : list like [{column -> value}, … , {column -> value}]
df_card = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pandas.read_csv("card_security.csv", dtype=str)


class Hotel:
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


class ReservationTicket:
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


class CreditCard:
    # To define how many parameter should use in init method and other method inside in class, you need to understand when we declare class init method authomatically
    # start work in situation for define in credit we need only number and that's why we can use only one parameter number
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        # We use dictionary data type because it is more efficient way to extract data
        card_data = {
            "number": self.number,
            "expiration": expiration,
            "holder": holder,
            "cvc": cvc
        }

        if card_data in df_card:
            return True
        else:
            return False


# Parent class: CreditCard
# Child class: CardSecurity
class CardSecurity(CreditCard):
    def authenticate(self, given_password):
        # When we inherit CreditCard class we have access to all his method that's why we can use here self.number
        password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False
