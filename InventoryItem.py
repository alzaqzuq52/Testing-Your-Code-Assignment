"""
InventoryItem.py
Simple InventoryItem class for the cash register app.
- Description: letters/numbers/spaces only
- Price: float (non-negative)
- Quantity: int (non-negative)
"""

class ValidationError(ValueError):
    pass

def _is_alnum_space(text):
    # allow spaces; remove them and check the rest are letters/numbers
    if not isinstance(text, str):
        return False
    return text.replace(" ", "").isalnum()

class InventoryItem:
    def __init__(self, description, price, quantity=0):
        # store and then validate
        self.description = description
        self.price = price
        self.quantity = quantity
        self._validate()

    def _validate(self):
        # description: not empty and only letters/numbers/spaces
        if not isinstance(self.description, str) or not self.description:
            raise ValidationError("Description must be a non-empty string.")
        if not _is_alnum_space(self.description):
            raise ValidationError("Description must be letters/numbers/spaces only.")

        # price: numeric and not negative
        if not isinstance(self.price, (int, float)):
            raise ValidationError("Price must be a number.")
        self.price = float(self.price)
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")

        # quantity: int and not negative
        if not isinstance(self.quantity, int):
            raise ValidationError("Quantity must be a whole number (int).")
        if self.quantity < 0:
            raise ValidationError("Quantity cannot be negative.")

    @property
    def line_total(self):
        # total for this item
        return round(self.price * self.quantity, 2)

    def set_quantity(self, qty):
        # change quantity safely
        if not isinstance(qty, int):
            raise ValidationError("Quantity must be a whole number (int).")
        if qty < 0:
            raise ValidationError("Quantity cannot be negative.")
        self.quantity = qty
