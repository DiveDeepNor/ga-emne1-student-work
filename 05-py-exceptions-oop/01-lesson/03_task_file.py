from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
path = data_folder / "report.txt"
print(path)

try:
    with path.open("w", encoding= "utf-8") as file:
        file.write("Practice report\n ")

except FileNotFoundError:
    print(f"Error, could not find file: {path}")
except PermissionError:
    print(f"Error, you dont have correct permission to: {path}")