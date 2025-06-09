from utils.file_operations import save_to_file, read_file

save_to_file("lol", "data.txt")
print(read_file("data.txt"))

print(__name__)