def ReverseComplement(dna):
    reverse = {'A': 'T', 'C': 'G','G': 'C', 'T': 'A'}

    return ''.join([reverse[i] for i in dna[::-1]])

print(ReverseComplement(input()))
