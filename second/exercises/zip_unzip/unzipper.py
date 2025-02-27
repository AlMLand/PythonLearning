import pathlib
import zipfile


class Unzipper:
    @staticmethod
    def unzip_file(file_path: pathlib.Path, destination: pathlib.Path):
        with zipfile.ZipFile(file_path, "r") as uf:
            uf.extractall(destination)
