"""
RNA transcript
"""


def to_rna(dna_strand: str) -> str:
    """
    Transcribe DNA into RNA
    """
    
    RNA_mapping = {
        'G' : 'C',
        'C' : 'G',
        'T' : 'A',
        'A' : 'U'
    }

    RNA_transcribed = []
    
    for nucleotide in dna_strand:
        if nucleotide in RNA_mapping:
            rna_trns = RNA_mapping.get(nucleotide)
            RNA_transcribed.append(rna_trns)
    
    rna_strand = ''.join(RNA_transcribed)
    return rna_strand