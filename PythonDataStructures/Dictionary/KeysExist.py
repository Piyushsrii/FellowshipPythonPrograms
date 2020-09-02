class KeyExist:
    def exist(self,studentData,keyStr,valStr):
        print(studentData.keys() >= { keyStr[1], keyStr[0]})
        print(studentData.keys() >= {keyStr[1], valStr[0]})
        print(studentData.keys() >= {keyStr[1], keyStr[1]})

keyValue = KeyExist()
rangeVal = int(input("Enter The range of value you want to enter : "))
studentData = { }
keyStr = [ ]
valStr = [ ]
for i in range(1,rangeVal+1):
    key = input("Enter The Key : ")
    keyStr.append(key)
    val = input("Enter The value for dictionary : ")
    valStr.append(val)
    studentData.setdefault(key,val)

print ("Data : ".studentData, keyStr)
keyValue.exist(studentData,keyStr,valStr)
