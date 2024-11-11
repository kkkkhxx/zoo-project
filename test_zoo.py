import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
    

    # Add your additional test cases here.
    def test_child5_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    def test_child0_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_child1_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(1), 50)

    def test_child11_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(11), 50)

    def test_child12_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)


    # Add your additional test cases here.
    def test_teen15_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_teen13_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_teen14_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(14), 100)

    def test_teen19_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def test_teen20_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    # Add your additional test cases here.
    def test_ad25_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(25), 150)

    def test_ad21_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_ad22_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(22), 150)

    def test_ad59_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(59), 150)

    def test_ad60_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    # Add your additional test cases here.
    def test_old61_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test_old65_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100)

    # Add your additional test cases here.
    def test_inv_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid")


if __name__ == '__main__':
    unittest.main()
