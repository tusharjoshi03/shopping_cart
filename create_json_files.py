import json

def create_products_json():
    
    """creates a JSON file from a dictionary object containing product codes and their respective quantities

        Parameters:
        no parameters
        
        Returns:
        no return value

       """
    
    product_prices = {
        
        'products' : [
            {
                'product_code' : 'apple',
                'price' : 1.0,
            },
            {
                'product_code' : 'banana',
                'price' : 1.1,
            },
            {
                'product_code' : 'kiwi',
                'price' : 3.0,
            },
            {
                'product_code' : 'grapes',
                'price' : 2.0,
            },
            {
                'product_code' : 'strawberry',
                'price' : 3.5,
            }
        ]
    }
    
    # convert dict into string format
    product_prices_string = json.dumps(product_prices,indent=4)
    
    # write converted data to a JSON file
    with open('products_2.json', 'w') as prices_file:
        prices_file.write(product_prices_string)
        
def create_currency_json():
    
    """creates a JSON file from a dictionary object containing currencies, associated symbols and their respective
    conversion rates considering 'Euro' as the base currency

        Parameters:
        no parameters
        
        Returns:
        no return value

       """
    
    currency_conversion_rates = {
        'currencies' : [
            {
                'currency' : 'EUR',
                'rate' : 1.00,
                'symbol': '€'
            },
            {
                'currency' : 'USD',
                'rate' : 1.00,
                'symbol': '$'
            },
            {
                'currency' : 'GBP',
                'rate' : 0.85,
                'symbol': '£'
            },
            {
                'currency' : 'AUD',
                'rate' : 1.45,
                'symbol': '$'
            },
            {
                'currency' : 'JPY',
                'rate' : 137.05,
                'symbol': '¥'
            }
        ]
    }
    
    # convert dict into string format
    currency_conversion_rates_string = json.dumps(currency_conversion_rates,indent=4)
    
    # write converted data to a JSON file
    with open('currencies.json', 'w') as currencies_file:
        currencies_file.write(currency_conversion_rates_string)
        
def main():
    
    """Main function that controls the flow of execution of this script. It calls a function that creates JSON file of
    items containing product code and their respective quantities

        Parameters:
        no parameters
        
        Returns:
        no return value

       """
    
    # create JSON file for product prices
    create_products_json()
    
    # create JSON file for currency conversion rates
    create_currency_json()
    
if __name__=="__main__":
    
    main()

