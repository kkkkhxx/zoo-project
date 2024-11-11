import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_child0_12_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_child0_12_0ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    # Add your additional test cases here.
    def test_teen13_20_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_teen13_20_20ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    # Add your additional test cases here.
    def test_ad21_60_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    
    def test_ad21_60_21ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    # Add your additional test cases here.
    def test_ad_60up_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    # Add your additional test cases here.
    def test_inv_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid")


if __name__ == '__main__':
    unittest.main()
