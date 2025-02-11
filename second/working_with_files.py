test_file_1_location = "../resources/test-file-1.txt"
with open(test_file_1_location) as file:
    print(file.read())
    print(file.read())

    if file.seekable():
        file.seek(0)
        print(file.read())

    file.seek(0)
    print(file.readlines())

test_file_2_location = "../resources/test-file-2.txt"
with open(test_file_2_location, "w") as file:
    file.write("Alex Alex")

with open(test_file_2_location, "a") as file:
    file.write("\nTimur, Timur")

with open(test_file_2_location, "r") as file:
    content = file.read()
    print(content)
