class palindromePairs():
    def __init__(self, words):
        self.words = words
        self.pairs = []
        self.palindromePair()
    
    def palindromePair(self):
        for i in range(0, len(self.words)):
            for j in range(0, len(self.words)):
                if i != j:
                    if self.words[i] + self.words[j] == (self.words[i] + self.words[j])[::-1]:
                        self.pairs.append([i, j])
                    else:  
                        print("not palindrome")  
    def concat(self):
        for i in range(len(self.pairs)):
            print(self.words[self.pairs[i][0]] + self.words[self.pairs[i][1]])
        print(self.pairs)

con = palindromePairs(["bat", "tab", "cat", "dog"])
pr = con.concat()
