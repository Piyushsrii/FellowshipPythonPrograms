import sys
class SizeOfObject:
    def objectSize(self,str1, str2, str3):
        print("\nMemory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
        print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
        print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes\n")

str1 = input("Enter The First String : ")
str2 = input("Enter The Second String : ")
str3 = input("Enter The Third String : ")
obj = SizeOfObject()
obj.objectSize(str1, str2, str3)