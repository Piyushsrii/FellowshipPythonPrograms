class StringLength:
    def chkLength(self,strVal):
        charCount = 0
        for x in strVal:
            charCount += 1
        return charCount

stringData = StringLength()
strVal = input("Enter A String : ")
print("String Character Count is : ",stringData.chkLength(strVal))