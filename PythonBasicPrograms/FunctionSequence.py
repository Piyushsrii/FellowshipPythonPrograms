class FunctionSequence:
    def maxminOfNum(self,data):
            maxNum = data[0]
            minNum = data[0]
            for num in data:
                if num > maxNum:
                    maxNum = num
                elif num < minNum:
                    minNum = num
            return maxNum, minNum

number = FunctionSequence()
valueRange = int(input("Enter The Range Of Value : "))
arrOfValue = []
for i in range(valueRange):
    num = int(input("Enter The Value : "))
    arrOfValue.append(num)
print(arrOfValue)
print(number.maxminOfNum(arrOfValue))
