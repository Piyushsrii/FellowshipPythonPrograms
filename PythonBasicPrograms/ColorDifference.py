class ColorSet:
    def colorDiff(self,colorList1,colorList2):
        print(colorList1.difference(colorList2))

colorList1 = set(["White", "Black", "Red"])
colorList2 = set(["Red", "Green"])
colorObj = ColorSet()
colorObj.colorDiff(colorList1,colorList2)

