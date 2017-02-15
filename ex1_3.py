def countPattern(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
            if pattern == text[i: i + len(pattern)]:
                count += 1
    return count

def FrequentWords(text,k):
    FrequentPatterns = set()

    Count = [0 for i in text]

    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        Count[i] = countPattern(text, pattern)

    maxCount = max(Count)

    for i in range(len(text) - k + 1):
        if Count[i] == maxCount:
            FrequentPatterns.add(text[i:i+k])

    return FrequentPatterns


text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

print(FrequentWords(text,k))

