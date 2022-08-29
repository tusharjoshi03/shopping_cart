# shopping_cart
Add items to the shopping cart and generate a receipt with total price of all items in the selected currency

This shopping till system project provides functionality to add different items to shopping cart, display their quantities and prices, display all items and their total price on receipt and select differet currencies for a transaction. Overview pf the steps followed to implement this project are described below:

1. Add different items with varying quantity to the shopping cart and display them in the same order on receipt.
2. Calculate total price for a transaction by adding up cost of each item and display total price on receipt.
3. Implement functionality to fetch product prices from an external source such as a JSON file.
4. Display product prices in different currencies using API: This approach worked successfully, but there is a limit to number of requests that can be sent to this API. Hence, I decided to include another option to get conversion rates for different currencies. The code for the API approach can be found in the commit history of the 'cart.py' script.
5. Display product prices in different currencies using a JSON file: In this approach, I created a JSON file (similar to the one for product prices) and fetched conversion rates for different currencies from this file. Along with conversion rates, symbols for those currencies were also added to the JSON file. The currencies considered for this approach are: Euro (EUR), United States Dollar (USD), Pound Sterling (GBP), Australian Dollar (AUD) and Japanese Yen (JPY).
6. Update the testing script to cover more test cases and make it more robust to changing requirements.
7. Documentation: Code clean up, adding comments for classes, functions and statements to increase readability of the code.

# Description for each script:

1. abc_class.py:
This script contains is an abstarct class that is used by the shopping till system. It contains two methods: add_item() and print_receipt()

2. cart.py:
This script contains the implementation to display items in the shopping cart on receipt, calculate and display their total price on receipt, read product prices from an external source (JSON file) and display product prices in different currencies. Currency for a particular transaction can be selected at the beginning, and all items on the receipt along with the total price will be displayed in the selected currency.

3. create_json_files.py:
This script creates JSON files for product prices and currency converison rates.

4. test_cart.py:
This script contains functions that test the functionality of 'cart.py' using several test cases. More test cases can be added to this script as per requirement.

# JSON Files:

1. products.json:
Contains product code along with their prices in JSON format

2. currencies.json:
Contains symbols and conversion rates for different currencies considering 'Euro' as the base currency

# Executing the code:

1. Clone the repository or download the zip file from the 'Code' tab.
2. Unzip the downloaded file. Open terminal from the command prompt and navigate to the directory where the unzipped code directory is present.
3. Run 'python3 cart.py' to execute 'cart.py' and verify all the functionalities.
4. Run 'python3 test_cart.py' to execute 'test_cart.py' to run test cases that are defined in the script.
5. To add more items or change product prices, the file 'products.json' can be updated as per requirement.
6. To add more currencies or change conversion rates, the file 'currencies.json' can be updated as per requirement.

Note: Python version used for implementation and testing was 3.6.5
