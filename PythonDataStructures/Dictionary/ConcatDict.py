class ConcatDictionary:
    def concat(self, dictOfNum1,dictOfNum2,dictOfNum3):
        print("First Dictionary : ",dictOfNum1,"\nSecond Dictionary : ",dictOfNum2,"\nThird Dictionary : ",dictOfNum3)
        dictOfNum4 = { }
        for d in (dictOfNum1, dictOfNum2, dictOfNum3): dictOfNum4.update(d)
        print(dictOfNum4)

dictionary = ConcatDictionary()
dictOfNum1 = { }
dictOfNum2 = { }
dictOfNum3 = { }
for i in range(1,4):
    val1 = int(input("Enter The value for first dictionary: "))
    dictOfNum1.setdefault(i, val1)

for i in range(4,7):
    val2 = int(input("Enter The value for second dictionary: "))
    dictOfNum2.setdefault(i, val2)

for i in range(7,10):
    val3 = int(input("Enter The value for third dictionary : "))
    dictOfNum3.setdefault(i, val3)

dictionary.concat(dictOfNum1,dictOfNum2,dictOfNum3)

