import pandas as pd
from util import pdfgen

class Inventory:
    def __init__(self):
        self.df = pd.read_csv('inventory.csv', sep=',')

    def print(self):
        print(self.df)

    def get_amount(self, product_id):
        amount = self.df.loc[self.df['id'] == product_id, 'quantity'].values[0]
        return amount

    def get_product(self, product_id):
        return self.df.loc[self.df['id'] == product_id]

    def reduce_qty_by_one(self, product_id):
        self.df.loc[self.df['id'] == product_id, 'quantity'] -= 1
        self.df.to_csv('inventory.csv', index=False)


class Purchase:
    def __init__(self, product_id):
        self.product_id = product_id

    def place_order(self):
        i = Inventory()
        product = i.get_product(self.product_id)
        amount = i.get_amount(self.product_id)
        if amount > 0:
            i.reduce_qty_by_one(self.product_id)
            r = Receipt(product)
            r.generate()
        else:
            print('There is no stock left of this product, please try again')


class Receipt:
    def __init__(self, product):
        self.product = product

    def generate(self):
        receipt_number = self.product['id'].values[0]
        article_name = self.product['name'].values[0]
        price = self.product['price'].values[0]
        pdfgen.generate_pdf(receipt_number, article_name, price)


inventory = Inventory()
inventory.print()

uid = int(input('Choose an article to buy > '))

purchase = Purchase(uid)
purchase.place_order()
