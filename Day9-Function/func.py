def function_name(name) :
    print("Hey there , This is Abhishek",name)

function_name("Raj")


def print_FullName(first_Name,last_Name):
    spc = " "
    fullName = first_Name + spc + last_Name
    print(fullName)

print_FullName("Abhishek","Gupta")

#  returning function
def addNum(a,b) :
    return a+b

print(addNum(3,4))


# Arbitrary Number of parameters in functions

def many_Items(*args):
    for it in args:
        print(it)

many_Items(4,2,2,545,4,5,5)