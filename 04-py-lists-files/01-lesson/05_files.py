from pathlib import Path

print(f"Current directory {Path.cwd()}")
data_directory = Path("..") / "data"
prices_path = data_directory / "prices.txt"

print(data_directory)
print(f"Directory exsists: {data_directory.exists()}")
print(prices_path)


print("\n---\n")
# "with open" closes file  soon as block is done.

with open(prices_path, "r", encoding="utf-8") as file:
    #  file.read() reads all content into a string
    #  Greaat for small files. Specify character
    # count or read single lines at a time

    content = file.read()

print(content)

prices = []
with open(prices_path, "r", encoding="utf-8") as file:
    for line in file:
        price = float(line.strip())
        prices.append(price)

print(prices)

report_path = data_directory / "price_report.txt"

#Exisitng content is replaced
with open(report_path, "w", encoding="utf-8") as file:
    file.write("First line\n")

#Exisitng content is kept, new content is added to the end
with open(report_path, "a", encoding="utf-8") as file:
    file.write("Antother line\n")


report_lines = [
    "Item: Epler",
    "Amount: 20",
    "Price: 96.50"]
with open(report_path, "a", encoding="utf-8") as file:
    for line in report_lines:
        file.write(line +"\n")


# We have already done this, don`t do it again
with open(report_path, "r", encoding="utf-8") as file:
    content = file.read()

# But add this to the end of your program:
with open(report_path, "a", encoding="utf-8") as file:
    file.write("Kommentar: Husk blåbær og grøt!\n")

