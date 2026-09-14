# Lists: Made with [], we can change content

characters = ["Kermit", "Miss Piggy", "Gonzo"]
characters.append("Fozzie")
characters[0] = "Miss Piggy"
print(characters)

#Tuples. Made with (), no item assignemnt, no growth or shrinkage
coordinates = (59.91, 10.75)
print(characters[0])
print(characters[1])

# Append virker ikke

# Men dette er fint
mixed_tuple = ("Njaal", 39, True)

print("\n---\n")

#Dictionatires: key + value pairs, made with {} and :

muppet = {
    "name": "Kermit",
    "species": "Frog",
    "job": "Host"
}

print(muppet["name"])
print(muppet["job"])
