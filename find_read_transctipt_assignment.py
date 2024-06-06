#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:40:53 2024

@author: fmohebbi
"""

# Define the input file
directory = "/Users/fmohebbi/Downloads/"
#output.txt contains two columns "read id" and "transript id it was assigned to" extracted from bam files for simulated data
input_file = directory + 'output.txt'

# Dictionary to store transcript IDs and their read counts
transcript_counts = {}

# Read the input file line by line
with open(input_file, 'r') as file:
    for line in file:
        # Split each line by tab (\t) to separate the read and transcript IDs
        read_id, transcript_id = line.strip().split('\t')
        slash_index = read_id.find('/')
        semicolon_index = read_id.find(';')
        
        # Extract the substring
        origin_transcript = read_id[slash_index + 1 : semicolon_index]
        
        # Update the count for the current origin_transcript and transcript_id pair
        if origin_transcript in transcript_counts:
            if transcript_id in transcript_counts[origin_transcript]:
                transcript_counts[origin_transcript][transcript_id] += 1
            else:
                transcript_counts[origin_transcript][transcript_id] = 1
        else:
            transcript_counts[origin_transcript] = {transcript_id: 1}

# Print the read counts for each origin_transcript and transcript_id pair
# for origin_transcript, counts in transcript_counts.items():
#     print(f'Origin Transcript: {origin_transcript}')
#     for transcript_id, count in counts.items():
#         print(f'Transcript ID assigned to: {transcript_id} \tRead Count: {count}')
#     print()
    
    
output_file = directory + 'counts_output.txt'
with open(output_file, 'w') as outfile:
    for origin_transcript, counts in transcript_counts.items():
        outfile.write(f'Origin Transcript: {origin_transcript}\n')
        for transcript_id, count in counts.items():
            outfile.write(f'Transcript ID assigned to: {transcript_id} \tRead Count: {count}')
        outfile.write('\n')
