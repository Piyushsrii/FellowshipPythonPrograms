class DisplayColor:
    def colorIndex(self):
        print("%s %s" % (color_list[0], color_list[-1]))

color_list = ["Red","Green","White" ,"Black"]
colorObj = DisplayColor()
colorObj.colorIndex()
