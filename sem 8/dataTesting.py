import operator
i = 0;

path=""

#for line in open(path+"BX-Book-Ratings.csv", encoding="ISO-8859-1"):
#	(user,bookid,rating) = line.split(";")
	#print(reviewerID , productID, productRating, reviewTime)
#	i+=1
	#if i == 1000000 :
	#	break
	
#print(i)

def loadDataset():

	path="" #/data/recommendation machine learning/aimotion/"
	print(path)

	books = {}
	rev_books = {}
	booksPerUser = {}
	
	for line in open(path+"BX-Books.csv", encoding="ISO-8859-1"): #):#
		line = line.replace('"', "")
		(id,title) = line.split(";") [0:2]
		books[id] = title
		rev_books[title] = id

	#Load the data
	prefs = {}
	count = 0
	for line in open(path+"BX-Book-Ratings.csv", encoding="ISO-8859-1"):
		line = line.replace('"', "")
		line = line.replace("\\","")
		(user,bookid,rating) = line.split(";")
		try:
			if float(rating) > 0.0:
				prefs.setdefault(user,{})
				prefs[user][books[bookid]] = float(rating)
				
				booksPerUser.setdefault(user, 0)
				if booksPerUser[user] >= 0:
					booksPerUser[user] += 1
				else:
					booksPerUser[user] = 0
					
		except ValueError:
			count+=1
		except KeyError:
			count +=1

	
	ans = sorted(booksPerUser.items(), key = operator.itemgetter(1))
	print(ans)
	
	return prefs,rev_books

loadDataset()

def bottom30():
	i = 0
	reviewsCount = 0
	for line in open(path+"BX-Book-Ratings.csv", encoding="ISO-8859-1"):
		if i > 804846:
			line = line.replace('"', "")
			(user,bookid,rating) = line.split(";")
			print(line)

		i+=1
	return reviewsCount

#print(bottom30())


#	1149781
#	70 % = 804846
#	30 % = 344934
