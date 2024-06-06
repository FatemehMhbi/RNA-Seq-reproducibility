import sys
import random
import os
import gzip


def read_fastq_pairs(input_file1, input_file2):
    """Reads paired-end FASTQ files and yields read pairs."""
    with open(input_file1, 'r') as f1, open(input_file2, 'r') as f2:
        pairs = []
        while True:
            try:
                pair = [
                    next(f1).strip(),
                    next(f1).strip(),
                    next(f1).strip(),
                    next(f1).strip(),
                    next(f2).strip(),
                    next(f2).strip(),
                    next(f2).strip(),
                    next(f2).strip()
                ]
                pairs.append(pair)
            except StopIteration:
                break
    return pairs

def write_fastq_pairs(read_pairs, output_file1, output_file2):
    """Writes shuffled paired-end read pairs to FASTQ files."""
    with open(output_file1, 'w') as f1, open(output_file2, 'w') as f2:
        for pair in read_pairs:
            f1.write('\n'.join(pair[:4]) + '\n')
            f2.write('\n'.join(pair[4:]) + '\n')

def shuffle_paired_fastq_reads(input_file1, input_file2, num_versions, iter):
    """Shuffles paired-end reads in FASTQ files while preserving read pairs."""
    read_pairs = read_fastq_pairs(input_file1, input_file2)
    filename1 = os.path.basename(input_file1)
    filename_no_extension1 = os.path.splitext(filename1)[0]
    
    filename2 = os.path.basename(input_file2)
    filename_no_extension2 = os.path.splitext(filename2)[0]
    
    for version in range(1, num_versions + 1):
        shuffled_pairs = random.sample(read_pairs, len(read_pairs))
        output_file1 = output_dir + filename_no_extension1 + '_shuffled_v' + iter + str(version) + '.fastq'
        output_file2 = output_dir + filename_no_extension2 + '_shuffled_v' + iter + str(version) + '.fastq'
        write_fastq_pairs(shuffled_pairs, output_file1, output_file2)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file1 input_file2")
        sys.exit(1)
    
    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]
    output_dir='/scratch1/fmohebbi/Chinese_simulated_10_v_shuffled/'
    iter = sys.argv[3]

    shuffle_paired_fastq_reads(input_file1, input_file2, 10, iter)
