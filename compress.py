
alphabet = ['a', 'b']
originalText = "abababbabaabbabbaabba"
#originalText = input()
size = len(originalText)
pCode = list(alphabet)
compressedText = ''
p = ''
start = 0
length = 0


def findLongestPrefix(org, i, pCode, compressed):
    nextBy = 1
    p = org[i]
    includeLatestP = 0
    while nextBy < size - i:
        if p in pCode:
            nxt = org[i + nextBy]
            t = pCode.index(p)
            p = p + nxt
            nextBy += 1
            includeLatestP = 1
        else:
            includeLatestP = 0
            compressed += str(t)
            pCode.append(p)
            break
    if includeLatestP == 1:
        compressed += str(pCode.index(p))

    return pCode.index(p), len(p), compressed


while start < size:
    p, length, compressedText = findLongestPrefix(originalText, start, pCode, compressedText)
    if length > 2:
        start = start + len(pCode[p]) - 1
    else:
        start += 1

print(pCode)
print('compressed: ', compressedText)
