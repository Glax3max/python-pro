# Properties of set
    # Unordered
    # immutable
    # unindexed
    # no duplicates allowed

# Possible operations on sets are: 
    # finding Union - s1.union(s2)
    # finding Intersection - s2.intersection(s2)
    # Check subset - s1.issubset(s2)
    # Check superset - s1.issuperset(s2)
    # Difference between sets - s1.difference(s2)
    # Finding Symmetric Difference between the sets:   s1.symmetric_differnce(s2)   , which means (A\B)U(B\A)
    # Joining sets : s1.isdisjoint(s2)  - gives boolean

# Creating set
st1 = {'items1','items2','items3','items4'}
st2 = {'items2','items3'}
print(st1)

# Getting the length
print(len(st1))

# finding union
s3 = st1.union(st2)
print(s3)