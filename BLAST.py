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
    parser.add_argument("-d", "--database", help="Path to the database file.", type=str, required=True)
    args = parser.parse_args()

    input_file = args.input
    database_file = args.database

    return database_file, input_file


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


def recup_data(FASTA_FILE):
	data_dict = {}
	with open(FASTA_FILE, 'r') as file :
		num_seq = 1
		seq_list = []
		flag_first = 0
		seq = ""
		for line in file:
			if line[0] == '>':
				if flag_first != 0:
					seq_list.append(seq)
				flag_first = 1
				seq = ""
				data_dict[num_seq] = []
				num_seq += 1
			else:
				seq = seq + line[:-1]
		seq_list.append(seq)
		for id_seq in range(1, len(seq_list)+1):
			words = trois_lettres(seq_list[id_seq-1])
			data_dict[id_seq] = words
	return data_dict





if __name__ == '__main__':
    database_file, input_file = args()

    input_fasta_seq = read_fasta(input_file)
    ##print("Full sequence:\n", input_fasta_seq)

    ##print("\n")

    input_mots = trois_lettres(input_fasta_seq)
    print(input_mots)
    
    data_dict = recup_data(database_file)
    print(data_dict)
