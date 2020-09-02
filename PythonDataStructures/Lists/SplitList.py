from itertools import groupby
from operator import itemgetter

class SplitList:
    def tosplitList(self, listOfStr):
        for char, gorupwords in groupby(sorted(listOfStr), key=itemgetter(0)):
            print("First Charater : ",char)
            for singleword in gorupwords:
                print("Word Belongs To First Character In List",singleword)

listData = SplitList()
rangeVal = int(input("Enter The range of value you want to enter : "))
listOfStr = []
for i in range(1, rangeVal + 1):
    strVal = input("Enter The Words In List : ")
    listOfStr.append(strVal)

print("List Data :- ", listOfStr)
print("The Updated List Are : ", listData.tosplitList(listOfStr))