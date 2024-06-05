class ValParenthesis:
    def __init__(self, symbol):
        self.symbol = symbol
        self.parenthesis = []
        self.valid_parenthesis()
    
    def valid_parenthesis(self):
        """
        Check if the given string of symbols has valid and balanced parentheses.
        """
        # Iterate through each character in the symbol string
        for i in range(len(self.symbol)):
            # If the character is an opening parenthesis, add its index to the list
            if self.symbol[i] == "(":
                self.parenthesis.append(i)
            # If the character is a closing parenthesis
            elif self.symbol[i] == ")":
                # Check if there is no matching opening parenthesis
                if len(self.parenthesis) == 0:
                    # Print False and return if unbalanced
                    print("False")
                    return
                else:
                    # Pop the last opening parenthesis index if matched
                    self.parenthesis.pop()
        # If the list is empty, all parentheses are balanced
        if len(self.parenthesis) == 0:
            print("True")
        else:
            # If the list is not empty, there are unmatched opening parentheses
            print("False")

# Create an instance of ValParenthesis with a string of symbols
ValParenthesis("(((){)")
