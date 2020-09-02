class AnonymousFunction:
    def getDivision(self):
        numList = [45, 55, 60, 65, 37, 100, 115, 105, 120, 220]
        # using anonymous function to filter
        result = list(filter(lambda x: (x % 15 == 0), numList))
        print("Numbers divisible by 15 are",result)

number = AnonymousFunction()
number.getDivision()