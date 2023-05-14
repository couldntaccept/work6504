import random

def remove_random_lines(input_file, output_file, p=0.1):
    """Remove random lines from a file.

    Args:
    input_file (str): Path to the input file.
    output_file (str): Path to the output file.
    p (float, optional): Probability of removing a line. Defaults to 0.1.
    """
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            if random.random() >= p:
                f_out.write(line)

# Use the function
remove_random_lines('dups_removed_sorted.txt', 'final_result.txt', p=0.1)
