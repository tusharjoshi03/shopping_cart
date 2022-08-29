import typing
import json
import abc_class as abc # Renamed abc.py to abc_class.py as 'abc' is a python module for defining abstract base class

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
    
    def print_receipt(self) -> typing.List[str]:
        
        """lists and prints all the items in the shopping cart in the order in which items are added

        Parameters:
        none, except the reference to point to the class object

        Returns:
        a list of strings where each element in the list represents an item in the shopping cart along with its quantity and
        price.

       """
        
        lines = []
        
        total_price = 0.0

        for item in self._items.items():
            
            price = self._get_product_price(item[0]) * item[1]

            price_string = "€%.2f" % price
            
            # updating total price of items by iterating through a list of items
            total_price = total_price + float(price)

            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)
            
        total_price = "€%.2f" % total_price
        
        # adding 'Total' to the receipt
        lines.append('Total: '+total_price)

        return lines
    
    def _get_product_price(self, product_code: str) -> float:
        
        """Gets price for a product based on product code

        Parameters:
        product_code (str): name of the product to be added to the cart

        Returns:
        a float value for the product

       """
        
        price = 0.0

        if product_code == 'apple':
            price = 1.0

        elif product_code == 'banana':
            price = 1.1

        elif product_code == 'kiwi':
            price = 3.0
            
        elif product_code == 'grapes':
            price = 2.0
            
        elif product_code == 'strawberry':
            price = 3.5

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
    
    cart.add_item("strawberry", 2)
    
    cart.add_item("kiwi", 1)
    
    receipt = cart.print_receipt()
    
    print("Items added in the shopping cart: ",receipt)

if __name__=="__main__":
    
    main()