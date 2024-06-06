#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:22:59 2023

@author: fatemehmohebbi
"""
import os, sys

# Function to process text files
def process_text_file(file_path, txt_path, delimiter):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    seperator = '\t'
    # Extract header
    header = lines[0].strip()

    # Process lines
    processed_lines = [header]
    for line in lines[1:]:
        parts = line.strip().split(delimiter)
        if len(parts) > 1:
            first_column = parts[0]
            new_col = first_column.strip().split("|")[0]
            processed_lines.append(f"{new_col}{seperator}{seperator.join(parts[1:])}")

    # Save processed lines to a new text file named "tpm.txt"
    with open(txt_path + '_tpm.txt', 'w') as file:
        file.write('\n'.join(processed_lines))


# Directory containing the text files
directory = sys.argv[1]
output_dir = sys.argv[2]
# directory = "/Users/fatemehmohebbi/Downloads/rna_seq_results/kallisto_output_sample_A/"
Ending = "/abundance.tsv"
# output_dir = "/Users/fatemehmohebbi/Downloads/rna_seq_results/kallisto_output_sample_A_converted/"

# Loop through files in the directory
for file in os.listdir(directory):
    filename = directory + file + Ending
    if file.startswith("SRR"):
        # file_path = os.path.join(directory, filename)
        if filename.endswith(".txt"):
            process_text_file(filename, output_dir + file, delimiter=' ')
        elif filename.endswith(".tsv"):
            process_text_file(filename, output_dir + file, delimiter='\t')
        print(f"{filename} processed successfully.")

print("Processed files saved as tpm.txt.")


