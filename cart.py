import typing
import json
import abc_class as abc # Renamed abc.py to abc_class.py as 'abc' is a python module for defining abstract base class
import requests
from datetime import date
from currency_symbols import CurrencySymbols

class ShoppingCart(abc.ShoppingCart):
    
    '''
    shopping cart class that initialises items to be added to the cart, loads the price list for all items and conversion
    rates for seevral currencies
    
    price_list(list): list that stores prices for all products
    currency_list(list): list that stores converison rates for different currencies
    currecny(str): currency selected by the user for transaction
    '''
    
    def __init__(self):
        
        self._items = dict()
        
        self.currency = "EUR"
        
        # load JSON file with product prices
        with open('products.json') as json_file:
            
            prices_data = json.load(json_file)
        
        self.price_list = prices_data['products']

    def add_item(self, product_code: str, quantity: int):
        
        """Adds items and their respective quantities to the shopping cart

        Parameters:
        product_code (str): name of the product to be added to the cart
        quantity (int): quantity of the product to be added to the cart

        Returns:
        no return value

       """
        
        if product_code not in self._items:
            
            self._items[product_code] = quantity
        
        else:
            
            q = self._items[product_code]
            
            self._items[product_code] = q + quantity
    
    def _get_currency(self) -> str:
        
        """gets the user's preferred currency for the transaction

        Parameters:
        none, except the reference to point to the class object
        
        Returns:
        a string that represents name of the currency selected by the user

       """
        
        print("""
            1.EUR (Euro)
            2.USD (United States Dollar)
            3.GBP (Pound Sterling)
            4.AUD (Australian Dollar)
            5.JPY (Japanese Yen)
            """)
        
        choice = input("Please select currency for this transaction: ")
        
        if choice=="1":
            currency = 'EUR'
        
        elif choice=="2":
            currency = 'USD'
        
        elif choice=="3":
            currency = 'GBP'
        
        elif choice=="4":
            currency = 'AUD'
        
        elif choice=="5":
            currency = 'JPY'
            
        else:
            print("Invalid choice, please select an option from the list")
            currency = self._get_currency()
            
        return currency
    
    def get_conversion_rate(self,transaction_currency):
    
        """gets the converison rate for the specified currency considering 'Euro' as the base currency

            Parameters:
            transaction_currency(str): currency selected by the user for a particular transaction

            Returns:
            conversion rate value as a float number from 'Euro' to the specified currency

           """
        
        # get today's date in yyyy-mm-dd
        today = date.today()
        current_date = today.strftime("%Y-%m-%d")

        # base currency or reference currency
        base="EUR"

        # conversion rates from a date
        start_date=current_date

        # conversion rates till a date
        end_date=current_date

        # api url for request 
        url = 'https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'
        
        send_request = url.format(base,start_date,end_date,transaction_currency)
    
        response = requests.get(send_request)

        # retrive response in json format
        data = response.json()

        conversion_rate = round((data['rates'][current_date][transaction_currency]),2)
    
        return conversion_rate
    
    def get_currency_symbol(self,transaction_currecny):
        
        """gets the symbol for the specified currency

            Parameters:
            transaction_currency(str): currency selected by the user for a particular transaction

            Returns:
            currency symbol as a string for the specified currency

           """
        
        currency_symbol = CurrencySymbols.get_symbol(transaction_currecny)
        
        return currency_symbol
    
    
    def print_receipt(self) -> typing.List[str]:
        
        """lists and prints all the items in the shopping cart along with the total price for the transaction

        Parameters:
        none, except the reference to point to the class object

        Returns:
        a list of strings where each element in the list represents an item in the shopping cart along with its quantity and
        price. The last element shows the total price for the transaction

       """
        
        lines = []
        
        total_price = 0.0
        
        self.currency = self._get_currency()
        
        # print items in receipt in the same order that they are added to the shopping cart
        for item in self._items.items():
            
            symbol = self.get_currency_symbol(self.currency)
            
            price = self._get_product_price(item[0],self.price_list,self.currency)
            
            price = price * item[1]
            
            price_string = symbol +"%.2f" % price
            
            # updating total price of items by iterating through a list of items
            total_price = total_price + float(price)

            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)
        
        total_price = symbol + "%.2f" % total_price
        
        # adding 'Total' to the receipt
        lines.append('Total: '+total_price)

        return lines
    
    def _get_product_price(self, product_code: str, price_list: list, receipt_currency: str) -> float:
        
        """Gets price for a product by referring to an external data source - JSON data file in this case

        Parameters:
        product_code (str): name of the product to be added to the cart
        price_list (list): list of products with their respective prices in JSON format
        currency_list (list): list of currencies with their respective conversion rates in JSON format
        receipt_currency(str): currency selected by the user during the transaction

        Returns:
        a float value for the product

       """
        
        price = 0.0
        
        default_currency="EUR"

        # fetching product prices from external JSON file
        for i in range(len(price_list)):
            
            if(price_list[i]['product_code'] == product_code):
                
                price = price_list[i]['price']
        
        # when the currency is not Euro
        if(receipt_currency != default_currency):
            
            conversion_rate = self.get_conversion_rate(receipt_currency)
            
            price = price * conversion_rate
        
        return price
  
def main():
    
    """Main function that controls the flow of execution of this script. It creates an instance of the class, adds items to
    the shopping cart and calls a function that prints the receipt showing those items

        Parameters:
        no parameters
        
        Returns:
        no return value

       """
        
    cart = ShoppingCart()
    
    cart.add_item("apple", 3)
    
    cart.add_item("banana", 6)
    
    cart.add_item("grapes", 1)
    
    cart.add_item("kiwi", 2)
    
    cart.add_item("strawberry", 1)
    
    receipt = cart.print_receipt()
    
    print("Items added in the shopping cart: ",receipt)

if __name__=="__main__":
    
    main()