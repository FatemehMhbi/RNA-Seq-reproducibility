#!/bin/bash

# Define constant path
constant_path="/project/fmohebbi_1178/RNA-seq_project/RNA-seq-repd/Computational_replicates/Chinese_quartet/Chinese_q_simulated_polyester/simulated_reads_rsem_chinese_q_fastq/"
output="/scratch1/fmohebbi/quantification_results/RSEM_chinese_simulated"
index='/project/fmohebbi_1178/RNA-seq_project/Ref_ind_chart/rsem_ref_ensmbl_110/human_ensembl'

# Define input files
input_files=("$constant_path"*_1.fastq)

# Loop through input files and submit Slurm jobs
for input_file1 in "${input_files[@]}"
do
    echo "processing: "$input_file1
    # Extract the filename from the full path
    filename=$(basename "$input_file1" _1.fastq)
    echo $filename
    input_file2="${input_file1/_1.fastq/_2.fastq}"
    # Define Slurm job submission script
    cat << EOF > job_${filename}.slurm
#!/bin/bash
#SBATCH --job-name=${filename}
#SBATCH --output=${filename}.out
#SBATCH --error=${filename}.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --mem=50G
#SBATCH --time=24:00:00
#SBATCH --partition=main

# Your commands here
module load conda
source activate rsem_env

cd $output

rsem-calculate-expression -p 12 --bowtie2 --paired-end --no-bam-output --append-names $input_file1 $input_file2 $index $filename

EOF

    # Submit Slurm job
    sbatch job_${filename}.slurm

    # Optional: Pause between job submissions
    #sleep 1
done
