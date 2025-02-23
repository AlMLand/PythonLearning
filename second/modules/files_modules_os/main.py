import os
import shutil
from pathlib import Path

test_file = "test-file.txt"
with open(test_file, "w+") as file:
    file.write("this is a test file")

print(os.getcwd())
print(os.listdir())
print(os.listdir("C:\\Users\\All Users"))

####

test_dir = "test_dir"

if test_dir not in (os.listdir(os.getcwd())):
    os.makedirs(test_dir)
    print(f"create directory {test_dir}")

if test_file not in os.listdir(f"{os.getcwd()}\\{test_dir}"):
    shutil.move(test_file, test_dir)
    print("move file: " + test_file + " from directory: " + os.getcwd().split("\\")[-1] + " to directory: " + test_dir)

for file in os.listdir(f"{os.getcwd()}\\{test_dir}"):
    full_qualified_path = os.path.join(os.getcwd(), f"{test_dir}\\{test_file}")
    os.remove(full_qualified_path)
    print(f"remove file: {test_file}")

if Path(test_dir).exists():
    os.rmdir(test_dir)
    print(f"remove directory: {test_dir}")
