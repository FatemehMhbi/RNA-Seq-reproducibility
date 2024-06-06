#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:12:10 2024

@author: fmohebbi
"""

import os
import glob
import pandas as pd
from utils_for_rna_seq_analysis import boxplot_treshold_based_consistency



def get_percentages_chinese_q(directory_path, header, seperator, threshold_percentage):
    print(directory_path)
    # threshold_percentage = 0.0 
    # header = 0
    # seperator = ' ' #'\t'
    # Define the sample IDs
    sample_ids = ['D5', 'D6', 'M8', 'F7']
    
    # Initialize a dictionary to store groups of files
    file_groups = {}
    # Initialize lists to store statistics
    statistics_output = []
    average_list = []
    top_genes_100 = []
    # Iterate through each sample ID
    for sample_id in sample_ids:
        # Get all files containing the sample ID in their names
        files = glob.glob(os.path.join(directory_path, f'*{sample_id}*.txt'))
    
        # Group files based on their prefixes
        for file in files:
            prefix = file.split(sample_id)[0]+sample_id
            if prefix not in file_groups:
                file_groups[prefix] = []
            file_groups[prefix].append(file)
    
    tp_genes = []
    threshold_percentages = []
    # Calculate absolute differences and average threshold-based percentages for each group
    for prefix, files in file_groups.items():
        statistics_output.append(f"Group '{prefix}' contains the following files:")
        statistics_output.append(files)
        # Read the first file as x and set the first column as index
        # x = pd.read_csv(files[0], sep='\t', index_col=0)
        x = pd.read_csv(files[0], sep=seperator, index_col=0, header=None if header == 0 else 'infer')
        x = x[x.index.str.startswith('ENS')]
        statistics_output.append(f"File X: {files[0]}")
        
        # Calculate absolute differences and threshold-based percentages for each subsequent file
        
        for file in files[1:]:
            # y = pd.read_csv(file, sep='\t', index_col=0)
            y = pd.read_csv(file, sep=seperator, index_col=0, header=None if header == 0 else 'infer')
            y = y[y.index.str.startswith('ENS')]
            # Merge DataFrames to ensure indices match
            merged = pd.merge(x, y, left_index=True, right_index=True)
            # Calculate absolute differences row-wise and take the average
            absolute_diff = (merged.iloc[:, 0] - merged.iloc[:, 1]).abs()
            max_index = absolute_diff.idxmax()
            # Get the corresponding row using iloc
            max_row = absolute_diff[max_index] #.max()
            top_genes = sorted(absolute_diff)
            top_genes_100.append(top_genes)
            # print("Row with max value:")
            # print(max_row)
            # print(max_index)
            tp_genes.append(max_index)
            average_diff = absolute_diff.mean()
            statistics_output.append(f"Average absolute difference between corresponding columns: {average_diff}")
            
            # Define the threshold percentage
            
            lower_bound = x * (1 - threshold_percentage)
            upper_bound = x * (1 + threshold_percentage)
            within_range_rows = ((lower_bound <= y) & (y <= upper_bound)).sum().sum()
            total_rows = x.shape[0]  # Total number of elements in x
            percentage_match = (within_range_rows / total_rows) * 100
            statistics_output.append(f"Consistency between corresponding files: {percentage_match}")
            threshold_percentages.append(percentage_match)
            
    # Calculate the average threshold percentage across all file pairs in the group
    average_percentage = sum(threshold_percentages) / len(threshold_percentages)
    average_list.append(average_percentage)
    statistics_output.append(f"\nAverage percentage of rows within threshold': {average_percentage:.2f}%")
    statistics_output.append("----------------------------------------------------------------------")
    
    print(set(tp_genes))
    # Print the statistics output
    # for stat in statistics_output:
    #     print(stat)
        
    # with open(directory_path+'_statistics_'+str(threshold_percentage)+'.txt', 'w') as file:
    #     for line in statistics_output:
    #         file.write(str(line) + '\n')
    return threshold_percentages, top_genes_100


if __name__ == "__main__":
    tools = ['featureCounts'] #, 'HTseq', 'Salmon', 'Kallisto', 'RSEM', 'STAR']
    dir_ = "/rna-seq-results/real_data/"
    tools_dir = [dir_+'featurecount_quartet']#,\
                  # dir_+'htseq_quartet',\
                  #     dir_+"salmon_quartet",\
                  #         dir_+"kallisto_quartet",\
                  #             dir_+"RSEM_quartet",\
                  #                 dir_+"STAR_quartet"]
    headers = [1, 0, 0, 1, 1, 0]
    seperators = ['\t', '\t', ' ', ' ', '\t', '\t']
    
    tools_percentages_list = []
    stats = []
    tp_genes_tools_list = []
    
    for file_path, h, s in zip(tools_dir, headers, seperators):
        percentage_list = []
        for tr in [0.0, 0.01, 0.1]:
            percentages, tp_g = get_percentages_chinese_q(file_path, h, s, tr)
            tp_genes_tools_list.append(tp_g)
            percentage_list.append(percentages)
        tools_percentages_list.append(percentage_list)
    # boxplot_treshold_based_consistency(tools_percentages_list, tools, "chinese", dir_)
