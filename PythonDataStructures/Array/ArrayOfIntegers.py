class ArrayOfIntegers:
    def index(self,arrayNum,indexValue):
        print(arrOfNum)
        print("Access first three items individually")
        print("Searched Index Element : ",arrayNum[indexValue])
        print("Last Element : ", arrayNum[-1])
        print("First Element :", arrayNum[1])

arr = ArrayOfIntegers()
arrOfNum = []
for i in range(5):
    val = int(input("Enter The value for array : "))
    arrOfNum.append(val)

indexValue = int(input("Enter The Index Value You Want To Find : "))
arr.index(arrOfNum,indexValue)
