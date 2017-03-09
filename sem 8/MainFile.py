import readDataset
import divideDataset
import friendsIntegration
import getRecommendation
import evaluate

def main():
    dict = readDataset.loadDataset()
    trainData = {}
    testData ={}
    TheOne = '189835'
    divideDataset.divide(dict,0.7,trainData,testData)
    #for TheOne in trainData:
    friends = friendsIntegration.getFriends(trainData ,TheOne)
    k_neighbour = getRecommendation.get_k_neighbours(trainData,TheOne,friends,100)
    results = getRecommendation.getRecommendation(trainData,k_neighbour,TheOne)
    for rating,item in results:
        if(item in testData[TheOne]):
            print(item,rating)
            print(testData[TheOne][item])
    evaluate.getPrecision(results, k_neighbour, friends, TheOne, testData)
    evaluate.getRecall(results, k_neighbour, friends, TheOne, testData)
main()


# top 11676
# second 98391
# third 189835

# random dude (254, 57)
# random dude 225002

