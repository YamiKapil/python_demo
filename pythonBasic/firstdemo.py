# writing the comments use '#'
# printing in the python
print('hello ')
# variables
a = 3
# no need to define the data type like int/double/float
print(a)

Str = "hello world"
print(Str)
b, c, d = 5, 6.4, "great"
print(b, c, d)
# printing the datatype other than string
print("{} {}".format("Value is ", b))
print(type(b))  # getting the variable type

# list data type
values = [1, 2, 'rahul', 'helo', 4.4, ]
# note: can pass different datatype in the list in python

print(values[0])  # output will be 1
print(values[-1])  # prints the last index of the list with -1
# getting the sublist from 2 to rahul
print(values[1:3])
# inserting the word
values.insert(3, 'hoho')
print(values)
# 'append' will add the value to the last of the list
del values[0]  # will delete the value of index 0

# tuple data type
# tuple data type is immutable (cannot update tuple after declaration)
# for tuple it should be small bracket "()"
val = (1, 2, "test", 4.4)
print(val[1])

# dictionary data type
# similar to list and tuple but should be curly braces "{}"
# it has a key value pair
dictVal = {1: "first value", "age": 22, 2: "second value"}

# creating dictionary during runtime
newDict = {}
newDict["firstName"] = "Test"
newDict["lastName"] = "Last"
print(newDict)



