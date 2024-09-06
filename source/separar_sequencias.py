from Bio import SeqIO

# Carregar a sequência FASTA
input_file = "Mus_musculus.GRCm39.dna_sm.chromosome.19.fa"
output_prefix = "mouse_chr22_part"

# Definir o tamanho máximo por parte (e.g., 10 milhões de nucleotídeos)
chunk_size = 10000000

# Dividir a sequência
with open(input_file) as fasta_file:
    record = next(SeqIO.parse(fasta_file, "fasta"))
    sequence = record.seq
    for i in range(0, len(sequence), chunk_size):
        chunk = sequence[i:i+chunk_size]
        output_file = f"{output_prefix}_{i//chunk_size+1}.fa"
        with open(output_file, "w") as out_file:
            out_file.write(f">{record.id}_part{i//chunk_size+1}\n")
            out_file.write(str(chunk) + "\n")
