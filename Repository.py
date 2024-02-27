#we keep all of the sentences in the repository split line by line
def load_variants(filename="variants.txt"):
    with open(filename, "r") as file:
        variants = file.read().splitlines()
    return variants