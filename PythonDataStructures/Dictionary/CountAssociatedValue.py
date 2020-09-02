class CountAssociatedValue:
    def toCount(self,keyValue):
        studentData = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
        print(sum(d[keyValue] for d in studentData))

dictKeyValues = CountAssociatedValue()
keyValue = input("Enter The Key You Want To Count : ")
dictKeyValues.toCount(keyValue)