class CashRegister:
    def __init__(self, discount=0):
        # Initialize total, last transaction, and an empty items list
        self.total = 0
        self.last_transaction = 0
        self.items = []  # Track added items
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        # Add items and increase total
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([title] * quantity)  # Add the item 'quantity' times

    def apply_discount(self):
        # Apply discount and update total
        if self.discount > 0:
            self.total -= (self.total * (self.discount / 100))
            self.total = round(self.total, 2)  # Round the total to 2 decimal places
            # Format the total to avoid .0 if it's a whole number
            print(f"After the discount, the total comes to ${self.total:.0f}." if self.total.is_integer() else f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Undo the last transaction
        self.total -= self.last_transaction
        self.last_transaction = 0

    def get_items(self):
        return self.items  # Return a list of item names only
