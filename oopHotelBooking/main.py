import pandas as pd

df = pd.read_csv('hotels.csv', sep=',')


class Hotel:
    def __init__(self, hotel_uid):
        self.hotel_uid = int(hotel_uid)
        self.hotel = df.loc[df['uid'] == hotel_uid]
        self.name = self.hotel.name.squeeze()
        self.city = self.hotel.city.squeeze()
        self.is_available = self.hotel.available.squeeze()
        pass

    def create_booking(self):
        df.loc[df['uid'] == self.hotel_uid, 'available'] = 'no'
        df.to_csv('hotels.csv', sep=',', index=False)

    def available(self):
        if self.is_available == 'yes':
            return True
        return False


class ReservationTicket:
    def __init__(self, hotel_object, customer_name):
        self.hotel_object = hotel_object
        self.customer_name = customer_name

    def generate(self):
        content = f"{self.customer_name} is booked at {self.hotel_object.name} in wonderful {self.hotel_object.city}"
        print(content)
        return


class CreditCard:
    def __init__(self, number, expiration_date, holder, cvv):
        self.number = number
        self.expiration_date = expiration_date
        self.holder = holder
        self.cvv = cvv

    def validate(self):
        valid_cards = pd.read_csv('cards.csv', sep=',', dtype=str).to_dict(orient='records')
        card_data = {
            "number": self.number,
            "expiration": self.expiration_date,
            "holder": self.holder,
            "cvc": self.cvv
        }
        if card_data in valid_cards:
            return True
        else:
            return False


print(df)

hotel_id = int(input("Enter the UID of the hotel > "))
hotel = Hotel(hotel_uid=hotel_id)

if hotel.available():
    credit_card = CreditCard(number='1234', expiration_date="12/26", holder="JOHN SMITH", cvv="123")
    if credit_card.validate():
        name = input("Enter your name > ")
        hotel.create_booking()
        reservation_ticket = ReservationTicket(hotel_object=hotel, customer_name=name)
        reservation_ticket.generate()
else:
    print("Sorry, the hotel is not available")
