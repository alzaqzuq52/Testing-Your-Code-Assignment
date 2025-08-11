"""
TestUnittest.py
unittest tests for the cash register app.
Run: python -m unittest -v
"""

import unittest
from InventoryItem import InventoryItem, ValidationError
from Order import Order

class TestInventoryItem(unittest.TestCase):
    def test_valid(self):
        it = InventoryItem("Banana 3lb", 1.25, 4)
        self.assertEqual(it.description, "Banana 3lb")
        self.assertEqual(it.price, 1.25)
        self.assertEqual(it.quantity, 4)
        self.assertAlmostEqual(it.line_total, 5.00, places=2)

    def test_description_rules(self):
        with self.assertRaises(ValidationError):
            InventoryItem("", 1.0, 1)
        with self.assertRaises(ValidationError):
            InventoryItem("Bad@Name", 1.0, 1)

    def test_price_rules(self):
        with self.assertRaises(ValidationError):
            InventoryItem("Thing", -1.0, 1)
        with self.assertRaises(ValidationError):
            InventoryItem("Thing", "x", 1)  # not a number

    def test_quantity_rules(self):
        with self.assertRaises(ValidationError):
            InventoryItem("Thing", 1.0, -1)
        with self.assertRaises(ValidationError):
            InventoryItem("Thing", 1.0, 2.5)  # must be int

    def test_set_quantity(self):
        it = InventoryItem("Candy", 0.99, 1)
        it.set_quantity(5)
        self.assertEqual(it.quantity, 5)
        self.assertAlmostEqual(it.line_total, 4.95, places=2)

class TestOrder(unittest.TestCase):
    def test_add_remove_updates_total(self):
        o = Order("2002")
        o.addItem(InventoryItem("Bread", 2.0, 2))  # 4.00
        o.addItem(InventoryItem("Milk", 3.0, 1))   # 3.00
        self.assertAlmostEqual(o.total, 7.0, places=2)

        removed = o.removeItem("Milk")
        self.assertTrue(removed)
        self.assertAlmostEqual(o.total, 4.0, places=2)

    def test_remove_missing(self):
        o = Order("3003")
        o.addItem(InventoryItem("Eggs", 2.5, 2))
        self.assertFalse(o.removeItem("Nope"))
        self.assertAlmostEqual(o.total, 5.0, places=2)

    def test_to_dict_has_basic_keys(self):
        o = Order("4004")
        o.addItem(InventoryItem("Juice", 3.25, 1))
        d = o.to_dict()
        for k in ["order_number", "order_date", "items", "total"]:
            self.assertIn(k, d)

if __name__ == "__main__":
    unittest.main(verbosity=2)
