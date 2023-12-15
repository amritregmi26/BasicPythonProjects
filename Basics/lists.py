items = list(("John", "Jane", "Harry", "William", "Oliver"))

# insert method is used to add items to specified index
items.insert(2,"Taylor")

# replacing items using slicing
items[1:3] =["Ross", "Kevin", "Shawn"]

# append is used to add items to end of the list
items.append("James")

# extend method is used to append same/another list to current list
items2 = ["Kobe", "Shaq", "Lebron"] 
items.extend(items2)

# remove method is used to remove specified item from the list
items.remove("Lebron")

# pop method is used to remove item from specified index or remove last element from the list
# items.pop() # removes last
# items.pop(1) # removes second

# clear method is used to clear the list
# items.clear()

# List Comprehension
items3 = [item for item in items if "e" in item] # adds item to list 3 that has e in it

# reverse method is used to reverse list items
items.reverse()

# sort method is used to sort the list items
items.reverse()

#count method is used to check how many times the specified value is repeated in the list
items.count("Kobe")