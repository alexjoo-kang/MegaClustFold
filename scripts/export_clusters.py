import os
from collections import defaultdict
from Bio import SeqIO

def read_fasta_as_dict(fasta_path):
    """Parses FASTA into a dict of {sequence_id: sequence_object}."""
    return {record.id: record for record in SeqIO.parse(fasta_path, "fasta")}

def parse_cluster_tsv(tsv_path):
    """Parses TSV and returns {rep_id: [member1, member2, ...]}."""
    clusters = defaultdict(list)
    with open(tsv_path, "r") as f:
        for line in f:
            rep, member = line.strip().split("\t")
            clusters[rep].append(member)
    return clusters

def export_clusters(fasta_path, tsv_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    seq_dict = read_fasta_as_dict(fasta_path)
    clusters = parse_cluster_tsv(tsv_path)

    for i, (rep_id, member_ids) in enumerate(clusters.items()):
        cluster_file = os.path.join(output_dir, f"cluster_{i}.fasta")
        with open(cluster_file, "w") as out_f:
            for member_id in member_ids:
                if member_id in seq_dict:
                    SeqIO.write(seq_dict[member_id], out_f, "fasta")
                else:
                    print(f"⚠️ Warning: {member_id} not found in FASTA.")

    print(f"✅ Exported {len(clusters)} clusters to '{output_dir}'.")

if __name__ == "__main__":
    cluster_tsv = "data/cluster_members.tsv"
    fasta_input = "data/clustered_representatives_cleaned.fasta"
    output_dir = "data/clusters"
    
    export_clusters(fasta_input, cluster_tsv, output_dir)
