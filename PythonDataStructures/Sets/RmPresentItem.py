class RmPresentItem:
    def chkPresentToRem(self,setValue,rmVal):
        setValue.discard(rmVal)
        print(setValue)

setValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter : "))
for i in range(1, rangeVal + 1):
    valAdd = input("Enter The String Or Value : ")
    setValue.add(valAdd)
print("Data Set : ",setValue)
rmVal = input("Enter An Items You Want To Remove From List : ")
setMembers = RmPresentItem()
setMembers.chkPresentToRem(setValue,rmVal)







