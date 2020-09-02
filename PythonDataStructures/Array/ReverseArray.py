class ReverseArray:
    def reverse(self,arrOfNUm):
        print("Original array: " + str(arrOfNum))
        arrOfNum.reverse()
        print("Reverse array: " + str(arrOfNum))

arr = ReverseArray()
rangeVal = int(input("Enter The range of value you want to enter : "))
arrOfNum = []
for i in range(rangeVal):
    val = int(input("Enter The value for array : "))
    arrOfNum.append(val)
arr.reverse(arrOfNum)
