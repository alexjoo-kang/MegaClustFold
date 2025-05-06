# 🧬 MegaClustFold 

MegaClustFold is a lightweight and modular pipeline that clusters protein sequences based on amino acid composition (AAC) using **MMseqs2 Linclust**, and then exports cluster-wise sequence files and embeddings. This version is simplified for reproducibility and educational purposes, focusing on basic clustering and AAC extraction.

> All input data is **synthetic** and intended for demonstration and testing only.

---

## 🙏 Acknowledgments

This project is inspired by outstanding tools such as **MMseqs2**, **ColabFold**, and **Foldseek** developed by the [Steinegger Lab](https://github.com/steineggerlab). Synthetic sequences are used to ensure reproducibility and open sharing.

---

## 📁 Project Structure

```

MegaClustFold/
├── data/
│   ├── autism_isoforms.fasta                        # Initial synthetic amino acid sequences
│   ├── cluster_members.tsv                          # MMseqs2 clustering output
│   ├── clustered_representatives.fasta              # Representative sequences from Linclust
│   ├── clustered_representatives_cleaned.fasta      # Strictly cleaned version
│   └── clusters/
│       ├── cluster_0.fasta
│       └── cluster_1.fasta
├── results/
│   └── aac_embeddings.csv                           # Amino Acid Composition embeddings
├── scripts/
│   ├── run_linclust.py                              # Runs MMseqs2 Linclust clustering
│   ├── export_clusters.py                           # Exports sequences per cluster
│   └── export_aac_embeddings.py                     # Computes AAC embeddings
├── strict_clean_clustered_fasta.py                  # Removes malformed FASTA headers
├── environment.yml                                  # Conda environment specification
├── .gitignore
└── README.md

````

---

## 🚀 Quick Start

### 1. Prepare Conda Environment

```bash
conda env create -f environment.yml
conda activate megaclustfold
````

### 2. Run Clustering Pipeline

#### (1) Run MMseqs2 Linclust

```bash
python scripts/run_linclust.py data/autism_isoforms.fasta
```

#### (2) Clean FASTA headers

```bash
python strict_clean_clustered_fasta.py
```

#### (3) Export cluster files

```bash
python scripts/export_clusters.py
```

#### (4) Compute AAC embeddings

```bash
python scripts/export_aac_embeddings.py
```

---

## 🔬 Optional: Structure Prediction with ColabFold

You can manually predict the 3D structures of clustered representative sequences using [ColabFold](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb).
### Example Input: `clustered_representatives_cleaned.fasta`

```
>FOXP2_variant_X
MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNEAELKVLQKAFSKLGAKEMNEE
>SHANK3_synthetic_A
MSEQNNTEMTFQIQRIYTKDISFEYKKMVDGVEKMVVKAFSKLGAEMDKLDSIEQKKLNQTSKLTMELESTFKVVVYKPWTKLLTP
```

Use one sequence at a time in the ColabFold notebook (`Run All`) and download the resulting files, which includes `.pdb` files.

---

## 🧠 Optional: Compare 3D Structures using Foldseek

Once you have `.pdb` structure files from ColabFold, you can use [Foldseek](https://github.com/steineggerlab/foldseek) for structural similarity comparison.

---

## 📦 Conda Environment (environment.yml)

```yaml
name: megaclustfold
channels:
  - conda-forge
  - bioconda
dependencies:
  - python=3.10.17
  - pip=25.0.1
  - mmseqs2=17.b804f
  - pip:
      - biopython==1.82
```

---

## 🔖 License

MIT License



