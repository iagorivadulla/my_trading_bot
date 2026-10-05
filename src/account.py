from datetime import datetime

'''
In this file will build an enviroment for trading

'''


class Account:
    def __init__(self, fiat: float):
        self.fiat = fiat #the first ammount
        self.assets = {} #this initialites a boid dict to see the actual state
        self.history = {} #history of transactions

    def __calculate_avg(self, asset):
        #this is a private method to calculate avg prices
        total_asset = 0
        total_cost = 0

        for i in self.history[asset].values():
            if i['action'] == 'buy':
                total_asset += i['amount']
                total_cost += i['amount'] * i['price']

            elif i['action'] == 'sell':
                avg_price = total_cost / total_asset
                total_cost -= i['amount'] * avg_price
                total_asset -= i['amount']

        if total_asset == 0:
            return 0

        return total_cost / total_asset

    def add_fiat(self, added):
        #this will add more fiat to accouunt
        self.fiat += added
        self.history['fiat'] = [datetime.now(), added]
        print(f'{added} added to account. Now you have {self.fiat}')

    def buy(self, asset, amount, price, date = None):
        #this will buy an asset added it to assets
        cost = amount * price
        if cost > self.fiat: #if you don't have enought you can't buy
            print(f'You do not have enough fiat to buy {asset}')
            return

        if asset not in self.assets:
            self.assets[asset] = {
                'amount': 0,
                'total_cost' : 0,
                'total_gain' : 0
            }
        if asset not in self.history:
            self.history[asset] = {}

        hist = {
            'amount': amount,
            'price': price,
            'action' : 'buy'
        }

        if date is None:
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


        self.history[asset][date] = hist

        self.assets[asset]['amount'] += amount
        self.assets[asset]['total_cost'] += cost
        self.assets[asset]['avg_price'] = self.__calculate_avg(asset)
        self.fiat -= cost



    def sell(self, asset, amount, price, date = None):
        #this will sell an asset if is in assets
        if asset not in self.assets:
            print(f'You do not have this asset')
            return

        if amount > self.assets[asset]['amount']:
            print(f'You do not have enough asset, you have {self.assets[asset]['amount']} {asset}')
            return

        revenue = amount * price

        hist = {
            'amount': amount,
            'price': price,
            'action' : 'sell'
        }

        if date is None:
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.history[asset][date] = hist

        avg_price = self.assets[asset]['total_cost'] / self.assets[asset]['amount']
        cost_of_sold = amount * avg_price

        self.assets[asset]['amount'] -= amount
        self.assets[asset]['total_gain'] += revenue
        self.assets[asset]['total_cost'] -= cost_of_sold
        self.assets[asset]['avg_price'] = self.__calculate_avg(asset)
        self.fiat += revenue

    def state(self):
        print(f'Total fiat: {self.fiat}')
        print(f'Assets: {self.assets}')

    def hist(self):
        return self.history



if __name__ == '__main__':
    pass