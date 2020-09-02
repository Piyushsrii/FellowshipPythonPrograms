class CountListItem:
    def itemCount(self,dictOfList):
        ctr = sum(map(len, dictOfList.values()))
        print(ctr)

dictList = CountListItem()
dictRange = int(input("Enter The range of value you want to enter in dictionary : "))
listRange = int(input("Enter The range of value you want to enter in dictionary : "))
dictOfList = { }
for i in range(1,dictRange+1):
    key = input("Enter The Key : ")
    valArr = [ ]
    for j in range(1, listRange + 1):
        val = input("Enter The value for dictionary : ")
        valArr.append(val)
    dictOfList.setdefault(key, valArr)
print (dictOfList)
dictList.itemCount(dictOfList)
