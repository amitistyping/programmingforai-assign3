import re


def read_codon_amino_acid_mapping(filename):
    codon_amino_acid_mapping = {}
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 1):
            split_string = re.split(r'[,\s]+', lines[i].strip())
            codons = split_string[1:(len(split_string) - 1) ]
            amino_acid = f"Amino Acid: {split_string.pop()} | Abbrv: {split_string[0]}"
            
            for codon in codons:
                codon_amino_acid_mapping[codon] = amino_acid
    return codon_amino_acid_mapping

filename = "codon_amino_acid_mapping.txt"
codon_amino_acid_mapping = read_codon_amino_acid_mapping(filename)

def dna_to_codon_sequence(dna_sequence):
    codon_sequence = [dna_sequence[i:i+3] for i in range(0, len(dna_sequence), 3)]
    return codon_sequence

def codon_to_amino_acid(codon_sequence, codon_amino_acid_mapping):
    amino_acid_sequence = [codon_amino_acid_mapping.get(codon, '') for codon in codon_sequence]
    return amino_acid_sequence


# EXECUTION STEPS

# Input DNA sequence
input_dna_sequence = "GCTCGTAATGATTGT"

# Step 1: Convert DNA sequence to codon sequence
codon_sequence = dna_to_codon_sequence(input_dna_sequence)
print("Codon Sequence:", codon_sequence)

# Step 2: Convert codon sequence to amino acid sequence
amino_acid_sequence = codon_to_amino_acid(codon_sequence, codon_amino_acid_mapping)
print("Amino Acid Sequence:", amino_acid_sequence)