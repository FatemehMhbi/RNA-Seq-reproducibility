import csv
import os
import pandas as pd
import re, glob, sys



def find_file_in_subfolders(root_folder, file_name):
    files_list = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if file_name in filenames:
            files_list.append(dirpath + "/")
    return files_list


# input_dir = "/Users/fatemehmohebbi/Downloads/rna_seq_results/kallisto_output_sample_A_converted/tpm_files/"
input_dir = "/Users/fmohebbi/Downloads/rna-seq-results/real_data/kallisto_quartet/"
mart_file = '/Users/fmohebbi/Downloads/rna-seq-results/mart_export.txt'
df = pd.read_csv(mart_file, delimiter=',')
gene_data = df.set_index('Transcript stable ID').to_dict()['Gene stable ID']

files = glob.glob(os.path.join(input_dir, "*abundance.tsv")) # "*tpm.txt"))
input_file = ''

pos_tpm = -1


for f in files:
    TPMDict = {}  # keys are geneIDs or transcript IDs, values are total expression for that gene or transcript
    total_tpms = 0

    with open(f + input_file, "r") as TPMFile:
        # next(TPMFile)  # Skip header
        Missing = 0
        total = 0
        for line in TPMFile:
            words = re.split(' |\t', line)
            if words[0].startswith('ENS'):
                gene_or_transcript_id = words[0].split(".")[0]
                TPM = float(words[pos_tpm])
                total_tpms += TPM
                total += 1
                if gene_or_transcript_id not in gene_data:
                    Missing += 1
                    continue
    
                key = gene_data[gene_or_transcript_id]
                if key not in TPMDict:
                    TPMDict[key] = 0
                TPMDict[key] += TPM
            else:
                continue
            
    factor = total_tpms/1000000
    count_dict = {key: value * factor for key, value in TPMDict.items()}

    if os.path.exists(f + 'geneCount.txt'):
        os.remove(f + 'geneCount.txt')

    with open(f + 'geneCount.txt', 'w') as fi:
        for ID, value in TPMDict.items():
            fi.write(ID + " " + str(value) + "\n")

    print("missing transcripts:", Missing)
    print("total:", total)
