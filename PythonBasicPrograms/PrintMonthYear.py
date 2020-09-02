import calendar

class PrintMonthYear:
    def __init__(self,year,month):
        self.year = year
        self.month = month

    def displayMonthYear(self):
        print(calendar.month(self.year, self.month))

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))

yearObj = PrintMonthYear(year,month)
yearObj.displayMonthYear()
