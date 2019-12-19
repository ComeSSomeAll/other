def distance(a, b):
    # Calculates the Levenshtein distance between a and b.
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)  # Keep current and previous row, not entire matrix
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

fin = open("brain111.txt")
fin2 = open("dict1.txt")
text = fin.read()
text2 = fin2.read().split()
splittext = text.replace('!','').replace('?','').replace(',','').replace(';','').replace('.','').replace(':','').replace('«','').replace('»','').replace('(','').replace(')','').replace('—','').lower().split()
countOfWordform = len(splittext)
countOfDifWordform = []
for i in range(countOfWordform):
    if splittext[i] not in countOfDifWordform:
        countOfDifWordform.append(splittext[i])
k=0
for i in range(len(countOfDifWordform)):
    if countOfDifWordform[i] in text2:
        k+=1
print(len(countOfDifWordform))
print(k)