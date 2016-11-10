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
    # Use set and dict comprehension instead of Counter for performance reasons. Counters are about 7x slower
    gene_counter.update({amino_acid:gene.count(amino_acid) for amino_acid in set(gene)})

    unstable = False
    for amino_acid in gene_counter:
        if gene_counter[amino_acid] != stable_num:
            unstable = True

    # O(n) solution with double-pointers
    if unstable:
        min_stabilizer_length = length
        i = 0
        # Increment right pointer across gene
        for j in xrange(0, length):
            # If amino acid on the right pointer is removed from gene, decrement its quantity in our counter
            amino_acid = gene[j]
            if amino_acid == 'a': gene_counter['a'] -= 1
            if amino_acid == 'c': gene_counter['c'] -= 1
            if amino_acid == 'g': gene_counter['g'] -= 1
            if amino_acid == 't': gene_counter['t'] -= 1

            # If all amino acids are <= stability levels = we have reached a solution
            while (gene_counter['a'] <= stable_num and gene_counter['c'] <= stable_num and
                   gene_counter['g'] <= stable_num and gene_counter['t'] <= stable_num and i <= j):
                # Keep track of best solution
                min_stabilizer_length = min(min_stabilizer_length, j - i + 1)

                # Increment left pointer to check for better solutions
                amino_acid2 = gene[i]
                if amino_acid2 == 'a': gene_counter['a'] += 1
                if amino_acid2 == 'c': gene_counter['c'] += 1
                if amino_acid2 == 'g': gene_counter['g'] += 1
                if amino_acid2 == 't': gene_counter['t'] += 1
                i += 1
    else:
        min_stabilizer_length = 0

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