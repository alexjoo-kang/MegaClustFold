# scripts/export_aac_embeddings.py

import os
import csv
from Bio import SeqIO
from collections import Counter

# List of 20 standard amino acids (alphabetical order for consistency)
AMINO_ACIDS = sorted("ACDEFGHIKLMNPQRSTVWY")

def compute_aac(sequence):
    """
    Computes the Amino Acid Composition (AAC) for a given sequence.
    Returns a dictionary with amino acid frequencies normalized by sequence length.
    """
    length = len(sequence)
    count = Counter(sequence)
    return {aa: count.get(aa, 0) / length for aa in AMINO_ACIDS}

def main():
    input_dir = "data/clusters"
    output_csv = "results/aac_embeddings.csv"

    if not os.path.exists(input_dir):
        print(f"❌ Input directory not found: {input_dir}")
        return

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Header row: cluster_id, sequence_id, then 20 amino acids
        writer.writerow(["cluster_id", "sequence_id"] + AMINO_ACIDS)

        for cluster_file in sorted(os.listdir(input_dir)):
            if not cluster_file.endswith(".fasta"):
                continue

            cluster_id = os.path.splitext(cluster_file)[0]
            cluster_path = os.path.join(input_dir, cluster_file)

            for record in SeqIO.parse(cluster_path, "fasta"):
                aac = compute_aac(str(record.seq))
                row = [cluster_id, record.id] + [aac[aa] for aa in AMINO_ACIDS]
                writer.writerow(row)

    print(f"✅ AAC embeddings exported to: {output_csv}")

if __name__ == "__main__":
    main()
