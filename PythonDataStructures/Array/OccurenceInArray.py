class OccurenceInArray:
    def countOccurence(self,arrOfNUm,value):
        print("Original array: " + str(arrOfNum))
        print("Number of occurrences of the number ",value," in array: " + str(arrOfNUm.count(value)))

arr = OccurenceInArray()
rangeVal = int(input("Enter The range of value you want to enter : "))
arrOfNum = []
for i in range(rangeVal):
    val = int(input("Enter The value for array : "))
    arrOfNum.append(val)
Value = int(input("Enter The Value You Want To Find Ocuurence of : "))
arr.countOccurence(arrOfNum,Value)

