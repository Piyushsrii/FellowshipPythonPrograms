class ReverseString:
    def toReverse(self,strVal):
        revStr = ''
        index = len(strVal)
        while index > 0:
            revStr += strVal[index - 1]
            index = index - 1
        return revStr

stringData = ReverseString()
strVal = input("Enter a String To Reverse : ")
print("Reverse String : ",stringData.toReverse(strVal))

