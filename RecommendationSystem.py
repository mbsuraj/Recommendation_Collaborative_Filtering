import math
from operator import itemgetter

# definie class similarity
class similarity:
    
    # Class instantiation 
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Minkowski Distance between two vectors
    def minkowski(self, r):
    
        # calcualte minkowski distance
        distance = 0       
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            p = self.ratings1[k]
            q = self.ratings2[k]
            distance += pow(abs(p - q), r)
    
        # return value of minkowski distance
        return pow(distance,1/r)

    # Pearson Correlation between two vectors
    def pearson(self):
        ratings1_keys = self.ratings1.keys()
        ratings2_keys = self.ratings2.keys()
        common_keys = ratings1_keys & ratings2_keys
        n = len(common_keys)
        if n==0:
               return -2
 
        sumP = 0
        sumQ = 0
        sumPQ = 0
        sumPsq = 0
        sumQsq = 0
        for common_rating in common_keys:
               sumP = sumP + self.ratings1[common_rating]
               sumQ = sumQ + self.ratings2[common_rating]
               sumPQ = sumPQ + self.ratings1[common_rating]*self.ratings2[common_rating]
               sumPsq = sumPsq + self.ratings1[common_rating]*self.ratings1[common_rating]
               sumQsq = sumQsq + self.ratings2[common_rating]*self.ratings2[common_rating]
               

        # calcualte the numerator term for pearson correlation
        # using relevant partial sums
        numerator = sumPQ - sumP*sumQ/n
        

        # calcualte the denominator term for pearson correlation
        # using relevant partial sums
        denominator = math.sqrt(sumPsq - pow(sumP, 2)/n) * math.sqrt(sumQsq - pow(sumQ, 2)/n)
        
        # error check for denominator==0 condition
        # return -2 if denominator==0
        if denominator == 0:
               return -2

        # calcualte the pearson correlation 
        # using the numerator and deonomminator
        # and return the pearson correlation
        pearson_corr = round(numerator/denominator, 2)
        
        return pearson_corr

# user ratings - this is the same data as we used in the User Recommendation Lecture
songData = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

# for whom are we making recommendations?
userX = "Veronica"
userXRatings = songData[userX]

# find the similarity measure (pearson correlation) between userX's ratings, and each of the other user's ratings.

similarity_list = []
for userY, userYRatings in songData.items():
       if userY != userX:
              similarity_measure = similarity(userXRatings, userYRatings).pearson()
              similarity_list.append((userY, similarity_measure))
print("User similarities with ", userX)
print(similarity_list)
print()
            
# sort the list of tuples by highest simialrity to lowest similarity.
# assign the sorted list to a variable called sortedUserSimilarities.
sortedUserSimilarities = sorted(similarity_list, key = itemgetter(1), reverse = True)
print("Users similar to ", userX, " in the decreasing order of their similarities")
print(sortedUserSimilarities)
print()

# userX's NN is the user at the 0th position of the sorted list.
# assign the NN to a variable called userXNN.
# Example of how userXNN might look: 'Jordyn'
userXNN = sortedUserSimilarities[0][0]
print("User with highest similarity: ", userXNN)
print()

# recos for userX should include albums rated by userXNN, not already rated by userX.
# assign the list of (album, rating) tuples to a variable called userXRecos.
userXRecos = []
userXNN_Ratings = songData[userXNN]
for movie, ratings in userXNN_Ratings.items():
       if movie in userXRatings.keys():
              continue
       else:
              userXRecos.append((movie, ratings))

# sort list of tuples by highest rating to lowest rating.
# assign sorted list to a varaible userXSortedRecos.
userXSortedRecos = sorted(userXRecos, key = itemgetter(1), reverse = True)

print ("Recommendations for", userX)
print ("--------------------------")
print ()
print (userXSortedRecos)