def readFile(fileName):
    inFile = open(fileName, 'r')
    content = inFile.read()
    inFile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)

nWords, nChars = readFile('teste.txt')
print(nChars, nWords)