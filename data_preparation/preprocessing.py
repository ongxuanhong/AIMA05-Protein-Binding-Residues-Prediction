protvec_dim = 100 # the dimension of the ProtVec embeddings
amino_acids = "ACDEFGHIKLMNPQRSTVWY" # the 20 amino acids
protvec = {aa: np.random.rand(protvec_dim) for aa in amino_acids} # load the ProtVec embeddings

def sequence_to_protvec(sequence):
    vec = np.zeros(protvec_dim)
    for aa in sequence:
        if aa in protvec:
            vec += protvec[aa]
    return vec / len(sequence)

def prepare_data(df):
    # convert the sequences to Prot
    df["Protein1_vec"] = df["Protein1"].apply(sequence_to_protvec)
    df["Protein2_vec"] = df["Protein2"].apply(sequence_to_protvec)

# load the protein binding file to analyze the format and structure of the data
file_path = "binding_residues_meta.txt"

# read the file and display its content
with open(file_path) as f:
    protein_binding_data = f.readlines()

# show the first few lines to understand the data format
protein_binding_data[:5]

# the raw data includes protein IDs and their corresponding binding sites positions
# separated by commas, indicating multiple binding sites for each protein.


# process the data to find the maxium binding site index
max_binding_site = 0
protein_bindings = {}

for line in protein_binding_data:
    parts = line.strip().split('\t')
    protein_id = parts[0]
    binding_sites = list(map(int, parts[1].split(',')))
    protein_bindings[protein_id] = binding_sites
    max_binding_site = max(max_binding_site, *binding_sites)

max_binding_site, len(protein_bindings)
# (5399, 681)
# the maxium binding site index is 5399, and there are 681 proteins in the dataset