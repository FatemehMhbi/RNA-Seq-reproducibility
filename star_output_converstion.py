#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:57:33 2024

@author: fatemehmohebbi
"""


import os
import glob

# Specify the directory path
path = "/Users/fmohebbi/Downloads/rna-seq-results/real_data/STAR_quartet/"
# path = "/Users/fatemehmohebbi/Downloads/rna_seq_results/real_analysis/star/Star_sample_D"

# Use glob to find all out.tab files in the directory
out_tab_files = glob.glob(os.path.join(path, '*bamReadsPerGene.out.tab'))

# Iterate through each out.tab file
for file_path in out_tab_files:
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract the first two columns while ignoring specified rows
    result = [(line.split()[0], line.split()[1]) for line in lines if not line.startswith(('N_unmapped', 'N_multimapping', 'N_noFeature', 'N_ambiguous'))]

    # Save the result to a text file
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    with open(os.path.join(path, file_name + '_gene_count.txt'), 'w') as file:
        for item in result:
            file.write(f"{item[0]}\t{item[1]}\n")

    print(f"Data saved to {file_name}_gene_count.txt")



# Specify the file path
# path = "/Users/fatemehmohebbi/Downloads/rna_seq_results/synthetic_analysis/analysis/Star/"
# file_ = path+'ERR188071_g.bamReadsPerGene.out.tab'

# # Read the content of the file
# with open(file_, 'r') as file:
#     lines = file.readlines()

# # Extract the first two columns while ignoring specified rows
# result = [(line.split()[0], line.split()[1]) for line in lines if not line.startswith(('N_unmapped', 'N_multimapping', 'N_noFeature', 'N_ambiguous'))]

# # Save the result to a text file
# file_name = file_.split('.')[0]
# with open(file_name+'_gene_count.txt', 'w') as file:
#     for item in result:
#         file.write(f"{item[0]}\t{item[1]}\n")

# print("Data saved to gene_count.txt")
