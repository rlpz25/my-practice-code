def rmWhiteSpace(lo):
    if " " in lo:
        lo.pop(lo.index(" "))
        rmWhiteSpace(lo)

def processAnagram(word):
    wordCh = []
    word = word.upper()
    for ch in word:
        wordCh.append(ch)
    
    # wordCh.sort()
    rmWhiteSpace(wordCh)
    print(wordCh)