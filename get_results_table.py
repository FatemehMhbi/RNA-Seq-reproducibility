#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:41:29 2024

@author: fmohebbi
"""

import pandas as pd
import glob, re

order_file_path = '/Users/fmohebbi/Downloads/rna-seq-results/gene_ids_110_ens.txt'  
results = "/Users/fmohebbi/Downloads/rna-seq-results/kallisto/simulated_shuffled_converted/"
# results = "/Users/fmohebbi/Downloads/rna-seq-results/featurecounts/counts_seqc_simulated_shuffled/"
# results = "/Users/fmohebbi/Downloads/rna-seq-results/HTseq/SEQC_shuffled/"
# results = "/Users/fmohebbi/Downloads/rna-seq-results/kallisto/simulated_shuffled_converted/"
# results = "/Users/fmohebbi/Downloads/rna-seq-results/RSEM/seqc_simulated_shuffled/"
# results = "/Users/fmohebbi/Downloads/rna-seq-results/STAR/counts_seqc_simulated_shuffled/"
results = "/Users/fmohebbi/Downloads/rna-seq-results/gene_count_results_for_simulation/"


# Define a custom sorting function
def alphanumeric_sort(file_name):
    parts = re.split(r'(\d+)', file_name)
    return [int(part) if part.isdigit() else part for part in parts]


def transctipts():
    df2_order = pd.read_csv(order_file_path, delimiter=',')  # Assuming file2 is comma-separated
    file_list = glob.glob(results + '*.isoforms.results')
    # sorted_files = sorted(file_list, key=lambda x: float('.'.join(x.split('/')[-1].split('.')[:-1])))
    sorted_files = sorted(file_list, key=alphanumeric_sort)
    
    df_counts = pd.DataFrame()
    i = 0
    for input_file_path in sorted_files:
        print(input_file_path)
        # Read the text files into pandas DataFrames
        df1 = pd.read_csv(input_file_path, delimiter='\t')  # Assuming file1 is tab-separated
        
        df1 = df1.set_index('transcript_id')
        df1 = df1.reindex(index=df2_order['transcript_id'].apply(lambda x: x.split('.')[0]))
        # df1 = df1.reset_index()
        
        e_counts = df1['expected_count']
        df_filled = e_counts.fillna(0)
        df_counts[str(i)] = df_filled
        i = i + 1
    df_counts.to_csv(results+"table.csv")
    
def genes():
    file_list = glob.glob(results + '*t.txt')
    # sorted_files = sorted(file_list, key=lambda x: float('.'.join(x.split('/')[-1].split('.')[:-1])))
    sorted_files = sorted(file_list, key=alphanumeric_sort)
    # sorted_files = file_list
    
    df_counts = pd.DataFrame()
    i = 0
    for input_file_path in sorted_files:
        print(input_file_path)
        # Read the text files into pandas DataFrames
        # df1 = pd.read_csv(input_file_path, delimiter=' ', header=None)  
        # Assuming file1 is tab-separated
        df1 = pd.read_csv(input_file_path, delimiter='\t') 
        
        df1 = df1.set_index(df1.columns[0])
        # df1 = df1.reset_index()
        
        e_counts=df1.iloc[:, 0]
        df_filled = e_counts.fillna(0)
        df_counts[str(i)] = df_filled
        i = i + 1
    df_counts = df_counts.set_index(df1.index)
    df_counts = df_counts[df_counts.index.str.startswith("ENS")]
    df_counts.to_csv(results+"table.csv")

if __name__ == "__main__":
    genes()