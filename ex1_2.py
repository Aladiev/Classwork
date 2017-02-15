def countPattern(text, pattern):
    count = 0

    for i in range(len(text) - len(pattern) + 1):
            if pattern == text[i: i + len(pattern)]:
                count += 1

    return count

# INPUT
file = open("PatternCount.txt")

strings = [line.strip() for line in file]

file.close()
#----------------------------------------
text = strings[0]
pattern = strings[1]

#countPattern("GCGCG","GCG")

print(countPattern(text,pattern))
