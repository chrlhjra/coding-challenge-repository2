class valParenthesis():
    def __init__(self, symbol):
        self.symbol = symbol
        self.parenthesis = []
        self.validParenthesis()
    
    def validParenthesis(self):
        for i in range(0, len(self.symbol)):
            if self.symbol[i] == "(":
                self.parenthesis.append(i)
            elif self.symbol[i] == ")":
                if len(self.parenthesis) == 0:
                    print("False")
                    return
                else:
                    self.parenthesis.pop()
        if len(self.parenthesis) == 0:
            print("True")
        else:
            print("False")

valParenthesis("(((){)")
