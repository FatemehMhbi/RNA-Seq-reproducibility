#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:37:45 2023

@author: fatemehmohebbi
"""

import os

# Function to read quant.sf file and extract TPM values
def extract_tpm_values(file_path):
    tpm_values = {}
    with open(file_path, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            data = line.strip().split('\t')
            tpm_values[data[0]] = float(data[3])
    return tpm_values

# Function to find the top 10 genes with different expression levels between two files
def find_top_10_differentially_expressed_genes(file1_path, file2_path):
    tpm_values_1 = extract_tpm_values(file1_path)
    tpm_values_2 = extract_tpm_values(file2_path)

    differential_genes = {}
    for gene_id in tpm_values_1.keys():
        if gene_id in tpm_values_2:
            if tpm_values_1[gene_id] != tpm_values_2[gene_id]:
                differential_genes[gene_id] = abs(tpm_values_1[gene_id] - tpm_values_2[gene_id])

    sorted_genes = sorted(differential_genes.items(), key=lambda x: x[1], reverse=True)[:10]

    return sorted_genes

# Main function to call find_top_10_differentially_expressed_genes with two specific quant.sf files
if __name__ == '__main__':
    file1_path = '/Users/fatemehmohebbi/Downloads/Sample_A_quants/SRR896663/quant.sf'
    file2_path = '/Users/fatemehmohebbi/Downloads/Sample_A_quants/SRR896732/quant.sf'
    top_10_genes = find_top_10_differentially_expressed_genes(file1_path, file2_path)

    for i, (gene_id, diff) in enumerate(top_10_genes, 1):
        tpm1 = extract_tpm_values(file1_path)[gene_id]
        tpm2 = extract_tpm_values(file2_path)[gene_id]
        print(f"{i}. Gene ID: {gene_id}, TPM in File 1: {tpm1}, TPM in File 2: {tpm2}, Difference in Expression: {diff}")


