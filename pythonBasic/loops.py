# python loops

# if else loop
greeting = 'Good Morning'

if greeting == 'Good Morning':
    print('condition matches')
else :
    print('condition not matched')
print('independent of if else condition')

# for loop
obj = [2, 3, 4, 5]
for i in obj:
    print(i)

# sum of first natural numbers
summation = 0
for j in range(1, 6):  # range(i, j) -> iterate from i to j-1
    summation = summation + j
print(summation)

for k in range(1, 10, 2):  # jump 2 index for every loop
    print(k)

for m in range(10):
    print(m)


# while loop

it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue  # skip this and continue from the next iteration
    if it == 3:
        break  # will break out of while loop
#    if it != 3:  # will print all except 3
    print(it)
    it = it - 1

print('while loop is done')
