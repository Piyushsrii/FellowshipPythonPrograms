import sys
class RecursionLimit:
    def limit(self):
        print("Current value of the recursion limit:")
        print(sys.getrecursionlimit())
        
recursion = RecursionLimit()
recursion.limit()
