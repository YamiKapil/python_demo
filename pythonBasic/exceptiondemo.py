itemsincart = 0
# 2 items will be added to cart

if itemsincart != 2:
    # raise Exception('product cart count not matching')
    pass

# another way is assertion
# assert (itemsincart == 2)
# if the condition is not true it will throw error


# try catch in python, python use except instead of catch
try:
    with open('text1.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)  # gives the Exception message
    print('something went wrong')  # give your own message
finally:  # will run all the time even in success and even in failure
    print('will always run')


