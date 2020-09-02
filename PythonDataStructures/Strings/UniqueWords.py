class UniqueWords:
    def findUnique(self,strVal):
        words = [word for word in strVal.split(",")]
        print("The Sorted And Unique Order : ",",".join(sorted(list(set(words)))))

stringData = UniqueWords()
strVal = input("Enter Words With , Separated Sequence : ")
stringData.findUnique(strVal)

