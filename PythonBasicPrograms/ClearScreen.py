import os
import time
class ClearScreen:
    def clear(self,timeClear):
        os.system("cls")
        time.sleep(timeClear)

timeClear = int(input("Enter The Time : "))
screen = ClearScreen()
screen.clear(timeClear)