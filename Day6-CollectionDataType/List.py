lst = ["Apple",'banana','Orange','Guava']
lst2 = lst.copy()
print(lst2)

lst2.insert(2,'4')
print(lst2)

# Unpacking list items
first_item,second_item,*rest = lst2
print(first_item,second_item,rest)

# Slicing items
lst3 = lst.copy()

all_fruits = lst3[1:3]
print(all_fruits)

# Checking items in a List
apple_Exist = 'Apple' in lst
print(apple_Exist)

# removing items and deleting items
lst3.remove('Apple')
print(lst3)

del lst3[2]
print(lst3)


# Clearing all items from a list
lst3.clear()
print(lst3)

# Joining Lists
lst = lst + lst2 + lst3
print(lst)