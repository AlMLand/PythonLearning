import zipfile

_package = "files\\"

file_name_to_content = {
    f"{_package}file1.txt": "This is a first text file",
    f"{_package}file2.txt": "This is a second text file",
}

for file_name, content in file_name_to_content.items():
    with open(file_name, "w+") as file:
        file.write(content)

# compressing the files
with zipfile.ZipFile(f"{_package}compressed_file.zip", "w") as zip_file:
    for file_name in file_name_to_content.keys():
        zip_file.write(file_name, compress_type=zipfile.ZIP_DEFLATED)

# uncompress the files
with zipfile.ZipFile(f"{_package}compressed_file.zip", "r") as zip_file:
    zip_file.extractall(f"{_package}uncompressed_files")

# compressing the directory
with zipfile.ZipFile(f"{_package}compressed_directory.zip", "w") as zip_file:
    zip_file.write(f"{_package}uncompressed_files", compress_type=zipfile.ZIP_DEFLATED)
