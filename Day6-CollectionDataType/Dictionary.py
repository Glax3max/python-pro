# Properties of dictionary
    # indexed
    # no duplicates allowed
    # unordered
    # modifiable 
    # paired(key:value)

# Creating dictionary
desc = dict()

desc = {'key1':'item1','key2':'items2','key3':'items3','key4':'items4'}
print(desc)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person) #The dictionary above shows that the datatype of a dictionary can be anything

print(len(person))

# Accessing Dictionary items
print(person['first_name'])

# Adding items to a Dictionary
person['frients'] = 0
print(person)

# Modifying Items in a Dictionary
person['friends'] = 1000000
print(person)

# Checking key in  a Dictionary
print('friends' in person)

# Removing key and value pair from a Dictionary
person.pop('friends')
print(person)