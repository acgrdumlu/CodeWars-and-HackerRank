# -*- coding: utf-8 -*-
"""This module stabilizes genes"""
from __future__ import division


def stabilize(length, gene):
    """Returns the minimum number of amino acids to cut in order to insert a proper stabilizer"""
    # Ensure the gene is the correct length
    stable_num = length / 4
    if not stable_num.is_integer():
        raise ValueError('Gene needs to be divisible by 4')
    else:
        stable_num = int(stable_num)

    # Count number of each amino acid (A,C,T,G) in the gene
    gene = gene.lower()
    gene_counter = {'a': 0, 'c': 0, 't': 0, 'g': 0}
    # Use set and dict comprehension instead of Counter for performance reasons
    gene_counter.update({amino_acid:gene.count(amino_acid) for amino_acid in set(gene)})

    # Determine the stabilization actions required
    stabilizer_reqs = {}
    desired_removal_count = 0
    removal = ''
    for amino_acid in gene_counter:
        if gene_counter[amino_acid] != stable_num:
            action_quantity = stable_num - gene_counter[amino_acid]
            stabilizer_reqs[amino_acid] = action_quantity
            # Calculate minimum # of amino acids to remove
            if action_quantity < 0:
                desired_removal_count = desired_removal_count + abs(action_quantity)
                removal = removal + amino_acid

    # Algo: Shrinking sliding window.
    # Performance: 150k gene --> correct answer in 5 seconds with dictionary comprehension
    #              If used Counter, it was 36 seconds
    # Issue is if solution substring is large, performance degrades significantly. Need solution that doesn't count
    i = 0
    j = desired_removal_count
    min_stabilizer_length = length
    while j < length:
        test_sequence_counter = {amino_acid:gene[i:j].count(amino_acid) for amino_acid in set(gene[i:j])}
        req_met = True
        for amino_acid in removal:
            if amino_acid not in test_sequence_counter:
                req_met = False
            elif test_sequence_counter[amino_acid] < abs(stabilizer_reqs[amino_acid]):
                req_met = False
        if req_met:
            min_stabilizer_length = min(min_stabilizer_length, j - i)
            i = i + 1
        elif j < length - 1:
            j = j + 1
        else:
            break

    return min_stabilizer_length


# Skip this section if nosetesting. This section is just for submission to HackerRank
if __name__ == "__main__":
    # Input format
    # First line contains two length of gene sequence
    # Second line contains the gene

    # Get input from user
    lgth = int(raw_input())
    gene_seq = raw_input()

    # Stabilize
    print stabilize(lgth, gene_seq)