items = ["Pencil", "Eraser", "Notebook", "Marker", "Ruler"]
stock_counts = [0, 5, 15, 7, 3]

inventory = {item:count for item, count in zip(items, stock_counts)}
print(inventory)


in_stock_items = {item: count for item, count in inventory.items() if count > 0}
print(in_stock_items)