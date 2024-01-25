import unittest
from stock import Stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_keywords(self):
        s = Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = Stock('GOOG', 100, 490.1)
        s.sell(50)
        self.assertEqual(s.shares, 50)

    def test_from_row(self):
        s = Stock.from_row(['ABAB', 22, 35.5])
        self.assertEqual(s.name, 'ABAB')
        self.assertEqual(s.shares, 22)
        self.assertEqual(s.price, 35.5)

    def test_repr(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

    def test_eq(self):
        s = Stock.from_row(['ABAB', 22, 35.5])
        t = Stock('GOOG', 100, 490.1)
        u = Stock('GOOG', 100, 490.1)
        self.assertTrue(t == u)
        self.assertFalse(s == t)

    def test_set_string_shares_fail(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '50'

    def test_set_negative_shares_fail(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -50

    def test_set_string_price_fail(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = '250.1'

    def test_set_negative_price_fail(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -50.6

    def test_set_non_existent_attr_fail(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 50


if __name__ == '__main__':
    unittest.main()
