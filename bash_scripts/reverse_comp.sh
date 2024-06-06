#!/bin/bash

#SBATCH --time=30:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=200G
#SBATCH --account=fmohebbi_1178
#SBATCH --partition=gpu

module load conda
source activate fastx_k

constant_path="/project/fmohebbi_1178/RNA-seq_project/RNA-seq-repd/Computational_replicates/Chinese_quartet/Chinese_q_simulated_polyester/simulated_reads_rsem_chinese_q_fastq/"
output_dir="/scratch1/fmohebbi/Chinese_q_simulated_rv"

for file in ${constant_path}/*.fastq; do
    FILENAME="$(basename -- $file)"
    ID="${FILENAME%.*}"

    #echo "Processing sample ${ID}"
    if [ -e "${output_dir}/${ID}_rv.fastq.gz" ]; then
        echo "File ${ID} exists"
    else
        echo "File does not exist"
        echo "Processing sample ${ID}"
        #zcat ${file} | fastx_reverse_complement -z -o "${output_dir}/${ID}_rv.fastq.gz"
        fastx_reverse_complement -i ${file} -o "${output_dir}/${ID}_rv.fastq"
    fi

done
