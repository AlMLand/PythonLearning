import pathlib
import re


class Directory:
    def __init__(self, start_direction: pathlib.Path):
        self.start_direction = start_direction

    def all_dirs(self) -> list:
        return [directory for directory in self.start_direction.iterdir() if directory.is_dir()]

    @staticmethod
    def all_files(directory) -> list:
        return [file for file in directory.iterdir() if file.is_file()]

    def find_files(self, regex: str) -> list:
        files = []
        for directory in self.all_dirs():
            for file in self.all_files(directory):
                with open(file, "r") as reading_file:
                    content = reading_file.read()
                    matcher = re.search(regex, content)
                    if matcher:
                        files.append(file.name)
                        print(f"Found text: {matcher.group()} in file: {file.name}")
        return files

    @staticmethod
    def all_dirs_for_recursive(directory: pathlib.Path) -> list:
        return [d for d in directory.iterdir() if d.is_dir()]

    def find_files_recursive(self, regex: str, directory: pathlib.Path = None) -> list:
        if directory is None:
            directory = self.start_direction

        files = []
        for file in self.all_files(directory):
            with open(file, "r") as reading_file:
                content = reading_file.read()
                matcher = re.search(regex, content)
                if matcher:
                    files.append(file.name)
                    print(f"Found text: {matcher.group()} in file: {file.name}")

        for subdir in self.all_dirs_for_recursive(directory):
            files.extend(self.find_files_recursive(regex, subdir))

        return files
