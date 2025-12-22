language = "python"
lst  = list(language)
print(type(lst))
print(len(lst))

lst2 = [i for i in language]
print(type(lst2))
print(lst2)

numbers = [i for i in range(11)]
print(numbers)

numbers2 = [i*i for i in range(11)]
print(numbers2)

numbers3 = [(i,i*i) for i in range(11)]
print(numbers3)

number4 = [i for i in range(21) if i%2 == 0]
print(number4)