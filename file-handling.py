# file = open('file-handling.txt')
# data = file.read()
# data = file.readline()
# data = file.read(50)
# data = file.readlines()
# for line in data:
#     print(line)
# print(data)

# file = open('file2.txt', 'a')
# data = "My first file...."
# file.write(data)
# file.read()

# file = open('file3.txt', 'a+')
# # data = file.read()
# # print(data)
# file.write("Latest data")

file = open('image.jpg', 'rb')
data = file.read()
file = open('copied_image.jpg', 'wb')
file.write(data)