import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        rows = []
        for row in reader:
            formatted_row = {key: f"{float(value):.6f}" for key, value in row.items()}
            rows.append(formatted_row)

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
