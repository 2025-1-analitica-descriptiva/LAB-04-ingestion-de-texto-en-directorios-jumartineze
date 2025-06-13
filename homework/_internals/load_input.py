import glob
import os


def load_input(input_directory):
    sequence = [
        {"phrase": open(file, "r", encoding="utf-8").read(), "target": os.path.basename(folder)}
        for folder in glob.glob(f"{input_directory}/*")
        for file in glob.glob(f"{folder}/*")
    ]
    return sequence