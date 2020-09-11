import os
import sys
import argparse

def args():
    """Parse the command-line arguments.

    Arguments
    ---------
    Python command-line

    Returns
    -------
    fasta_file: string
    """

    # Declaration of expexted arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Path to the input fasta file.", type=str, required=True)
    args = parser.parse_args()

    # Check if the fasta files directory is valid
    input_file = args.input
    if not os.path.isfile(pdb_file):
        sys.exit(f"{input_file} does not exist.\n"
                "Please enter a valid input fasta file.")

    return input_file



if __name__ == '__main__':
    input_file = args()

    with open(input_file, "r") as f_in:
        for line in f_in:
            if line[0] != ">":
                
