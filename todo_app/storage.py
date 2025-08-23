import json
from json.decoder import JSONDecodeError
from todo_app.config import FILE_NAME


def load_todos():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return []


def save_todos(todos):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(todos, file, indent=4)
    except IOError:
        print("\nError: Gagal menyimpan data.")
