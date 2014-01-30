# 
# Kyle DeRosa
# 30 Jan, 2014
# chapter 2 - guide to Data Mining end of chapter projects
#
# 1) extend recommender class to provie manhattan and euclidean distances for NN method
# 2) import Movie_Ratings data and format into dictionaries that be utilized by the recommender class
#


import csv
from recommender import recommender

class User:
	def __init__(self):
		self.name = ""
		self.ratings = {}

	def printRatings(self):
		print(self.name, self.ratings)

users = []

#open file and create list of User classes
# users = []; a list of User classes, containing the name (string) and movie ratings (dictionary {'movie name': 0-5}

with open("/Users/kylederosa/Github/guideToDataMiningData/Movie_Ratings.csv", 'rb') as csvfile: 

	rating = {'film': 'rating'}
	movie = []
	f = csv.reader(csvfile, delimiter=',')
	for row in f:		
		if row[0]=='':
			for user in row:
				print(user)
				new_user = User()
				new_user.name = user
				users.append(new_user)
		else:
			movie.append(row[0])
			i = 0
			for rating in row:
				if i > 0:
					if rating != '':
						users[i].ratings[row[0]] = float(rating)
				i=i+1
# convert list of User objects to dictionary of user ratings - {'name' : {'movie' : 0-5, 'movie2' : 0-5 ... 'movie_n' : 0-5}}

userDict = {}

for user in users:
	userDict[user.name] = user.ratings

#
r = recommender(userDict)

#print('movie list', movie)

#use movie list to populate recommender.productid2name dictionary - {'film name' : 'film name'}
for film in movie:
	r.productid2name[film] = film

#use user User list to populate recommender.username2id and recommender.userid2name = {'name' : 'name'}
for user in users:
	r.username2id[user.name] = user.name
	r.userid2name[user.name] = user.name
#print(r.productid2name)

#here, for recommender.recommend and recommend.userRatings to function,
# userID and productId lists need to be constructed if they are to utilize the 
# recommender class without changing it. Consider creating new datasets, or (more likely)
# use the existing Movie_list.csv to create userIDs and ProductIDs

# assuming that: ProductIDs should handle recommender.recommend - COMPLETE
# and UserIDs should handle recomender.userRatings - COMPLETE

r.userRatings('Matt', 5)
print("Matt: pearson: ", r.recommend('Matt', 'pearson'))
