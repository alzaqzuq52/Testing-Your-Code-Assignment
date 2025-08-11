"""
TestPytest.py
pytest tests for the cash register app.
Run: pytest -q
"""
import pytest
from InventoryItem import InventoryItem, ValidationError
from Order import Order

def test_line_total_rounds():
    it = InventoryItem("Gum", 0.3333, 3)
    assert it.line_total == round(0.3333 * 3, 2)

@pytest.mark.parametrize("bad_desc", ["", "Bad#", "No@pe"])
def test_bad_descriptions(bad_desc):
    with pytest.raises(ValidationError):
        InventoryItem(bad_desc, 1.0, 1)

def test_addItem_type_check():
    o = Order("X1")
    with pytest.raises(TypeError):
        o.addItem("not item")  # should be InventoryItem

def test_change_quantity_and_recalc():
    o = Order("Y2")
    it = InventoryItem("Rice", 4.0, 1)
    o.addItem(it)
    assert o.total == 4.0
    it.set_quantity(3)
    o._recalculate_total()
    assert o.total == 12.0
