class PalindromePair:
    def __init__(self, words):
        self.words = words
        self.pairs = []
        self.palindrome_pair()
    
    def palindrome_pair(self):
        """
        Find all pairs of words that form a palindrome when concatenated.
        """
        # Iterate through each word
        for i in range(len(self.words)):
            # Iterate through each word again to form pairs
            for j in range(len(self.words)):
                # Ensure that a word is not paired with itself
                if i != j:
                    # Check if concatenating the two words forms a palindrome
                    if self.words[i] + self.words[j] == (self.words[i] + self.words[j])[::-1]:
                        # If it forms a palindrome, add the indices of the pair to the pairs list
                        self.pairs.append([i, j])    
    
    def concat(self):
        # Iterate through each pair of indices in the pairs list
        for i in range(len(self.pairs)):
            # Print the concatenated words forming a palindrome
            print(self.words[self.pairs[i][0]] + self.words[self.pairs[i][1]])
        # Print the list of pairs of indices
        print(self.pairs)

# Create an instance of PalindromePair with a list of words
con = PalindromePair(["bat", "tab", "cat", "dog"])

# Call the concat method to print palindromic pairs and their indices
pr = con.concat()
