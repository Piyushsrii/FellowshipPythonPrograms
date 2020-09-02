class LeadingZeroes:
    def zeroes(self,val):
        str1 = val
        str2 = val
        print("Original String: ",val)
        print("\nAdded trailing zeros :")
        str1 = str1.ljust(8,'0')
        print(str1)
        str1 = str1.ljust(10,'0')
        print(str1)

        print("\nAdded leading zeros:")
        str2 = str2.rjust(8,'0')
        print(str2)
        str2 = val.rjust(10,'0')
        print(str2)

val = input("Enter The Value : ")
values = LeadingZeroes()
values.zeroes(val)