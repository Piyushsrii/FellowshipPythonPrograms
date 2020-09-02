class EmptyVariable:
    def emptyVar(self):
        n = 20
        d = {"x":200}
        l = [1,3,5]
        t= (5,7,8)
        print("Before Emptying", n, d, l, t)
        print("After Emptying",type(n)(), type(d)(), type(l)(), type(t)())
        
varObj = EmptyVariable()
varObj.emptyVar()