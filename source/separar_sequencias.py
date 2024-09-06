from Bio import SeqIO

# Carregar o arquivo FASTA contendo as sequências alinhadas
fasta_file = "aligned_sequences.fasta"  # Substitua pelo seu arquivo

# Ler as sequências alinhadas
aligned_sequences = list(SeqIO.parse(fasta_file, "fasta"))

# Exibir as sequências carregadas
for seq_record in aligned_sequences:
    print(f"ID: {seq_record.id}")
    print(f"Sequência: {seq_record.seq}\n")
