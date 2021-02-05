import os
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

fileName = str(sys.argv[1])
print("\t[FILENAME]", fileName)

source = f"C:\\Users\\toufi\\Downloads\\{fileName}"     
path = "C:\\Users\\toufi\\OneDrive\\Documenten\\s4"     # Deze moet veranderd worden iedere keer dat we een nieuw semester hebben
directories = None
choice = None

def isDirectory(name):
    filepath = f"{path}\\{name}"
    return os.path.isdir(filepath)

def dirCommand(path):
    # Print de mogelijke mappen om naar te moven
    global directories
    directories = os.listdir(path)
    filter(isDirectory, directories)
    if directories:
        print("\n\t[MAPPEN]\n")
        for directory in directories:
            print(f"\t{directory}")

while True:
    dirCommand(path)
    if not directories or not choice:
        break
    else: 
        choice = input("\n\tBij welke map hiervan hoort dit bestand?: ")
        chosenFolder = process.extractOne( query=choice, choices=directories, scorer=fuzz.partial_ratio )[0]
        path = f"{path}\\{chosenFolder}"

path = f"{path}\\{fileName}"
os.rename(source, path)

# choice = input("\tDo you want to change the filename (Y/N)?: ")

# if choice.upper() == "Y":
#     newName = input("\tEnter the new name: ")
#     new = f"{path}\\{newName}"
#     os.rename(path, new)    # hernoemen van het bestand

print(f"\n\t[SOURCE PATH] {source}")

print(f"\t[FINAL PATH] {path}")

input("\n\tPress Enter to exit...") 