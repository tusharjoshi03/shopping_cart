from cart import ShoppingCart
import unittest

class TestShoppingCart(unittest.TestCase):
    
    def test_add_item(self):
        
        print('Testing add_item() for a single product (in Euro):')
        
        cart = ShoppingCart()
        
        cart.add_item("apple", 1)

        receipt = cart.print_receipt()
        
        assert receipt == ["apple - 1 - €1.00","Total: €1.00"], "Please select default currency (Euro) for this test case"
        
        print('** Test case passed successfully! **')
        
        print('--------------------------------------------------')
 
    def test_currency(self):
        
        print('Testing add_item() with GBP:')
        
        cart = ShoppingCart()
        
        cart.add_item("apple", 1)

        receipt = cart.print_receipt()

        assert receipt == ["apple - 1 - £0.85","Total: £0.85"], "Please select currency as GBP for this test case"
        
        print('** Test case passed successfully! **')
        
        print('--------------------------------------------------')
  
    def test_add_different_items(self):
        
        print('Testing add_item() for multiple products (in Euro):')
        
        cart = ShoppingCart()
        
        cart.add_item("banana", 1)
        
        cart.add_item("kiwi", 2)

        receipt = cart.print_receipt()

        assert receipt[0] == "banana - 1 - €1.10", "Please select default currency (Euro) for this test case"
        
        assert receipt[1] == "kiwi - 2 - €6.00", "Please select default currency (Euro) for this test case"
        
        assert receipt == ["banana - 1 - €1.10","kiwi - 2 - €6.00", "Total: €7.10"], "Please select default currency (Euro) for this test case"
        
        print('** Test case passed successfully! **')
        
        print('--------------------------------------------------')

    def test_total_price(self):
        
        print('Testing total price calculation for all products in the shopping cart (in Euro):')
        
        cart = ShoppingCart()
        
        cart.add_item("apple", 2)
        
        cart.add_item("banana", 1)
        
        cart.add_item("kiwi", 1)
        
        cart.add_item("strawberry", 1)

        receipt = cart.print_receipt()
        
        number_of_products = len(receipt)
        
        assert receipt[number_of_products-1] == "Total: €9.60", "Please select default currency (Euro) for this test case"
        
        print('** Test case passed successfully! **')
        
        print('--------------------------------------------------')

unittest.main()