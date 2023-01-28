# file = open('test.txt')
# # print(file.read(2))
# # print(file.readline())
# # print(file.readline())
# while file.readline() != "":
#     print(file.readline())
# file.close()

with open('test.txt', 'r') as read_file:
    read = read_file.readlines()
    reversed(read)
    with open('test2.txt', 'w') as write_file:
        for i in reversed(read):
            write_file.write(i)


