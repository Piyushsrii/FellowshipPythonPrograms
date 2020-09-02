class OccurenceOfString:
    def count(self,String, Character):
        print("Count Of Characters is : ",String.count(Character))

String = input("Enter a String : ")
Character = input("Enter The Character You Want To Count In a string : ")
Obj = OccurenceOfString()
Obj.count(String, Character)

