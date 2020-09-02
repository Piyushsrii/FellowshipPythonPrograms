class CharacterLowerCase:
    def toLowecase(self,strVal,position):
        print("Updated String : ",strVal[:position].lower() + strVal[position:])

stringData = CharacterLowerCase()
strVal = input("Enter a string : ")
position = int(input("Enter position number to which you want the character to lowercase :"))
stringData.toLowecase(strVal,position)

