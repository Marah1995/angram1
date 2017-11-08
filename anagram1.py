word = open('words.txt','r')
wordlist = word.readlines()
wordclean = [word.strip().lower() for word in wordlist]
SortedWords = {}
for words in wordclean:
    Length = len(words)
    if(SortedWords.has_key(Length)):
        SortedWords[Length].append(words)
    else:
        SortedWords[Length] = []
        SortedWords[Length].append(words)
        
    

