class DeterminVariable:
    def defineVariable(self):
        try:
            x = int(input("Enter First Variable : "))
        except ValueError:
            print("Variable is not defined....!")
        else:
            print("Variable is defined.")
        try:
            y = int(input("Enter Second Variable : "))
        except ValueError:
            print("Variable is not defined....!")
        else:
            print("Variable is defined.")


var = DeterminVariable()
var.defineVariable()