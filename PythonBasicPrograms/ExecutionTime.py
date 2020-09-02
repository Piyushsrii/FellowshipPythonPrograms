import time
class ExecutionTime:
    def sumOfnumbers(self, sumNumber):
        startTime = time.time()
        sum = 0
        for i in range(sumNumber):
            sum = sum + i
        endTime = time.time()
        return sum,round (endTime - startTime,4)

sumNumber= int(input("Enter a number To sum : "))

sumObj = ExecutionTime()
sumObj.sumOfnumbers(sumNumber)
print("\nTime Took To Sum 1 to ",sumNumber,"is : ",sumObj.sumOfnumbers(sumNumber))
