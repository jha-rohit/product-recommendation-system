import numpy as np
import matplotlib.pyplot as plt
dic = {}
myList = []
def makeGraph():
	counter = 0
	dic[3.0] = 10
	dic[6.0] = 3
	for i in range(0,10):

		if i in dic:
			dic[i] += 1
		else:
			dic[i] = 0
	
	lists = sorted(dic.items())
	x,y = zip(*lists)
	
	plt.plot(x,y)
	#plt.plot()
	plt.show()

makeGraph()
