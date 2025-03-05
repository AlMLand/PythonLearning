from pathlib import Path

from second.exercises.zip_unzip.directory import Directory
from second.exercises.zip_unzip.unzipper import Unzipper

Unzipper.unzip_file(Path("unzip_me_for_instructions.zip"), Path("exercise"))
directory = Directory(Path("exercise\\extracted_content"))
files = directory.find_files_recursive(r"\d{3}-\d{3}-\d{4}")
