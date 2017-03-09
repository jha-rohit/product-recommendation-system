import math

def cosine_similarity(dict, person1, person2):
	# sigma(a*b) / sqrt(sigma(a*a)) * sqrt(sigma(b*b))
	sumAB = 0.0
	sumAA = 0.0
	sumBB = 0.0
	for item in dict[person1]:
		if item in dict[person2]:
			sumAB += dict[person1][item] * dict[person2][item]
			sumAA += dict[person1][item] * dict[person1][item]
			sumBB += dict[person2][item] * dict[person2][item]
	try:
		#ret = ret
		return sumAB / (math.sqrt(sumAA) * math.sqrt(sumBB))
	except ZeroDivisionError:
		return -1
		print("zero division")
	

def distance_euclid(dict, person1, person2):
    sum = 0
    for item in dict[person1]:
        if item in dict[person2]:
            sum += pow(dict[person1][item] - dict[person2][item] , 2)

    if sum == 0:
        return 0          #no match for movies found so return 0.

    return 1/(1 + math.sqrt(sum))    #lesser distance more euclid value normalised form 0 to 1

def distance_pearson(dict, person1, person2):
    sum1 = 0
    sum2 = 0
    N = 0
    if person1 not in dict : return 0
    if person2 not in dict : return 0
    for item in dict[person1]:
        if item in dict[person2]:
            N += 1
    if N == 0:
        return 0

    for item in dict[person1]:
        if item in dict[person2]:
            sum1 += dict[person1][item]
            sum2 += dict[person2][item]

    sum1_sq = 0
    sum2_sq = 0

    for item in dict[person1]:
        if item in dict[person2]:
            sum1_sq += pow(dict[person1][item],2)
            sum2_sq += pow(dict[person2][item],2)

    sum_product = 0
    for item in dict[person1]:
        if item in dict[person2]:
            sum_product = sum_product + (dict[person1][item] * dict[person2][item])

    num = sum_product - (sum1*sum2/N)
    den = math.sqrt((sum1_sq - pow(sum1,2)/N)*(sum2_sq - pow(sum2,2)/N))

    if den == 0:
        return 0

    return num/den

