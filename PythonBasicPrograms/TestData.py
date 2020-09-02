class TestData:
    def checkGroupMember(self, groupData, n):
        for value in groupData:
            if n == value:
                return True
        return False

dataObj = TestData()
print(dataObj.checkGroupMember([1, 5, 8, 3], 3))
print(dataObj.checkGroupMember([1, 5, 8, 3], -1))
