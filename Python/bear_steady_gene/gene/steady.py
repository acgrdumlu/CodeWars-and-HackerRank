from __future__ import division
from collections import Counter


def stabilize(gene):
    """Returns the minimum number of amino acids to cut in order to insert a proper stabilizer"""
    # Ensure the gene is the correct length
    stable_num = len(gene) / 4
    if not stable_num.is_integer():
        raise ValueError('Gene needs to be divisible by 4')
    else:
        stable_num = int(stable_num)

    # Count number of each amino acid (A,C,T,G) in the gene
    gene = gene.lower()
    counter = Counter(gene)

    # Determine the characteristics of the stabilizer strand required
    stabilizer = {}
    for amino_acid in counter:
        if counter[amino_acid] != stable_num:
            stabilizer[amino_acid] = stable_num - counter[amino_acid]

    # Determine minimum # of amino acids to remove
    desired_removal_count = 0
    for amino_acid in stabilizer:
        if stabilizer[amino_acid] < 0:
            desired_removal_count = desired_removal_count + abs(stabilizer[amino_acid])

    return desired_removal_count
