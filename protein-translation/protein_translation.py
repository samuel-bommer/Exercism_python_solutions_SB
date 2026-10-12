"""
Translate an RNA Sequence into proteins

RNA strands are made up of three-nucleotide sequences called codons. Each of them translates
to an amino acid. When joined together, these make proteins.

| Codon              | Amino Acid    |
| ------------------ | ------------- |
| AUG                | Methionine    |
| UUU, UUC           | Phenylalanine |
| UUA, UUG           | Leucine       |
| UCU, UCC, UCA, UCG | Serine        |
| UAU, UAC           | Tyrosine      |
| UGU, UGC           | Cysteine      |
| UGG                | Tryptophan    |
| UAA, UAG, UGA      | STOP          |

To be able to code that, we neeed be able to break up the string into groups of three 
and then have a dictionary with the corresponding Codons and Amino Acids
"""

DICT_AMINO = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan', 
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
}

def proteins(strand: str) -> list[str]:
    """
    Input: strand of Codon
    Output: [Amino Acids]
    """
    
    codon_list = []
    for indx in range(0, len(strand), 3):
        codon = strand[indx:indx+3]
        codon_list.append(codon)
    
    amino_acids = []
    for codon in codon_list:
        if codon in DICT_AMINO:
            value = DICT_AMINO[codon]

            if value == 'STOP':
                break
            amino_acids.append(value)

        else:
            break
    
    return amino_acids
