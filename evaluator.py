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

