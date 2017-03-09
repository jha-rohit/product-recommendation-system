
def loadDataset():

	path="" #/data/recommendation machine learning/aimotion/"
	print(path)

	books = {}
	for line in open(path+"BX-Books.csv", encoding="ISO-8859-1"):
		line = line.replace('"', "")
		(id,title) = line.split(";") [0:2]
		books[id] = title

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
		except ValueError:
			count+=1
		except KeyError:
			count +=1
	return prefs
