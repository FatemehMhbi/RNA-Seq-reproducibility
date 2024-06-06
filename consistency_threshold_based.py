#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 10:01:15 2024

@author: fatemehmohebbi
"""

import csv
import numpy as np
import glob
import pandas as pd
from itertools import chain


def extract_names_above_threshold(file_path, threshold):
    names_above_threshold = []

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Assuming the first row contains column names
        header = next(csv_reader)
        name_column_index = header.index('0')  # Replace 'Name' with the actual name of your name column
        value_column_index = header.index('1')  # Replace 'Value' with the actual name of your value column
        
        for row in csv_reader:
            name = row[name_column_index]
            value = float(row[value_column_index])
            
            if value > threshold:
                names_above_threshold.append(name.split('.')[0].strip())

    return names_above_threshold


def read_top_items_from_column(file_path, column_index, num_items):
    """Read the top N items from a specific column in a CSV file."""
    top_items = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the first row
        for row in reader:
            if len(row) > column_index:
                # Splitting the value by "," and taking the first part
                item = row[column_index].split('.')[0].strip()
                top_items.append(item)
                if len(top_items) >= num_items:
                    break
    return top_items


def shared_genes_per_rank_real_data(file_paths,num_items):
    # Specify the column index (0-based) you want to consider
    column_index = 1  # Assuming the second column (index 1)     

    # Initialize an empty set for the first intersection
    current_intersection = set()

    # Iterate over the file paths
    for i, file_path in enumerate(file_paths):
        # Read top items from the current column
        column_data = read_top_items_from_column(file_path, column_index, num_items)

        # If it's the first iteration, set the current intersection to the column data
        if i == 0:
            current_intersection = column_data
        else:
            # Find the intersection with the current column
            # current_intersection = current_intersection.intersection(column_data)
            current_intersection = list(filter(lambda x: x in column_data, current_intersection))

        # Print the intersection at each step
        # print("this file :", file_path)
        # print(current_intersection)
        # print(f"Intersection{i + 1} of top {num_items} items in the second column:", len(current_intersection))

    # Calculate and print the percentage for the final intersection
    final_intersection_size = len(current_intersection)
    print(current_intersection)
    print(f"Intersection{i + 2} of top {num_items} items in the second columns:", final_intersection_size)
    return current_intersection


def genes_per_rank_real_data(file_paths,num_items):
    # Specify the column index (0-based) you want to consider
    column_index = 1  # Assuming the second column (index 1)     
    my_dataframe = pd.DataFrame()

    # Iterate over the file paths
    for i, file_path in enumerate(file_paths):
        # Read top items from the current column
        column_data = read_top_items_from_column(file_path, column_index, num_items)
        my_dataframe[str(i)] = list(column_data)
    my_dataframe.to_csv(file_path.split('.csv')[0]+"_sample_table.csv", index=False)
    return my_dataframe

def shared_genes_per_threshold_real_data(file_paths,threshold):
    
    # Initialize an empty set for the first intersection
    current_intersection = []

    # Iterate over the file paths
    for i, file_path in enumerate(file_paths):
        # Read top items from the current column
        column_data = extract_names_above_threshold(file_path, threshold)

        # If it's the first iteration, set the current intersection to the column data
        if i == 0:
            current_intersection = column_data
        else:
            # Find the intersection with the current column
            # current_intersection = current_intersection.intersection(column_data)
            current_intersection = list(filter(lambda x: x in column_data, current_intersection))

        # Print the intersection at each step
        # print("this file :", i)
        # print(current_intersection)
        # print(f"Intersection{i + 1} of top {num_items} items in the second column:", len(current_intersection))

    # Calculate and print the percentage for the final intersection
    final_intersection_size = len(current_intersection)
    # print(current_intersection)
    print(f"Intersection{i + 2} of top ranked items in the second columns:", final_intersection_size)
    return current_intersection


def compare2(file1, file2, num_items = 100):
    # Specify the column index (0-based) you want to consider
    column_index = 1  # Assuming the second column (index 1)    

    # Read top 100 items from both columns
    column1_data = read_top_items_from_column(file1, column_index, num_items)
    column2_data = read_top_items_from_column(file2, column_index, num_items)
    # column1_data = extract_names_above_threshold(file1, 100)
    # column2_data = extract_names_above_threshold(file2, 100)


    # Find the intersection of the two columns
    # intersection1 = column1_data.intersection(column2_data)
    intersection1 = list(filter(lambda x: x in column2_data, column1_data))

    # print(f"Intersection1 of top {num_items} items in second columns:", intersection1)
    # print(intersection1)
    return intersection1


def percentage_threshold(file_paths,threshold):
    
    # Initialize an empty set for the first intersection
    percentage = []
    ids = []
    all_genes = 38666
    # Iterate over the file paths
    
    for i, file_path in enumerate(file_paths):
        # Read top items from the current column
        # print(file_path)
        ids.append(file_path.split("/")[-1].split('_abs_gene_count_diff')[0])
        column_data = extract_names_above_threshold(file_path, threshold)
        perc = (all_genes - len(column_data))*100/all_genes
        percentage.append(perc)
    df = pd.DataFrame({'ID': ids, 'Percentage': percentage})
    df.to_csv(file_path.split('_abs_gene_count_diff')[0]+'s_gene_count_perc_treshold'+str(threshold)+'.txt', sep='\t', index=False)
    return df


def threshold_based_consistency():

    sample = 'B'
    library = "across_libraries"
    # library = "within_library"
    dir_ = "/Users/fatemehmohebbi/Downloads/rna_seq_results/real_analysis/"
    file1= dir_+ "salmon/salmon_output_sample_"+sample+"/"+library+"/"
    file2= dir_+ "featurecount/expression_levels/exp_levels_"+sample+"/"+library+"/"
    file3= dir_+ "htseq/htseq_sample_"+sample+"/"+library+"/"
    file4= dir_+ "kallisto/kallisto_output_sample_converted_"+sample+"/"+library+"/"
    file5= dir_+ "rsem/rsem_gene_count_"+sample+"/"+library+"/"
    file6= dir_+ "star/Star_sample_"+sample+"/"+library+"/"
    for Address in [file1, file2, file3, file4, file5, file6]:
        print(Address)
        #*rv_abs_gene_count_diff.csv files are outputs of get_abs_gene_count_difference.py
        files = glob.glob(Address+'*rv_abs_gene_count_diff.csv')
        print(files)
        for trs in [1, 10, 100]:
            f1 = percentage_threshold(files, trs)
            print(f1)


        
if __name__ == "__main__":
    threshold_based_consistency()

    

