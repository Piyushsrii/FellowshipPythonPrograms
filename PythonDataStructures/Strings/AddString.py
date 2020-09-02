class Addstring:
    def stringAdd(self,strVal):
        length = len(strVal)
        if length > 2:
            if strVal[-3:] == 'ing':
                strVal += 'ly'
            else:
                strVal += 'ing'
        else:
            print("Enter More than 3 Characters")

        return strVal

stringData = Addstring()
strVal = input("Enter A String : ")
print("String Character Count is : ",stringData.stringAdd(strVal))