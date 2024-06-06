#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:21:30 2023

@author: fatemehmohebbi
"""
import glob


# folder_path = '/Users/fatemehmohebbi/Downloads/featureCounts_bowties_synthetic_data/*counts.txt'
folder_path = '/project/fmohebbi_1178/RNA-seq-repd/seqc/feature_count_sampleA/*_counts_sorted.txt'

# Iterate over all text files in the folder
for file_path in glob.glob(folder_path):

    # Replace 'output_expression_levels.txt' with the desired name for the output text file.
    id_ = file_path.split('_bowtie2_2_counts_sorted.txt')[0]
    output_file = id_ + "_featurecounts_Elevels.txt"
    
    
    # Dictionary to store expression levels for each gene
    expression_levels = {}
    
    # Open the featureCounts output file for reading
    with open(file_path, 'r') as f_counts:
        # Iterate through each line in the file
        for line in f_counts:
            # Skip lines not starting with 'ENSG'
            if not line.startswith('ENSG'):
                continue
    
            fields = line.strip().split('\t')
    
            # Extract gene ID
            gene_id = fields[0]
    
            # Extract expression levels for each sample
            sample_expression = [int(count) for count in fields[6:]]
    
            # Create a dictionary entry for the gene if it doesn't exist
            if gene_id not in expression_levels:
                expression_levels[gene_id] = {}
    
            # Associate expression levels with sample names
            for sample, count in zip(range(1, len(sample_expression) + 1), sample_expression):
                expression_levels[gene_id][f"Sample{sample}"] = count
    
    # Close the featureCounts output file
    
    # Write the expression levels to the output text file
    with open(output_file, 'w') as output:
        # Write header
        output.write("GeneID\t" + "\t".join([f"Sample{i}" for i in range(1, len(sample_expression) + 1)]) + "\n")
    
        # Write expression levels
        for gene_id, levels in expression_levels.items():
            output.write(f"{gene_id}\t" + "\t".join(str(levels.get(sample, 0)) for sample in [f"Sample{i}" for i in range(1, len(sample_expression) + 1)]) + "\n")
    
    print(f"Expression levels extracted and saved to {output_file}")
    
    
    
