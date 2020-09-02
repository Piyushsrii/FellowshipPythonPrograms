class RemoveKey:
    def remove(self, dictOfNum, keyValue):
        if keyValue in dictOfNum:
            del dictOfNum[keyValue]
        print("Updated Dictionary : ",dictOfNum)

dictkey = RemoveKey()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = {}
for i in range(1,rangeVal+1):
    key = input("Enter The Key : ")
    val = input("Enter The value for dictionary : ")
    dictOfNum.setdefault(key, val)

print("Dictionary : ", dictOfNum)
keyValue = input("Enter The Key You Want To Delete : ")
dictkey.remove(dictOfNum, keyValue)
