#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 17:53:15 2024

@author: fmohebbi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from get_inputs import get_path

fig, axes = plt.subplots(figsize=(7, 8))
    
def draw_rp(shs,buffer,color):
    legend_handles1 = []
    for i in range(0,len(tools)):
        sh_perc = shs[i]
        pos = np.arange(len(sh_perc))+buffer[i]
        col = color[i]
        box = axes.boxplot(sh_perc, positions = pos,
                        boxprops=dict(facecolor=col, alpha = 0.5), widths = 0.13, vert=True, patch_artist=True)
        # for i, data in enumerate(sh_perc):
        #     x = [pos[i] for t in range(len(data)) ]
        #     axes.scatter(x, data, color='black', marker='.', alpha=0.5)
        legend_handles1.append(box['boxes'][0])
    axes.legend(legend_handles1, tools, loc='lower right', bbox_to_anchor=(1.1, 0.0), fancybox=True, shadow=True) #loc='lower right') #'upper left'
    # axes.set_title('Technical replicates')
    axes.set_ylabel('percentage of consistency %')
    axes.set_ylim([45,100])
    axes.set_xlabel('Threshold')
    #axes.set_xticklabels(['exact match','integer','within 1%','within 10%'])
    num_ticks = 3
    xtick_pos = np.linspace(0, len(sh_perc) - 1, num_ticks)
    axes.set_xticks(xtick_pos)

    axes.set_xticklabels(['Exact match','0.01','0.1'])
    for pos in xtick_pos[1:]:
        axes.axvline(x=pos - 0.5, linestyle='--', color='gray', alpha=0.7)

    xtick_pos = np.arange(len(sh_perc))
    axes.set_xticks(xtick_pos)
    

def boxplot_treshold_based_consistency(consistencies, tools, lable):
    # Adjust colors and buffers based on the number of tools
    num_tools = len(tools)
    basic_colors = list(mcolors.TABLEAU_COLORS.values())
    color = basic_colors[:num_tools]
    buffer = np.linspace(-0.3, 0.3, num_tools)

    buffer = buffer + np.arange(num_tools) * 0.005  # Adjust the buffer for better visualization
    # print(rps)
    draw_rp(consistencies, buffer, color)

    # plt.suptitle("Percentage of consistency (gene count) between simulated replicates and their reversed complement", wrap=True)
    plt.suptitle("Percentage of consistency (gene count) "+mode, wrap=True)
    plt.savefig(dir_+"boxplot_"+lable+".png", dpi=199)
    plt.show()

def consistency_calculation(file1_path, file2_path):
    df1_ = pd.read_csv(file1_path, index_col=0)  # Assuming first column is the index
    df2_ = pd.read_csv(file2_path, index_col=0)
    consistencies = []
    average_list = []
    statistics_output = []  # List to store the print statements
    
    shared_genes = set(df1_.index).intersection(df2_.index)
    
    df1 = df1_[df1_.index.isin(shared_genes)].sort_index()
    df2 = df2_[df2_.index.isin(shared_genes)].sort_index()
    
    df2.columns = df1.columns

    if df1.shape != df2.shape:
        statistics_output.append("Error: Dimensions of the DataFrames do not match.")
    else:
        # Calculate the absolute differences and take the average
        absolute_diff = (df1 - df2).abs()
        # print(absolute_diff)
        max_index = absolute_diff.idxmax()
        # Get the corresponding row using iloc
        # max_row = absolute_diff[max_index] #.max()
        
        print("Row with max value:")
        # print(max_row)
        print(max_index)
        average_diff = absolute_diff.mean().mean()  # Calculate the average over all rows
        statistics_output.append(f"Average absolute difference between corresponding columns: {average_diff}")

        # Define the threshold percentage
        thresholds = [0.0, 0.01, 0.1]
        
        for threshold_percentage in thresholds:
            statistics_output.append(f"-----------------------------{threshold_percentage}------------------------------")
            match_percentages = []
            for col in df1.columns:
                lower_bound = df1[col] * (1 - threshold_percentage)
                upper_bound = df1[col] * (1 + threshold_percentage)
                within_range_rows = ((lower_bound <= df2[col]) & (df2[col] <= upper_bound)).sum()
                total_rows = df1.shape[0]
                percentage_match = (within_range_rows / total_rows) * 100
                match_percentages.append(percentage_match)
                statistics_output.append(f"Column '{col}': {within_range_rows} rows within threshold ({percentage_match:.2f}%).")
            consistencies.append(match_percentages)
            # Calculate the average percentage across all columns
            average_percentage = sum(match_percentages) / len(match_percentages)
            average_list.append(average_percentage)
            statistics_output.append(f"\nAverage percentage of rows within threshold across all columns: {average_percentage:.2f}%")
            statistics_output.append("----------------------------------------------------------------------")

    return consistencies, average_list, statistics_output


if __name__ == "__main__":
    # mode = 'simulated_vs_rv'
    # mode = 'simulated_vs_shuffled'
    mode = 'seqc_real_vs_rv'
    # mode = 'seqc_real_vs_shuffled'
    # mode = 'simulated_vs_actual_gene_count'

    tools, tools_dir = get_path(mode)
    dir_ = "/Users/fmohebbi/Downloads/rna-seq-results/in_silico/"
    
    tools_percentages_list = []
    tools_consistency_list = []
    stats = []
    for file1_path, file2_path in tools_dir:
        percentages_list, consistency, text = consistency_calculation(file1_path, file2_path)
        tools_percentages_list.append(percentages_list)
        tools_consistency_list.append(consistency)
        stats.extend([file1_path, file2_path])
        stats.extend(text)  # Extend the list with all lines from text
        stats.append('')  
        
    # with open(dir_+ mode + '.txt', 'w') as f:
    #     for line in stats:
    #         f.write(str(line) + '\n')
    # boxplot_treshold_based_consistency(tools_percentages_list, tools, mode)
        