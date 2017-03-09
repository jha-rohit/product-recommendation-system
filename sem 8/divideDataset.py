import random

def divide(dict , ratio, trainData={}, testData={}):
    for key,value in dict.items():
        #print(key,value)
        trainVec = {}
        testVec = {}
        for book,rating in value.items():
            if(random.random() <= ratio):
                trainVec[book] = rating
            else:
                testVec[book] = rating
        trainData[key] = trainVec
        testData[key] = testVec