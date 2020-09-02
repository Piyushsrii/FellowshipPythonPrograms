class Reversename:
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName

	def reverseName(self):
		print ("Hello  " + lastName + " " + firstName)

firstName = input("Input your First Name : ")
lastName = input("Input your Last Name : ")

nameObj = Reversename(firstName, lastName)
nameObj.reverseName()