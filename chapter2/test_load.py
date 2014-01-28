import csv

class User:
	def __init__(self):
		self.name = ""
		self.ratings = []

	def printRatings(self):
		print(self.name, self.ratings)

users = []

with open("BX-Dump/Movie_Ratings.csv", 'rb') as csvfile: 

	rating = {'film': 'rating'}
	f = csv.reader(csvfile, delimiter=',')
	for row in f:		
		if row[0]=='':
			for user in row:
				print(user)
				new_user = User()
				new_user.name = user
				users.append(new_user)
		else:
			i = 0
			for rating in row:
				if i > 0:
					rating = {row[0] : rating}
					users[i].ratings.append(rating)
				i=i+1
for user in users:
	user.printRatings()
