def dna_to_rna(dna):
    rna = []
    for i in dna:
        if i == "T":
            rna.append("U")
        else:
            rna.append(i)
    return "".join(rna)

print(dna_to_rna("GCAT"))
print(dna_to_rna("TTTT"))
print(dna_to_rna("TACCGCCGCC"))


def dna_to_rna2(dna):
    return dna.replace("T", "U")

print(dna_to_rna2("GCAT"))
print(dna_to_rna2("TTTT"))
print(dna_to_rna2("TACCGCCGCC"))


def DNAtoRNA(dna):
    RNA= ""
    i = 0
    for i in dna:
        if i == "T":
            RNA = RNA + "U"
        else:
            RNA = RNA + i
    return RNA
print(DNAtoRNA("TACCGCCGCC"))

def DNAtoRNA2(dna):
    return "".join(["U" if c=="T" else c for c in dna])

# Define the dictionary mapping DNA nucleotides to RNA nucleotides
dna_dict = {
    "A": "A",
    "T": "U",
    "C": "C",
    "G": "G"
}

# Define the function to convert DNA to RNA
def DNAtoRNA3(dna):
    rna = []
    for letter in dna:
        rna.append(dna_dict[letter])
    return "".join(rna)

# Test the function
print(DNAtoRNA3("TACCGCCGCC"))  # Expected output: "UACCGCCGCC"

