# -*- coding: utf-8 -*-

import re

from collections import defaultdict

print "Read Spatium.py"


def featureSelection(sampleWList, wLen):
    ky, val = sampleWList.keys(), sampleWList.values()
    val, ky = zip(*sorted(zip(val, ky), reverse=True))
    aWordList = [ky[i] for i in range(min(wLen, len(ky))) if val[i] > val[-1]]
    return aWordList


def mergeToProfile(wLists):
    newWLists = []
    for aProfile in wLists:
        authorProfile = defaultdict(int)
        for aDoc in aProfile:
            for key in aDoc.keys():
                authorProfile[key] += aDoc[key]
        newWLists.append(authorProfile)
    return newWLists


def convertToRelFreq(wLists):
    newWLists = []
    for aProfile in wLists:
        authorProfile = defaultdict(float)
        scaling = sum(aProfile.values()) / 1000.0
        for key in aProfile.keys():
            authorProfile[key] = aProfile[key]/scaling
        newWLists.append(authorProfile)
    return newWLists


def freqByList(wLists, aWordList):
    newWLists = []
    for aProfile in wLists:
        newWLists.append([aProfile[key] for key in aWordList])
    return newWLists


def l1Distance(profiles, sampleWList, aWordList):
    relProfiles = convertToRelFreq(profiles)
    relSamples = convertToRelFreq([sampleWList])

    profileFreq = freqByList(relProfiles, aWordList)
    aSample = freqByList(relSamples, aWordList)[0]

    differences = []
    for aProfile in profileFreq:
        diff = [abs(aSample[i] - aFreq) for i, aFreq in enumerate(aProfile)]
        differences.append(sum(diff))
    return differences
