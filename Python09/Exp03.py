# Copy Contents of "Galaxy.txt"

# Create "Galaxy.txt" with 25 galaxy names
with open("Galaxy.txt", "w") as file:
    file.write("\n".join([
        "Andromeda", "Milky Way", "Triangulum", "Whirlpool", "Sombrero", "Messier 87", 
        "Large Magellanic Cloud", "Small Magellanic Cloud", "Cartwheel", "Cigar", 
        "Pinwheel", "Centaurus A", "Hoag's Object", "Black Eye", "Tadpole", 
        "Antennae", "Sunflower", "Sculptor", "NGC 1300", "NGC 3370", 
        "NGC 6946", "NGC 253", "IC 1101", "Virgo A", "NGC 4565"
    ]))

# Make a copy of "Galaxy.txt"
def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dest:
            dest.write(src.read())
            print(f"Contents copied from {source} to {destination}")
    except FileNotFoundError:
        print(f"File {source} is not found!")

# Example usage
copy_file("Galaxy.txt", "Galaxy_copy.txt")
