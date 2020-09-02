class CharFrequency:
    def chkCount(self,strVal):
        dictCharCount = { }
        for n in strVal:
            keys = dictCharCount.keys()
            if n in keys:
                dictCharCount[n] += 1
            else:
                dictCharCount[n] = 1
        return dictCharCount

stringData = CharFrequency()
strVal = input("Enter A String : ")
print("String Character Count is : ",stringData.chkCount(strVal))