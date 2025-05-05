# strict_clean_clustered_fasta.py

def clean_strict_duplicate_fasta(input_fasta, output_fasta):
    """
    Keeps only entries where the header appears twice in a row,
    and removes any single-instance headers.
    """
    cleaned = []
    with open(input_fasta, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        if lines[i].startswith(">"):
            current_header = lines[i]

            # Check for immediate duplicate header
            if i + 1 < len(lines) and lines[i + 1] == current_header:
                # Keep only if exactly duplicated
                if i + 2 < len(lines) and not lines[i + 2].startswith(">"):
                    cleaned.append(current_header)
                    cleaned.append(lines[i + 2])  # The actual sequence line
                    i += 3  # Move past both headers and the sequence
                else:
                    i += 1  # Skip malformed case
            else:
                i += 1  # Single header: skip
        else:
            i += 1  # Sequence line without header: skip

    with open(output_fasta, "w") as f:
        f.write("\n".join(cleaned) + "\n")

    print(f"✅ Strict cleaned FASTA saved to: {output_fasta}")


if __name__ == "__main__":
    input_fasta = "data/clustered_representatives.fasta"
    output_fasta = "data/clustered_representatives_cleaned.fasta"
    clean_strict_duplicate_fasta(input_fasta, output_fasta)
