class ExtractSingleKey:
    def getSingleKey(self):
        d = {'Red': 'Green'}
        (c1, c2,), = d.items()
        print(c1 ,c2)

extract = ExtractSingleKey()
extract.getSingleKey()
