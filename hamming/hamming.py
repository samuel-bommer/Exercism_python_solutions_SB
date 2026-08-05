"""
Hamming distance
"""

def distance(strand_a: str, strand_b: str) -> int:
    """
    We compare two strands and count the 
    differences, this is known as the Hamming
    distance.
    """
    
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    
    hamming_distance = 0
    for neucleotide in range(len(strand_a)):
        if strand_a[neucleotide] != strand_b[neucleotide]:
            hamming_distance += 1
                
    return hamming_distance