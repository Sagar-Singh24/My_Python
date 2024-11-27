# Wipe Out Contents of a File

# Create "planets.txt" with a list of planets
with open("planets.txt", "w") as file:
    file.write("Mercury\nVenus\nEarth\nMars\nJupiter\nSaturn\nUranus\nNeptune\nPluto")

# Wipe out contents of the file
def wipe_file_contents(filename):
    try:
        with open(filename, "w") as file:
            file.truncate(0)
            print(f"Contents of {filename} have been wiped out.")
    except FileNotFoundError:
        print("File not found!")

# Example usage
wipe_file_contents("planets.txt")
