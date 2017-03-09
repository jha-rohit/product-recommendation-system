import distance

def topMatches(dict,person,best):
    for other in dict:
        if other != person:
            scores = [(distance.distance_pearson(),person,other),other]  #usign Pearson Distance

    scores.sort()
    scores.reverse()
    print(scores)
    return scores[0:best]

