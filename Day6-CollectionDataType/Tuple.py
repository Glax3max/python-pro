# Property of Tuples
    # Ordered
    # Unmutable
    # Allows duplicates
# We cannot use add,insert ,remove methods in tuple because it is not modifiable

# Methods of tuples are:
    # tuple():to create an empty tuple
    # count():to count the number of a specified item in a tuple 
    # index():to find the index of a specified item in a tuple 
    #  .(dot) :operator to join two or more tuples and to create a new tuple

# Creating a tuple
    # Creating an empty tuple
empty_tuple = ()

empty_tuple = tuple()


# syntax
tpl = ('items1','items2','items3','items4')
fruits = ('apple','banana','orange','mango','lemon')


# tuple length
print(len(tpl))
print(len(fruits))

# Accessing tuple items
print(fruits[2]) #positive index

print(fruits[-1]) #Negative index

# Slicing  tuples
print(fruits[0:5])

# Changing tuple to list and list to tuple
newList = list(tpl)
print(newList)

newTuple = tuple(newList)
print(newTuple)

# Checking an item in a tuple
print('items3' in tpl)
print('items34' in tpl)

# joining tuples
tuple1 = ('Tiger','lion','Deer','bear')
tuple2 = ('Cat','Dog','Horse')
resultant_Tuple = tuple1 + tuple2
print(resultant_Tuple)