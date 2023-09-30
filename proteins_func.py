def calc_protein_mass(sequence: str) -> int: 
    """
    Calculate protein molecular weight using the average 
    molecular weight of amino acid - 110 Da
    """
    return len(sequence) * 110


def heaviest_protein(sequence: list):
    """
    Return the sequence of the heaviest protein from list
    """
    protein_mass = {}
    list_of_protein = sequence
    for i in list_of_protein:
        protein_mass[i] = calc_protein_mass(i)
    return count_uniq_max_mass(protein_mass)

def count_uniq_max_mass(protein_mass):
    """
    Count amount of proteins with the same maximum mass and return them
    """
    max_weight = max(protein_mass.values())
    count_protein = 0
    proteins = [] 
    for i in protein_mass:
        if protein_mass[i] == max_weight:
            count_protein += 1
            if count_protein >=1:
                proteins.append(i)
    
    return f'{proteins} - {max_weight}'


def lightest_protein(sequence: list):
    """
    Return the sequence of the lightest protein from list
    """
    protein_mass = {}
    list_of_protein = sequence
    for i in list_of_protein:
        protein_mass[i] = calc_protein_mass(i)
    return count_uniq_min_mass(protein_mass)

def count_uniq_min_mass(protein_mass):
    """
    Count amount of proteins with the same minimum mass and return them
    """
    min_weight = min(protein_mass.values())
    count_protein = 0
    proteins = [] 
    for i in protein_mass:
        if protein_mass[i] == min_weight:
            count_protein += 1
            if count_protein >=1:
                proteins.append(i)
    return f'{proteins} - {min_weight}'

