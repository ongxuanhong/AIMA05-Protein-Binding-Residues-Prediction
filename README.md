# AIMA05-Protein-Binding-Residues-Prediction

## Data files
- Training set 
    - Protein sequence
    - Ground truth files: metal, nuclear acid, small molecules

- Independent set
    - Protein sequence
    - Ground truth files: metal, nuclear acid, small molecules

## Data preprocessing
- Protein sequence: remove unatural sequence, sort.
- Ground truth: 3 into 1, categorize in numbers, filter out redundant sequences, sort.
- Feature engineering: Descriptor by Protr.org, amino acid encoding.

## Descriptor with  ProtrWeb
- http://protr.org/

## Models
- Random forest
- CNN (Conv1D)

## BindEmbed21 model
- https://github.com/Rostlab/bindPredict

**Background**
- Importance of predicting protein binding sites
    - Knowing protein function is crucial to understand the molecular mechanisms of life.
    - For most proteins, function depends on binding to other molecules called ligands.
    - Binding sites are highly specific and often determined by a few key residues.

- Traditional methods
    - Tranditional methods often rely on experimental data and homology modeling, requiring the construction of multiple sequence alignmens (MSAs).
    - However, creating high-quality MSAs is time-consuming and computationally intensive, especially for proteins with low sequence homology of insufficient homologous sequences.


**Dataset**
- Transformer-based protein Language Model (pLM) ProtT5 as input.
- Annotations from BioLiP.

**Model architecture**
- The BindEmbed21 model combines homology-based inference (HBI) and ML methods to predict protein binding sites.
- The model's performance was evaluated using precision, recall, F1 score, and Matthews correlation coefficient (MCC) to compare results with and without using MSAs.

## References
- ProtVec: A Continuous Distributed Representation of Biological Sequences (https://arxiv.org/abs/1503.05140)
- https://github.com/mikejhuang/PhageProtVec