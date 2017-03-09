from collections import defaultdict
import matplotlib.pyplot as plt

def getPrecision(results, k_neighbour, friends, theChosenOne, testData):
	totalItems = 0
	ans = 0
	ratingsDiff = {}
	#ratingsDiff = defaultdict(lambda:0, ratingsDiff)
	for rating, item in results:
		if(item in testData[theChosenOne]):
			predictedRating = rating
			actualRating = testData[theChosenOne][item]
			ans += abs(predictedRating - actualRating)
			
			
			#ratingsDiff.setdefault(abs(actualRating - predictedRating),0)
			try:
				if abs(actualRating - predictedRating) in ratingsDiff:
					ratingsDiff[abs(actualRating - predictedRating)] += 1
				else:
					ratingsDiff[abs(actualRating - predictedRating)] = 0
			except TypeError:
				print("Typo")
			
			lists = sorted(ratingsDiff.items())
			x,y = zip(*lists)
	
			plt.plot(x,y)
			
			totalItems += 1
	print("--------------precision aa gaya re bhai")
	print(ans)
	print(totalItems)
	print(1 - (ans / (totalItems * 10) ))
	plt.show()
	print(ratingsDiff)
	return ans
	
def getRecall(results, k_neighbour, friends, theChosenOne, testData):
	totalItems = 0
	ans = 0
	for rating, item in results:
		if(item in testData[theChosenOne]):
			ans += 1
	print("--------------recall aa gaya re bhai")
	print(ans)
	totalItems = len(testData[theChosenOne])
	print(totalItems)
	print(ans/totalItems)
	return ans/totalItems
