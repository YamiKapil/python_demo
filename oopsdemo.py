# classes are user defined blueprint or prototype
# eg: in a class name Calculator there are methods like sum, subtract etc.
# in class we have methods, class variables, instance variables, constructors

class Calculator:
    num = 100 # class variables
    # default constructor

    def __init__(self,a,b):
        self.firstNumber = a # instance variable
        self.secondNumber = b
        print('i am called automatically')

    def getData(self):
        print('i am now executing as method in class')

    def summation(self):
        return self.firstNumber + self.secondNumber


obj = Calculator(3, 5)  # syntax to create object in python
obj.getData()

obj1 = Calculator(6, 2)
print(obj.summation())

# self keyword is mandatory for calling variable names into method
# instance and class variables is different
# constructor name should be __init__
# new keyword is not required when creating object


# Inheritance in Python

class ChildClass(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getcompletedata(self):
        return self.num2 + self.num+self.summation()


childObj = ChildClass()
print(childObj.getcompletedata())






