#
#  FILTERINGDATA.py
#
#  Code file for the book Programmer's Guide to Data Mining
#  http://guidetodatamining.com
#  Ron Zacharski
#

from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0},
         "Clara": {"Blues Traveler": 4.75, "Norah Jones": 4.5, "Phoenix": 5.0, "The Strokes": 4.25, "Weird Al": 4.0},
         "Robert": {"Blues Traveler": 4.0, "Norah Jones": 3.0, "Phoenix": 5.0, "The Strokes": 2.0, "Weird Al": 1.0}		 
        }

#print("Veronica's ratings: ", users["Veronica"] )


def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRatings = False 
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1 #Indicates no ratings in common

# EXERCISE 1 - IMPLEMENT MINKOWSKI DISTANCE

def minkowski(rating1, rating2, r):
# Computes the Manhattan distance. 
#	Both rating1 and rating2 are dictionaries of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5} 
#	r is the Minkowski constant 
#		r = 1: 	Manhattan distance
#		r = 2:  Euclidean distance 
#		r = \infinity: Supremum distance

	distance = 0
	commonRatings = False 
	for key in rating1:
		if key in rating2:
			distance += (abs(rating1[key] - rating2[key]))**r
			commonRatings = True
	distance = distance**(1/r)
	if commonRatings:
		return distance
	else:
		return -1 #Indicates no ratings in common

# EXERCISE 3 - IMPLEMENT PEARSON

def pearson(user1, user2):
# Computes the Pearson Correlation Coefficient
#	Both user1 and user2 are dictionaries of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5} 
	
	x_sum = x2_sum = y_sum = y2_sum = xy_sum = n = 0
	for key in user1:
		if key in user2:
			x_sum += user1[key]
			x2_sum += user1[key]**2
			y_sum += user2[key]
			y2_sum += user2[key]**2
			xy_sum += user1[key]*user2[key]
			n += 1
	denominator = numerator = 0
	numerator = xy_sum - (x_sum*y_sum/n)
	denominator = sqrt(x2_sum - (x_sum**2) / n) * sqrt(y2_sum -(y_sum**2) / n) 
	if denominator == 0: 
		return 0
	else:
		return numerator / denominator

# EXERCISE WHATEVER - IMPLEMENT COSINE

def cosine(user1, user2):
# Computes Cosine Similarity
#	Both user1 and user2 are dictionaries of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5} 

	xy_dot = x2_sum = y2_sum = 0
	for key in user1:
		if key in user2:
			xy_dot += user1[key] * user2[key]
			x2_sum += user1[key]**2
			y2_sum += user2[key]**2
	denominator = sqrt(x2_sum) * sqrt(y2_sum)
	print(denominator)
	if denominator == 0:
		return 0
	else:
		return xy_dot / denominator

# EXERCISE 2 - IMPLEMENT MINKOWSKI DISTANCE in NearestNeighbor

def computeNearestNeighbor(username, users, cNN_r):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users:
        if user != username:
            distance = minkowski(users[user], users[username],cNN_r)
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances
	
#print( "Haily nearest neighbor", computeNearestNeighbor("Hailey", users, 1))

def recommend(username, users, recommend_r):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(username, users, recommend_r)[0][1]

    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

# examples - uncomment to run

# test Minkowski
#print( 'Hailey Manhattan: ', recommend('Hailey', users, 1))
#print( 'Hailey Euclidean: ',  recommend('Hailey', users, 2))

# test pearson

print( 'Angelica and Bill pearson: ',  pearson(users['Angelica'], users['Bill']))

# test cosine

print( 'Clara and Robert cosine: ',  cosine(users['Clara'], users['Robert']))
#print( recommend('Chan', users, 1))
