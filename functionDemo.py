# function in python
# def is identifier needed to create a function
def greetme():
    print('good morning')


def greetme2(name):
    print('good morning ' + name)


def addints(a, b):
    print(a+b)
    # return a+b  # can also return back the value


# calling the function
greetme()


# parameterized function
greetme2("this is string")
addints(3, 4)
