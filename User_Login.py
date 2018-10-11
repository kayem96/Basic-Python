class User:
	name = ""
	email = ""
	Password = ""
	login = False

	def logIn(self):
		email = input("Enter Your Email: ")
		Password = input("Enter Password: ")

		if email == self.email and Password == self.Password:
			login = True
			print("Login Succes!")

		else:
			print("Login faild! Please Try Again!")

	def LogOut(self):
		login = False
		print("Logged Out!")

	def isLoggedIn(self):
		if self.login:
			return True
		else:
			return False

	def profile(self):
		if isLoggedIn():
			print(self.name, "\n", self,Email)
		else:
			print("User is not logged in!")

user1 = User()

user1.name = "Shafiul Kayem"
user1.email = "shafiulkayem@gmail.com"
user1.Password = "12345678"

user1.logIn()


review = input("What's your feelling ? >>> ")
print("Thanks! :)")