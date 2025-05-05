import os
import subprocess
import shutil
import tempfile
import argparse

def run_linclust(input_fasta, output_fasta, cluster_tsv, min_seq_id=0.9):
    if not os.path.exists(input_fasta):
        print(f"❌ Input FASTA file does not exist: {input_fasta}")
        return

    with tempfile.TemporaryDirectory() as tmpdir:
        db_dir = os.path.join(tmpdir, "db")
        res_dir = os.path.join(tmpdir, "res")

        # Step 1: Create MMseqs2 DB
        subprocess.run(["mmseqs", "createdb", input_fasta, db_dir], check=True)

        # Step 2: Run Linclust clustering
        subprocess.run([
            "mmseqs", "linclust", db_dir, res_dir, tmpdir,
            "--min-seq-id", str(min_seq_id)  # 👈 User can adjust this value
        ], check=True)

        # Step 3: Create representative sequence output
        subprocess.run(["mmseqs", "createseqfiledb", db_dir, res_dir, os.path.join(tmpdir, "rep_seqs")], check=True)

        # Step 4: Convert DB to FASTA
        subprocess.run(["mmseqs", "result2flat", db_dir, db_dir, os.path.join(tmpdir, "rep_seqs"), output_fasta], check=True)

        # Step 5: Create cluster mapping
        cluster_map_file = os.path.join(tmpdir, "cluster_mapping.tsv")
        subprocess.run(["mmseqs", "createtsv", db_dir, db_dir, res_dir, cluster_map_file], check=True)

        shutil.move(cluster_map_file, cluster_tsv)

    print(f"✅ Clustering complete.")
    print(f"📄 Representatives: {output_fasta}")
    print(f"📄 Cluster Map:     {cluster_tsv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run MMseqs2 Linclust on a FASTA file.")
    parser.add_argument("input_fasta", help="Input FASTA file path")
    parser.add_argument("--min-seq-id", type=float, default=0.9, help="Minimum sequence identity for clustering (default: 0.9)")
    args = parser.parse_args()

    input_fasta = args.input_fasta
    output_fasta = "data/clustered_representatives.fasta"
    cluster_tsv = "data/cluster_members.tsv"

    run_linclust(input_fasta, output_fasta, cluster_tsv, min_seq_id=args.min_seq_id)
