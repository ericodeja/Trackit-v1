import json


file_path = "db/habits.json"
all_habits = {}


def read_db(value):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            value.update(data)
    except FileNotFoundError:
        value = {}
read_db(all_habits)


def write_db(value):
    all_habits.update(value)
    with open(file_path, "w") as file:
        json.dump(all_habits, file, indent=4)
