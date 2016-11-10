# -*- coding: utf-8 -*-
"""This module stabilizes genes"""
from __future__ import division
from collections import Counter


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
    gene_counter = Counter(gene)
    # Add a slot for any missing amino acids to the counter (this doesn't change the quantity of prexisting ones)
    gene_counter.update({'a': 0, 'c': 0, 't': 0, 'g': 0})

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

    # Algo: start from beginning with desired removal count. If can't satisfy all required removals, +1 to its size
    # Shit algo since inefficient
    req_met = False
    while not req_met:
        for x in xrange(0, length):
            test_sequence_counter = Counter(gene[x:x + desired_removal_count])
            for amino_acid in removal:
                if test_sequence_counter[amino_acid] == abs(stabilizer_reqs[amino_acid]):
                    req_met = True
        if not req_met:
            desired_removal_count = desired_removal_count + 1

    # Algo: Shrinking sliding window

    return desired_removal_count


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