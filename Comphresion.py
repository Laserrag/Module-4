items = ["Pencil", "Eraser", "Notebook", "Marker", "Ruler"]
stock_counts = [0, 5, 15, 7, 3]

inventory = {item:count for item, count in zip(items, stock_counts)}
print(inventory)


in_stock_items = {item: count for item, count in inventory.items() if count > 0}
print(in_stock_items)

chosen_item = input("Enter the item you want to check: ")
if chosen_item in inventory and inventory[chosen_item] > 0:
    print("The value of ", inventory[chosen_item])
    print(f"{chosen_item} is in the inventory.")
else:
    print(f"{chosen_item} is not in the inventory.")
