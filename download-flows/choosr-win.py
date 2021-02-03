import os
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

fileName = str(sys.argv[1])

print("[FILENAME]", fileName)

source = f"C:\\Users\\toufi\\Downloads\\{fileName}" 
path = "C:\\Users\\toufi\\OneDrive\\Documenten\\s4" 
folders = None
choice = None

def dirCommand(path):
    global folders
    print("\n\t[MAPPEN]\n")
    folders = os.listdir(path)
    print("[INFO]", len(folders))
    for folder in folders:
        print(f"\t{folder}")

while True:
    dirCommand(path)
    choice = input("\n\tBij welke map hiervan hoort dit bestand?: ")

    if folders == [] or choice == "":
        break
    else: 
        chosenFolder = process.extractOne( query=choice, choices=folders, scorer=fuzz.partial_ratio )[0]
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