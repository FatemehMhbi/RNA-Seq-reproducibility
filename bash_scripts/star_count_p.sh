#!/bin/bash

# Define constant path
constant_path="/project/fmohebbi_1178/RNA-seq_project/RNA-seq-repd/Computational_replicates/Chinese_quartet/Chinese_q_shuffled/"
output="/scratch1/fmohebbi/quantification_results/Star_chinese_q_shuffled"
GTF="/project/fmohebbi_1178/RNA-seq_project/Ref_ind_chart/Homo_sapiens.GRCh38.110.chr.gtf"
index="/project/fmohebbi_1178/RNA-seq_project/Ref_ind_chart/star_index"

# Define input files
input_files=("$constant_path"*_R1.fastq.gz)

# Loop through input files and submit Slurm jobs
for input_file1 in "${input_files[@]}"
do
    echo "processing: "$input_file1
    # Extract the filename from the full path
    filename=$(basename "$input_file1" _R1.fastq.gz)
    echo $filename
    input_file2="${input_file1/_R1.fastq.gz/_R2.fastq.gz}"
    # Define Slurm job submission script
    cat << EOF > job_${filename}.slurm
#!/bin/bash
#SBATCH --job-name=${filename}
#SBATCH --output=${filename}.out
#SBATCH --error=${filename}.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=120G
#SBATCH --time=20:00:00
#SBATCH --partition=main

module load conda
source activate star_env

cd $output
  STAR --runThreadN 10\
  --genomeDir ${index} \
  --readFilesCommand zcat \
  --readFilesIn $input_file1 $input_file2  \
  --sjdbGTFfile ${GTF} \
  --quantMode GeneCounts \
  --outFileNamePrefix ${filename}.bam

EOF

    # Submit Slurm job
    sbatch job_${filename}.slurm

    # Optional: Pause between job submissions
    #sleep 1
done
