#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:25:19 2024

@author: fatemehmohebbi
"""

import csv
import numpy as np
import glob
import pandas as pd


def read_top_items_from_column(file_path, column_index, num_items):
    """Read the top N items from a specific column in a CSV file."""
    top_items = set()
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the first row
        for row in reader:
            if len(row) > column_index:
                # Splitting the value by "," and taking the first part
                item = row[column_index].split('.')[0].strip()
                top_items.add(item)
                if len(top_items) >= num_items:
                    break
    # print(next(iter(top_items), None))
    return top_items #next(iter(top_items), None)


def top_genes(file_paths):
    top_g = []
    for i, file_path in enumerate(file_paths):
        column_data = read_top_items_from_column(file_path, 1, 10)
        top_g.extend(column_data)

    top_genes = set(top_g)
    return top_genes


def all_replicates_top_genes(my_dict):
    genes_dict = {}
    for tool, address in my_dict.items():
        files = glob.glob(address+'*abs_gene_count_diff.csv')
        top_genes_set = top_genes(files)
        
        genes_dict[tool] = top_genes_set

    return genes_dict


def make_table_with_top_genes():
    samples = ['A', 'B', 'C', 'D']

    dataframes_list = []
    for sample in samples:
        df_ = pd.DataFrame()
        tool_column = []
        sample_column = []
        gene_column = []
        tools = ['Salmon', 'HTSeq', 'RSEM', 'Kallisto', 'featurecount']
        Address = []
        Address.append("/Users/fatemehmohebbi/Downloads/rna_seq_results/real_analysis/salmon/salmon_output_sample_"+sample+"/")
        Address.append("/Users/fatemehmohebbi/Downloads/rna_seq_results/real_analysis/htseq/htseq_sample_"+sample+"/")
        Address.append("/Users/fatemehmohebbi/Downloads/rna_seq_results/real_analysis/rsem/rsem_gene_count_"+sample+"/")
        Address.append("/Users/fatemehmohebbi/Downloads/rna_seq_results/real_analysis/kallisto/kallisto_output_sample_converted_"+sample+"/")
        Address.append("/Users/fatemehmohebbi/Downloads/rna_seq_results/real_analysis/featurecount/exp_levels_"+sample+"/")
    
        my_dict = dict(zip(tools, Address))
        values = all_replicates_top_genes(my_dict)
        
        for key, value in values.items():
            i=0
            for item in value:
                if i == 0:
                    sample_column.append(sample)
                    tool_column.append(key)
                    gene_column.append(item)
                    i = i + 1
                else:
                    sample_column.append('')
                    tool_column.append('')
                    gene_column.append(item)
        df_['Sample'] = sample_column
        df_['Tool'] = tool_column
        df_['Top gene'] = gene_column
        dataframes_list.append(df_)
    result_df = pd.concat(dataframes_list, axis=1, ignore_index=True)
    result_df.to_excel('/Users/fatemehmohebbi/Downloads/rna_seq_results/real_analysis/top_genes_seqc_10.xlsx', index=False)
            

if __name__ == "__main__":
    """get all top genes for all replicates for each sample, most likely is the same gene
    if it is not then seperately report it."""
    make_table_with_top_genes()

