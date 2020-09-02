class Histogram:
    def histogram(self,arrOfIntegrs):
        for n in arrOfIntegrs:
            pattern = ''
            noOfTimes = n
            while( noOfTimes > 0 ):
              pattern += '*'
              noOfTimes = noOfTimes - 1
            print(pattern)

arrOfIntegers = []
rangeOfValue = int(input("Enter The Range Of Values You Want To Enter : "))
for i in range(rangeOfValue):
    value = int(input("Enter The Value : "))
    arrOfIntegers.append(value)
    listValue = value.

histObj = Histogram()
histObj.histogram(arrOfIntegers)