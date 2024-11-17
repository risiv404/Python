import json

INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE, 'r', encoding="utf-8") as file:
        data = json.load(file)
    total_sum = sum(item["score"] * item["weight"] for item in data)

    return round(total_sum, 3)

if __name__ == '__main__':
    print(task())
