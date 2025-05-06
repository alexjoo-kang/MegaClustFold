# 🧬 MegaClustFold 

MegaClustFold is a lightweight and modular pipeline that clusters protein sequences using **MMseqs2 Linclust**. This version is simplified for reproducibility and educational purposes, focusing on basic clustering.

> All input data is **synthetic** and intended for demonstration and testing only.

---

## 🙏 Acknowledgments

This project is inspired by outstanding tools such as **MMseqs2**, **ColabFold**, and **Foldseek** developed by the [Steinegger Lab](https://github.com/steineggerlab). Synthetic sequences are used to ensure reproducibility and open sharing.

Also, this project was developed with extensive assistance from OpenAI's ChatGPT, which provided significant guidance in both designing the pipeline and generating the underlying Python code. 

This repository reflects a learning experience, and I plan to study and improve my understanding of the components involved.

---

## 📁 Project Structure

```

MegaClustFold/
├── data/
│   ├── autism_isoforms.fasta                        # Initial synthetic amino acid sequences
│   ├── cluster_members.tsv                          # MMseqs2 clustering output
│   ├── clustered_representatives.fasta              # Representative sequences from Linclust
│   ├── clustered_representatives_cleaned.fasta      # Strictly cleaned version
├── scripts/
│   └── run_linclust.py                              # Runs MMseqs2 Linclust clustering
├── strict_clean_clustered_fasta.py                  # Removes malformed FASTA headers
├── environment.yml                                  # Conda environment specification
├── .gitignore
└── README.md

````

---

## 📥 How to Download This Repository
You can download this project in two ways:

### ✅ Option 1: Download as ZIP
1. Click the green `Code` button at the top of the GitHub page
2. Select `Download ZIP`
3. Extract the ZIP
4. `cd /path/to/MegaClustFold-main`

> ✅ No git command required

### 🧪 Option 2: Clone with Git
```bash
git clone https://github.com/alexjoo-kang/MegaClustFold.git
cd MegaClustFold
```

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



