import distance
import operator

def get_k_neighbours(dict,person,friends,k):
    all_neighbours=[]
    for other in dict:
        if other == person: continue
        #sim =  distance.distance_pearson(dict,person,other)
        sim =  distance.distance_euclid(dict,person,other)
        #sim = distance.cosine_similarity(dict, person, other)
        if sim <= 0: continue
        if friends[other] == 0:
            sim = sim/2

        all_neighbours.append((other,sim))

    all_neighbours.sort(key=operator.itemgetter(1))
    all_neighbours.reverse()
    k_neighbours =all_neighbours[:k]
    return k_neighbours

def getRecommendation(dict,neighbours,person):
    total_sum = {}
    sim_sum = {}
    for user,sim_score in neighbours:
        for item in dict[user]:
            if (item not in dict[person] or dict[person][item] == 0):
                total_sum.setdefault(item,0)
                total_sum[item] += (dict[user][item]*sim_score)
                sim_sum.setdefault(item,0)
                sim_sum[item]+=sim_score


    rankings = [(total/sim_sum[item],item) for item,total in total_sum.items()]

    rankings.sort()
    rankings.reverse()
    return rankings




