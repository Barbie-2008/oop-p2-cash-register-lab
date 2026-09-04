#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not a valid discount. Please enter a number between 0 and 100.")

    def add_item(self, item, price, quantity=1):
        subtotal = price * quantity
        self.total += subtotal
        self.items.extend([item] * quantity)
        self.last_transaction_amount.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if not self.discount:
            print("There is no discount to apply.")
            return
        discount_amount = (self.total * self.discount) / 100
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        if not self.last_transaction_amount:
            print("There are no transactions to void.")
            return
        last_transaction = self.last_transaction_amount.pop()
        item_total = last_transaction["price"] * last_transaction["quantity"]
        self.total -= item_total

        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])


