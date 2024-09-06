def parse_sequences_from_txt(file_path):
    with open(file_path, 'r') as file:
        sequences = {}
        current_header = None
        current_sequence = []

        for line in file:
            line = line.strip()
            if line.startswith('>'):  # New sequence header
                if current_header:
                    # Save the previous sequence
                    sequences[current_header] = ''.join(current_sequence)
                current_header = line  # Store the header
                current_sequence = []  # Reset sequence list for the new header
            else:
                current_sequence.append(line)  # Add DNA sequence parts

        # Don't forget to save the last sequence
        if current_header:
            sequences[current_header] = ''.join(current_sequence)

    return sequences

# Exemplo de uso
file_path = 'seqdump.txt'
sequences = parse_sequences_from_txt(file_path)

# Printar os primeiros 100 nucleotídeos da primeira sequência
for header, sequence in sequences.items():
    print(f"{header} -> {sequence[:100]}")
    break
