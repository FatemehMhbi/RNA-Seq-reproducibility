#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:56:53 2024

@author: fatemehmohebbi
"""


def get_path(mode):
    base_path = '/Users/fmohebbi/Downloads/rna-seq-results/in_silico/'
    
    # Real data paths
    file1_fc_real = base_path + 'featurecounts/count_seqc/table.csv'
    file2_fc_real_rv = base_path + 'featurecounts/counts_seqc_rv/table.csv'
    
    file1_htseq_real = base_path + 'HTseq/SEQC/table.csv'
    file2_htseq_real_rv = base_path + 'HTseq/SEQC_rv/table.csv'
    
    file1_salmon_real = base_path + 'salmon/counts_seqc/table.csv'
    file2_salmon_real_rv = base_path + 'salmon/counts_seqc_rv/table.csv'
    
    file1_kallisto_real = base_path + 'kallisto/real_converted/table.csv'
    file2_kallisto_real_rv = base_path + 'kallisto/SEQC_rv_converted/table.csv'
    
    file1_rsem_real = base_path + 'RSEM/seqc/table.csv'
    file2_rsem_real_rv = base_path + 'RSEM/seqc_rv/table.csv'
    
    file1_star_real = base_path + 'STAR/counts_seqc/table.csv'
    file2_star_real_rv = base_path + 'STAR/counts_seqc_rv/table.csv'
    
    # Shuffled data paths
    file1_fc_shuffled = base_path + 'featurecounts/counts_seqc_shuffled/table_v1.csv'
    
    file1_htseq_shuffled = base_path + 'HTseq/SEQC_shuffled/table_v1.csv'
    
    file1_salmon_shuffled = base_path + 'salmon/counts_seqc_shuffled/table_v1.csv'
    
    file1_kallisto_shuffled = base_path + 'kallisto/SEQC_shuffled_converted/table_v1.csv'
    
    file1_rsem_shuffled = base_path + 'RSEM/seqc_shuffled_results/table_v1.csv'
    
    file1_star_shuffled = base_path + 'STAR/counts_seqc_shuffled/table_v1.csv'
    
    # Simulated data paths
    file1_fc_simulated = base_path + 'featurecounts/counts_seqc_simulated/table.csv'
    file2_fc_simulated_shuffled = base_path + 'featurecounts/counts_seqc_simulated_shuffled/table_v1.csv'
    
    file1_htseq_simulated = base_path + 'HTseq/simulated/table.csv'
    file2_htseq_simulated_shuffled = base_path + 'HTseq/simulated_shuffled/table_v1.csv'
    
    file1_salmon_simulated = base_path + 'salmon/counts_seqc_simulated/table.csv'
    file2_salmon_simulated_shuffled = base_path + 'salmon/counts_seqc_simulated_shuffled/table_v1.csv'
    
    file1_kallisto_simulated = base_path + 'kallisto/simulated_converted/table.csv'
    file2_kallisto_simulated_shuffled = base_path + 'kallisto/simulated_shuffled_converted/table_v9.csv'
    
    file1_rsem_simulated = base_path + 'RSEM/seqc_simulated/table.csv'
    file2_rsem_simulated_shuffled = base_path + 'RSEM/seqc_simulated_shuffled/table_v1.csv'
    
    file1_star_simulated = base_path + 'STAR/counts_seqc_simulated/table.csv'
    file2_star_simulated_shuffled = base_path + 'STAR/counts_seqc_simulated_shuffled/table_v1.csv'


    file2_fc_simulated_rv = base_path + 'featurecounts/counts_seqc_simulated_rv/table.csv'
    
    file2_htseq_simulated_rv = base_path + 'HTseq/simulated_rv/table.csv'

    file2_salmon_simulated_rv = base_path + 'salmon/counts_seqc_simulated_rv/table.csv'
    
    file2_kallisto_simulated_rv = base_path + 'kallisto/simulated_rv_converted/table.csv'
    
    file2_rsem_simulated_rv = base_path + 'RSEM/seqc_simulated_rv/table.csv'
    
    file2_star_simulated_rv = base_path + 'STAR/counts_seqc_simulated_rv/table.csv'
    
    tools = ['featureCount', 'HTseq', 'Salmon', 'Kallisto', 'RSEM', 'STAR']
    file2_actual_gene_counts = base_path + "gene_count_results_for_simulation/table_number.csv"
    
    if mode == 'simulated_vs_rv':
        tools_dir = [(file1_fc_simulated, file2_fc_simulated_rv), (file1_htseq_simulated, file2_htseq_simulated_rv), 
                     (file1_salmon_simulated, file2_salmon_simulated_rv), (file1_kallisto_simulated, file2_kallisto_simulated_rv), 
                     (file1_rsem_simulated, file2_rsem_simulated_rv), (file1_star_simulated, file2_star_simulated_rv)]
    elif mode == 'simulated_vs_shuffled':
        tools_dir = [(file1_fc_simulated, file2_fc_simulated_shuffled ), (file1_htseq_simulated, file2_htseq_simulated_shuffled ), 
                     (file1_salmon_simulated, file2_salmon_simulated_shuffled ), (file1_kallisto_simulated, file2_kallisto_simulated_shuffled), 
                     (file1_rsem_simulated, file2_rsem_simulated_shuffled), (file1_star_simulated, file2_star_simulated_shuffled)]
    elif mode == 'seqc_real_vs_rv':
        tools_dir = [(file1_fc_real, file2_fc_real_rv), (file1_htseq_real, file2_htseq_real_rv), 
                     (file1_salmon_real, file2_salmon_real_rv), (file1_kallisto_real, file2_kallisto_real_rv), 
                     (file1_rsem_real, file2_rsem_real_rv), (file1_star_real, file2_star_real_rv)]
    elif mode == 'seqc_real_vs_shuffled':
        tools_dir = [(file1_fc_real, file1_fc_shuffled), (file1_htseq_real, file1_htseq_shuffled), 
                     (file1_salmon_real, file1_salmon_shuffled), (file1_kallisto_real, file1_kallisto_shuffled), 
                     (file1_rsem_real, file1_rsem_shuffled), (file1_star_real, file1_star_shuffled)]
    elif mode == 'simulated_vs_actual_gene_count':
        tools_dir = [(file2_actual_gene_counts, file1_fc_simulated), (file2_actual_gene_counts, file1_htseq_simulated), 
                     (file2_actual_gene_counts, file1_salmon_simulated), (file2_actual_gene_counts, file1_kallisto_simulated), 
                     (file2_actual_gene_counts, file1_rsem_simulated), (file2_actual_gene_counts, file1_star_simulated)]
    else:
        tools_dir = []  # Default empty list if mode is not recognized
        
    return tools, tools_dir
