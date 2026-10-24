from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
path = data_folder / "message.txt"
print(path)

try:
    with path.open(encoding= "utf-8") as file:
        number = file.read()
    print(number)
except FileNotFoundError:
    print(f"Error, could not find file: {path}")


path = data_folder / "number.txt"
print(path)

try:
    with path.open(encoding= "utf-8") as file:
        number = int(file.read().strip())
    print(number*2)
except FileNotFoundError:
    print(f"Error, could not find file: {path}")
except ValueError:
    print("The file must contain a integer")