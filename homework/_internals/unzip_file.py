import os
import zipfile


def unzip_file(zip_path):
    if not os.path.exists("files/input"):
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall("files")