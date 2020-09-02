class RemoveItems:
    def toremove(self,setValue,rmVal):
        for i in range(rmVal):
            setValue.pop()
        print(setValue)

setValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter : "))
for i in range(1, rangeVal + 1):
    valAdd = input("Enter The String Or Value : ")
    setValue.add(valAdd)
print(setValue)
rmVal = int(input("How Many Items You Want To Remove From List : "))
setMembers = RemoveItems()
setMembers.toremove(setValue,rmVal)
