#!/bin/bash

# Define constant path
constant_path="/scratch1/fmohebbi/chinese_simulated_rv_hisat2/"
output="/scratch1/fmohebbi/quantification_results/featureCount_chinese_simulated_rv"
GTF="/project/fmohebbi_1178/RNA-seq_project/Ref_ind_chart/Homo_sapiens.GRCh38.110.chr.gtf"

# Define input files
input_files=("$constant_path"*.bam)


# Loop through input files and submit Slurm jobs
for input_file1 in "${input_files[@]}"
do
    echo "processing: "$input_file1
    # Extract the filename from the full path
    filename=$(basename "$input_file1" .bam)
    echo $filename
    # Define Slurm job submission script
    cat << EOF > job_${filename}.slurm
#!/bin/bash
#SBATCH --job-name=${filename}
#SBATCH --output=${filename}.out
#SBATCH --error=${filename}.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=60G
#SBATCH --time=20:00:00
#SBATCH --partition=main

module load conda
source activate featurecount_tool

cd $output
featureCounts -p --countReadPairs -t exon -g gene_id -a $GTF -o ${filename}_featurecount.txt $input_file1

EOF

    # Submit Slurm job
    sbatch job_${filename}.slurm

    # Optional: Pause between job submissions
    #sleep 1
done
