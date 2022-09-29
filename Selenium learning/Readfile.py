
# open the file by giving path of file
file=open("test.txt")
#print(file.read()) # To read whole file
#print((file.read())) # to read n no. of characters

# print('using readine----- ')
# line =file.readline()
# while line!='':
#     print(line)
#     line=file.readline()

print('using readlines---for loop')

for line in file.readlines():
    print(line)

