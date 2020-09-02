class SpecStringPart:
    def chkSpecCharacter(self,strVal):
        print(strVal.rsplit('/', 1)[0])
        print(strVal.rsplit('-', 1)[0])

stringData = SpecStringPart()
strVal = input("Enter Words With , Separated Sequence : ")
stringData.chkSpecCharacter(strVal)

