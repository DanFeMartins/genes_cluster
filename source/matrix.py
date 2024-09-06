from Bio import SeqIO
import numpy as np

# Função para calcular a similaridade entre duas sequências alinhadas
def calc_similarity(seq1, seq2):
    # Contagem de correspondências
    matches = sum(1 for a, b in zip(seq1, seq2) if a == b and a != '-')
    return matches / len(seq1)  # Similaridade percentual

# Função para criar a matriz de similaridade
def create_similarity_matrix(sequences):
    num_seqs = len(sequences)
    similarity_matrix = np.zeros((num_seqs, num_seqs))

    # Comparar cada sequência com as demais
    for i in range(num_seqs):
        for j in range(i, num_seqs):
            if i == j:
                similarity_matrix[i][j] = 1.0  # Similaridade máxima consigo mesmo
            else:
                similarity = calc_similarity(sequences[i].seq, sequences[j].seq)
                similarity_matrix[i][j] = similarity
                similarity_matrix[j][i] = similarity  # Simetria na matriz

    return similarity_matrix

# Ler o arquivo de sequências alinhadas (fasta format)
def load_sequences(file_path):
    sequences = list(SeqIO.parse(file_path, "fasta"))
    return sequences

# Exemplo de uso
file_path = "seqdump.txt"
sequences = load_sequences(file_path)

similarity_matrix = create_similarity_matrix(sequences)

# Exibir a matriz
import pandas as pd
gene_names = [seq.id for seq in sequences]
df = pd.DataFrame(similarity_matrix, index=gene_names, columns=gene_names)
print(df)

# Caso precise salvar a matriz para usar em outro software
df.to_csv('matriz_de_similaridade.csv')
