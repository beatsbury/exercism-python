def to_rna(dna_strand):
    # GCTA -> CGAU
    dna = 'GCTA'
    rna = 'CGAU'
    rna_value = ''
    for nucleotide in dna_strand:
        rna_value += rna[dna.index(nucleotide)]
    return rna_value