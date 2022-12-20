#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.items_list = []

  def add_item(self, item_name, price, quantity=1):
    transaction_total = 0
    for _ in range(quantity):
      transaction_total += price 
      self.items.append(item_name)
    self.items_list.append(transaction_total)
    self.total += transaction_total


  def apply_discount(self):
    if self.discount > 0:
      self.total = int(self.total - (self.discount * .01) * self.total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    if len(self.items) > 0:
      self.items.pop()
      last_item = self.items_list.pop()
      self.total = round(self.total - last_item, 2)
    return self.total
    
