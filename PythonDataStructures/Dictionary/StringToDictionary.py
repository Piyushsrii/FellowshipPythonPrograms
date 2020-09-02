class StringToDictionary:
    def toDictionary(self,strValue):
        dict = { }
        for char in strValue:
            dict[char] = dict.get(char, 0) + 1
        print(dict)

string = StringToDictionary()
strValue = input("Enter The String To Convert Into Dictionary : ")
string.toDictionary(strValue)
