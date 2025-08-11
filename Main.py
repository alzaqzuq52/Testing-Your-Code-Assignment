"""
Main.py
Small demo to show the classes working.
Run: python Main.py
"""

from InventoryItem import InventoryItem, ValidationError
from Order import Order

def print_receipt(order):
    data = order.to_dict()
    print("=" * 32)
    print(f"Order #: {data['order_number']}")
    print(f"Date:    {data['order_date']}")
    print("-" * 32)
    for it in data["items"]:
        line = f"{it['description']} x{it['quantity']} @ ${it['price']:.2f} = ${it['line_total']:.2f}"
        print(line)
    print("-" * 32)
    print(f"TOTAL: ${data['total']:.2f}")
    print("=" * 32)

def main():
    order = Order("1001")
    try:
        order.addItem(InventoryItem("Apple 2lb", 3.49, 2))
        order.addItem(InventoryItem("Milk 1gal", 4.19, 1))
        order.addItem(InventoryItem("Bread", 2.50, 3))
    except ValidationError as e:
        # simple error handling
        print("Problem with item:", e)

    # show remove works
    order.removeItem("Milk 1gal")
    print_receipt(order)

if __name__ == "__main__":
    main()
