#!/bin/bash

# Define constant path
constant_path="/scratch1/fmohebbi/chinese_q_samples_for_synthetic/"

# Define input files
input_files=("$constant_path"*_R1.fastq.gz)

# Loop through input files and submit Slurm jobs
for input_file1 in "${input_files[@]}"
do
    # Extract the filename from the full path
    filename=$(basename "$input_file1" _R1.fastq.gz)"f"
    input_file2="${input_file1/_R1.fastq.gz/_R2.fastq.gz}"
    # Define Slurm job submission script
    cat << EOF > job_${filename}.slurm
#!/bin/bash
#SBATCH --job-name=${filename}
#SBATCH --output=${filename}.out
#SBATCH --error=${filename}.err
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=200G
#SBATCH --time=30:00:00
#SBATCH --account=fmohebbi_1178

# Your commands here
python /scratch1/fmohebbi/Scripts/Shuffling_reads_chinese_q.py "$input_file1" "$input_file2" "f22" 

EOF

    # Submit Slurm job
    sbatch job_${filename}.slurm

    # Optional: Pause between job submissions
    #sleep 1
done
