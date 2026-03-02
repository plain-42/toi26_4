import os

def create_file_if_not_exists(filename: str) -> None:
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            pass

def append_to_file(text: str, filename: str) -> None:
    create_file_if_not_exists(filename)
    with open(filename, "r") as f:
        lines = f.readlines()
        print(*(lines[::2]), sep="")
        
    with open(filename, "a") as f:
        f.write(text + "\n")

append_to_file("Пятая строка", "example.txt")
