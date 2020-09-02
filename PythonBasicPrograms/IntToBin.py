class IntToBin:
    def convertToBin(self, value):
        print(format(value, '08b'))
        print(format(value, '010b'))

value = int(input("Enter The Value : "))
int = IntToBin()
int.convertToBin(value)
