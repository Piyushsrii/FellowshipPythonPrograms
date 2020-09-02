from datetime import date

class PrintMonthYear:
    def __init__(self,initialDay,finalDay):
        self.initialDay = initialDay
        self.finalDay = finalDay

    def displayDifference(self):
        diffInDays = self.finalDay - self.initialDay
        print("Difference in days : ", diffInDays.days)

initialDate = int(input("Enter The Initial Date : "))
finalDate = int(input("Enter The Final Date : "))
initialMonth = int(input("Enter The Initial Month : "))
finalMonth = int(input("Enter The Final Month : "))
year = int(input("Enter The Year : "))

firstDate = date(year, initialMonth, initialDate)
lastDate = date(year, finalMonth, finalDate)
print("Date Are : ",firstDate, " ", lastDate)
yearObj = PrintMonthYear(firstDate,lastDate)
yearObj.displayDifference()

