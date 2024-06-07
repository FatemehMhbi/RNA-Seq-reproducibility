# RNA-Seq-reproducibility

This repository includes the bash scripts used to run RNA-Seq quantification tools and the Python codes used to calculate the consistency percentages and draw box plots. Most of the bash scripts are to run the tools for RNA-Seq replicates in parallel by submitting a Slurm job for each replicate separately. 


Chinese_q_analysis.py \
This script is specifically for Chinese Quartet data since it has 4 samples with ids (D5, D6, M8, F7]. It reads the output of tools, featureCounts, HTSeq, Salmon, Kallisto, RSEM, and STAR-count, calculates the absolute gene count differences and the average consistency percentages for three thresholds [0, 0.01, 0.1], and draws the box plot. When running it make sure the header and separators are set for each tool’s files accordingly. The gene counts are compared within the libraries in this script if you want them to be across the libraries then you need to change how x and y variables (files) are picked.
This script uses “utils_for_rna_seq_analysis.py” which includes a function to draw a consistency box plot.


Consistency_threshold_based.py \
The threshold here is defined differently. I considered thresholds [1, 10, 100]. For each threshold it counts the number of genes that their gene count difference is above 1, 10, and 100. We are not using this type of thresholds. It was used only to compare the extend of gene count differences across the tools. With a bit of modification you can get top genes for the tools using the functions defined in this script. 
To run this script you need the absolute gene count difference files that are the output of “get_abs_gene_count_differences.py”. We might want to combine them at some points. 


Convert_kallisto_results.py \
This script simply read abundance.tsv files for SEQC data (outputs of kallisto, includes 5 columns) and extact the tpm or gene count columns and save them as a txt file. 

Convert_tpm_to_gene_count.py \
This script converts tpm to gene count. It needs a mart export file as input that contains the list of genes and their corresponding transcripts. 

Featurecount_output_converstion.py \
This script extract gene expression levels out of featureCounts output (which includes multiple columns).

Find_read_transcript_assinment.py \
This script is specifically for RSEM output for simulated data. In simulated data (obtained from Polyester), the name of the reads includes the name of the transcript they belong to. Using the bam files generated by RSEM we can see what transcript each read is assigned.


Rna-seq_results_analysis_and_box_plot.py \
This script outputs the box plot for SEQC, shuffled and reverse complement versions. Three thresholds are considered [0, 0.01, 0.1]. The inputs for this script are outputs of “get_results_table.py. It calculates the average consistency percentages for each threshold for each tool. It uses the script “get_inputs.py”. 

Star_output_conversion.py \
The output of STAR-count include multiple columns. This script extract the gene counts. 
