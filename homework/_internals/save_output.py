import csv
import os


def save_output(data, output_directory, filename):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_path = os.path.join(output_directory, filename)

    with open(output_path, "w", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["phrase", "target"])
        writer.writeheader()
        writer.writerows(data)