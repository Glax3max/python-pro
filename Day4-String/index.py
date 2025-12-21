multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String concatenation
fname = "ABhishek"
lname = "Gupta"
space = " "

print(fname + space + lname)


# Escape Sequences in Strings

# new line('\n)
print("Abhsihek\nGupta")

# Tab (means 8 space)
print("Abhishek\tGupta")

#Backslash
print("car\\truck")

# Single quote(')
print('Abhishek\'')

# double quote(")
print('\"Stay Happy and keep pushing ur self\"')


# Making table with the use of tab (\t)

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"')


# String formatting

first_name = "Raj"
last_name = "Kumar"
age = 32

detail = 'My name is {} {}.I am {} years old'.format(first_name,last_name,age)
print(detail)

# String interpolation

a = 4
b = 3
print(f'{a} + {b} = {a+b}')

# Python Strings as Sequences of Characters


    # Unpacking Characters(Destructuring)
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


