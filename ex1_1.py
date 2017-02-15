# EXAMPLE
# count = [0, 0, 0, 0]
#
# count[0] += "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC".count('A')


file = open("Vibrio_cholerae.txt")

strings = [line.strip() for line in file]

file.close()

count = [0, 0, 0, 0]  # A   C   G   T

for line in strings:
    count[0] += line.count('A')
    count[1] += line.count('C')
    count[2] += line.count('G')
    count[3] += line.count('T')

print(count)
