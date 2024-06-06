#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=30
#SBATCH --mem=100GB
#SBATCH --time=48:00:00
#SBATCH --account=fmohebbi_1178
#SBATCH --partition=main

module load conda
source activate salmon

output='/scratch1/fmohebbi/quantification_results/salmon_chinese_simulated_rv'
fastq="/scratch1/fmohebbi/Chinese_q_simulated_rv"
index="/project/fmohebbi_1178/RNA-seq_project/RNA-seq-repd/results_april19/quantification-tools/salmon/index/salmon_index"

echo "Salmon test RNA-seq samples mapping"
#cd $fastq
for file1 in "${fastq}"/*_1_rv.fastq; do
  base=$(basename ${file1} .fastq)
  modified_name="${base//_1_rv/}"
  echo ${modified_name}
  echo ${file1}

  file2="${file1/_1_rv.fastq/_2_rv.fastq}"
  echo ${file2}
  salmon quant -i ${index}  -l A  -1 ${file1}  -2 ${file2} -p 30 --validateMappings -o ${output}/${modified_name}
done

echo "Salmon finished running!"
