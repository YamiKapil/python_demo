# file = open('text.txt')

# read all the contents of the file
# print(file.read())
# read only 2 bytes/characters
# print(file.read(2))
# read the file line wise line
# print(file.readline())  # read the first line
# print(file.readline())  # read the second line


# print all the content line by line using readLine method
# line = file.readline()
# while line != '':
#    print(line)
#    line = file.readline()

# another method is, this will give the file in list
# line = file.readlines()
# for line in file.readlines():
#    print(line)

# file.close()


# writing in the file
# when opening this way we don't have to close the file
# give a flag r to open in read mode and w to open in write mode

# reversing the file list and writing back to file
with open('text.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)







