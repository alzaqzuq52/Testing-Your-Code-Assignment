"""
Order.py
Order class holds InventoryItem objects, order number, date, and total.
"""

from datetime import datetime
from InventoryItem import InventoryItem

class Order:
    def __init__(self, order_number):
        self.order_number = str(order_number)
        self.order_date = datetime.now()
        self.items = []
        self.total = 0.0

    def _recalculate_total(self):
        # add up each item's line_total
        t = 0.0
        for it in self.items:
            t += it.line_total
        self.total = round(t, 2)

    def addItem(self, item):
        # only let InventoryItem objects in
        if not isinstance(item, InventoryItem):
            raise TypeError("addItem expects an InventoryItem.")
        self.items.append(item)
        self._recalculate_total()

    def removeItem(self, description):
        # remove the first matching item by description (case-insensitive)
        desc = str(description).lower()
        for i, it in enumerate(self.items):
            if it.description.lower() == desc:
                del self.items[i]
                self._recalculate_total()
                return True
        return False

    def to_dict(self):
        # basic dict for printing or testing
        data = {
            "order_number": self.order_number,
            "order_date": self.order_date.isoformat(timespec="seconds"),
            "items": [],
            "total": self.total
        }
        for it in self.items:
            data["items"].append({
                "description": it.description,
                "price": it.price,
                "quantity": it.quantity,
                "line_total": it.line_total
            })
        return data
