# -*- coding: utf-8 -*-

import os
import re

print "Read evaluator.py"


def normProbs(prob, t):
    '''
    normalize the probabilities.
    rejects are [0.0, 0.5]
    verifications are [0.5, 1.0]
    unknowns are 0.5
    '''
    scoreMax = max(prob)*1.025
    prob = [x/2 if x <= 1.0-t else x for x in prob]
    prob = [((x-1)/(scoreMax-1))/2 + 0.5 if x >= 1.0+t else x for x in prob]
    prob = [0.5 if 1.0-t < x < 1.0+t else x for x in prob]
    prob = [0.0 if x < 0.0 else x for x in prob]

    prob = [round(x, 3) for x in prob]
    return prob


def writeNameAndScore(names, scores, aFolder, aName):
    sta = [sum([1 for x in scores if x > 0.5]), scores.count(0.5),
           sum([1 for x in scores if x < 0.5])]
    if not os.path.isdir(aFolder + "/"):
        os.mkdir(aFolder + "/")
    with open(aFolder + "/" + aName + ".txt", "w") as f:
        for anIndex in range(len(names)):
            s = "{} {:.3f}\n".format(names[anIndex], scores[anIndex])
            f.write(s)
    print "Scores written to file " + aName + ".txt"
    print "{} verifications, {} unknowns, {} rejects".format(*sta)


def getTruthAV(aFile):
    with open(aFile) as inFile:
        text = inFile.read().split("\n")
    if text[0][-1] == "\r":
        text = [x[:-1] for x in text]
    decision = [x[-1] for x in text if len(x)]
    decision = [1 if x == "Y" else 0 for x in decision]
    problem = [x[-7:-2] for x in text if len(x)]
    return {problem[i]: decision[i] for i in range(len(problem))}


def getAnswerAV(aFile):
    with open(aFile) as inFile:
        text = inFile.read()
    problem = re.findall(r'([A-Z]{2}\d{3}) ', text)
    decision = re.findall(r' ([01]\.\d{,3})', text)
    return {problem[i]: float(decision[i]) for i in range(len(problem))}


def calcC1(truthDict, answerDict):
    correct = 0.0
    incorrect = 0.0
    for e in truthDict:
        if truthDict[e] == 1:
            if answerDict[e] > 0.5:
                correct += 1
            elif answerDict[e] < 0.5:
                incorrect += 1
        if truthDict[e] == 0:
            if answerDict[e] < 0.5:
                correct += 1
            elif answerDict[e] > 0.5:
                incorrect += 1
    n = len(truthDict.keys())
    unknown = len([x for x in answerDict.values() if x == 0.5])
    return (1.0/n)*(correct+(unknown*correct/n))


def evalAV(truthPath, answerPath):
    truthDict = getTruthAV(truthPath)
    answerDict = getAnswerAV(answerPath)
    print "c@1:", round(calcC1(truthDict, answerDict), 4)
