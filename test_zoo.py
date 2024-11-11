import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    # Add your additional test cases here.
    def test_teen13_20_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    # Add your additional test cases here.
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
