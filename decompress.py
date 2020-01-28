
alphabet = ['a', 'b']
originalText = ''
compressedText = '012233588'
# compressedText = input()
size = len(compressedText)
pCode = list(alphabet)
p = ''
lastP = ''
start = 0


def updatePcode(firstCharP, lastP, pCode):

    pc = lastP + firstCharP
    if pc not in pCode:
        pCode.append(pc)

    return pCode


while start < size:
    lastP = p
    code = int(compressedText[start])
    if code < len(pCode):
        p = pCode[code]
        if p in pCode:
            originalText += str(p)
            if lastP != '':
                pCode = updatePcode(p[0], lastP, pCode)
            start += 1
    else:
        pCode = updatePcode(lastP[0], lastP, pCode)
        p = pCode[code]
        originalText += str(p)
        pCode = updatePcode(p[0], lastP, pCode)
        start += 1

print(pCode)
print('original: ', originalText)
