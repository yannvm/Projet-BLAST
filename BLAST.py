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
    if not os.path.isfile(input_file):
        sys.exit(f"{input_file} does not exist.\n"
                "Please enter a valid input fasta file.")

    return input_file


def read_fasta(fasta_file):
    sequence = ""

    with open(fasta_file, "r") as f_in:
        for line in f_in:
            if line[0] != ">":
                sequence += line.strip()

    return sequence           


def trois_lettres(fasta_seq):
    fasta_mots = []

    for i in range(len(fasta_seq)-3):
        fasta_mots.append(fasta_seq[i:i+3])

    return fasta_mots



if __name__ == '__main__':
    input_file = args()

    input_fasta_seq = read_fasta(input_file)
    ##print("Full sequence:\n", input_fasta_seq)

    ##print("\n")

    input_mots = trois_lettres(input_fasta_seq)
    print(input_mots)
