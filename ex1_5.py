def countPattern(text, pattern):
    count = []

    for i in range(len(text) - len(pattern) + 1):
        #print(pattern + " - " + text[i: i + len(pattern)])
        if pattern == text[i: i + len(pattern)]:
            count.append(i)

    return count

text = input()
pattern = input()


#countPattern("GCGCG","GCG")

print(countPattern(text,pattern))
