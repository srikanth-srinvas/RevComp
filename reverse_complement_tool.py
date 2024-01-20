# reverse_complement_tool.py

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse

def reverse_complement_fasta(input_file, output_file):
    # Read input FASTA file
    records = list(SeqIO.parse(input_file, "fasta"))

    # Generate reverse complement for each sequence
    reverse_complement_records = []
    for record in records:
        sequence = str(record.seq)
        reverse_complement = str(Seq(sequence).reverse_complement())
        reverse_complement_record = SeqRecord(Seq(reverse_complement), id=record.id, description=record.description)
        reverse_complement_records.append(reverse_complement_record)

    # Write reverse complement sequences to a new FASTA file
    with open(output_file, "w") as output_handle:
        SeqIO.write(reverse_complement_records, output_handle, "fasta")

def main():
    parser = argparse.ArgumentParser(description="Reverse complement sequences in a FASTA file.")
    parser.add_argument("input_file", help="Path to the input FASTA file")
    parser.add_argument("output_file", help="Path to the output FASTA file")

    args = parser.parse_args()

    reverse_complement_fasta(args.input_file, args.output_file)
    print(f"Reverse complement sequences written to {args.output_file}")

if __name__ == "__main__":
    main()
