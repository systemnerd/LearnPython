my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()
print(file_content)


user_name = input('Enter your name: ')

my_file_write = open('data.txt', 'w')
my_file_write.write(user_name)

my_file_write.close()
