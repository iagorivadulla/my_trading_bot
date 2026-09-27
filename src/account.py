from datetime import datetime

'''
In this file will build an enviroment for trading

'''

class Account:
    def __init__(self, fiat: float):
        self.fiat = fiat #the first ammount
        self.assets = {} #this initialites a boid dict to see the actual state
        self.history = {} #history of transactions

    def add_fiat(self, added):
        #this will add more fiat to accouunt
        self.fiat += added
        self.history['fiat'] = [datetime.now(), added]
        print(f'{added} added to account. Now you have {self.fiat}')

    def buy(self, asset, amount, price):
        #this will buy an asset added it to assets
        cost = amount * price
        if cost > self.fiat: #if you don't have enought you can't buy
            print(f'You do not have enough fiat to buy {asset}')




    def sell(self, asset, amount, price):
        #this will sell an asset if is in assets
        pass

    def state(self):
        print(f'Toal fiat: {self.fiat}')
        print(f'Assets: {self.assets}')

    def history(self):
        print(self.history)



if __name__ == '__main__':
    pass