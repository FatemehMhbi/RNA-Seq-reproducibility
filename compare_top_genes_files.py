#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:54:55 2023

@author: fatemehmohebbi
"""

import csv
import numpy as np
import glob


def extract_names_above_threshold(file_path, threshold):
    names_above_threshold = set()

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
                names_above_threshold.add(name.split('.')[0].strip())

    return names_above_threshold


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
    return top_items


def shared_genes_per_rank_real_data(file_paths,num_items=100):
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
            current_intersection = current_intersection.intersection(column_data)

        # Print the intersection at each step
        print("this file :", i)
        print(current_intersection)
        # print(f"Intersection{i + 1} of top {num_items} items in the second column:", len(current_intersection))

    # Calculate and print the percentage for the final intersection
    final_intersection_size = len(current_intersection)
    # print(current_intersection)
    print(f"Intersection{i + 2} of top {num_items} items in the second columns:", final_intersection_size)
    return current_intersection

def shared_genes_per_threshold_real_data(file_paths,threshold = 10.0):
    
    # Initialize an empty set for the first intersection
    current_intersection = set()

    # Iterate over the file paths
    for i, file_path in enumerate(file_paths):
        # Read top items from the current column
        column_data = extract_names_above_threshold(file_path, threshold)

        # If it's the first iteration, set the current intersection to the column data
        if i == 0:
            current_intersection = column_data
        else:
            # Find the intersection with the current column
            current_intersection = current_intersection.intersection(column_data)

        # Print the intersection at each step
        print("this file :", i)
        print(current_intersection)
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


    # Find the intersection of the two columns
    intersection1 = column1_data.intersection(column2_data)



    # print(f"Intersection1 of top {num_items} items in second columns:", intersection1)
    print(len(intersection1))
    return len(intersection1)


if __name__ == "__main__":
    IDs = range(0, 16)
    percentage_list = []
    sample = 'B'
    # Address = "/Users/fatemehmohebbi/Downloads/rna_seq_results/Kallisto/kallisto_output_sample_converted_"+sample+"/"
    Address = "/Users/fatemehmohebbi/Downloads/rna_seq_results/htseq/htseq_sample_"+sample+"/"
    # Address = "/Users/fatemehmohebbi/Downloads/rna_seq_results/salmon_output_sample_"+sample+"/"
    files = glob.glob(Address+'*abs_gene_count_diff.csv')
    # f1 = shared_genes_per_threshold_real_data(files)
    f1 = shared_genes_per_rank_real_data(files)

    # Address = "/Users/fatemehmohebbi/Downloads/rna_seq_results/salmon_output_sample_"+sample+"/"
    # Address = "/Users/fatemehmohebbi/Downloads/rna_seq_results/htseq/htseq_sample_"+sample+"/"
    Address = "/Users/fatemehmohebbi/Downloads/rna_seq_results/rsem/rsem_gene_count_"+sample+"/"
    files = glob.glob(Address+'*abs_gene_count_diff.csv')
    f2 = shared_genes_per_threshold_real_data(files)
    # f2 = shared_genes_per_rank_real_data(files)
    
    print("intersection: ", f1.intersection(f2))
    print(len(f1.intersection(f2)))

