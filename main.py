#############################################################################
# Libraries
#############################################################################
import random
import scipy
from numpy.random import choice
from scipy.io.wavfile import read as wavread
import time
import numpy as np
import math
#############################################################################



#############################################################################
# General info of algorithm
#############################################################################
# Number of primary population
NumberOfPrimaryPopulation = 10
# Number of Generations
NumberOfGenerations = 100
# Mutation Probability
MutationProbability = 0.1
# Sample rate
SampleRate = 44100
# Length of the song in seconds
SongLength = 5.94
# Song 1 Name
SongName1 = 'upanddown1.wav'
# Song 2 Name
SongName2 = 'upanddown2.wav'
# Song 3 Name
SongName3 = 'upanddown3.wav'
# Song 4 Name
SongName4 = 'upanddown4.wav'
# Song 5 Name
SongName5 = 'upanddown5.wav'
# Song 6 Name
SongName6 = 'despair2.wav'
# Song 7 Name
SongName7 = 'despair3.wav'
# Domain
Domain = 32768 + 32767
#############################################################################



#############################################################################
# Song Decoder
#############################################################################
def SongDecoder(SongName):
    DataOfSong = []
    [_, y] = wavread(SongName)
    for i in range(0, int(SongLength*SampleRate)):
        y1, y2 = [y[i][0], y[i][1]]
        res = int((y1 + y2) / 2)
        DataOfSong.append(res)
    return DataOfSong
#############################################################################



#############################################################################
# Data of Songs
#############################################################################
SongData1 = SongDecoder(SongName1)
SongData2 = SongDecoder(SongName2)
SongData3 = SongDecoder(SongName3)
SongData4 = SongDecoder(SongName4)
SongData5 = SongDecoder(SongName5)
SongData6 = SongDecoder(SongName6)
SongData7 = SongDecoder(SongName7)
#############################################################################



#############################################################################
# Find the  local minimum and maximum
#############################################################################
domainOfAllSongs = []
domainOfAllSongs.append(min(SongData1))
domainOfAllSongs.append(max(SongData1))
domainOfAllSongs.append(min(SongData2))
domainOfAllSongs.append(max(SongData2))
domainOfAllSongs.append(min(SongData3))
domainOfAllSongs.append(max(SongData3))
domainOfAllSongs.append(min(SongData4))
domainOfAllSongs.append(max(SongData4))
domainOfAllSongs.append(min(SongData5))
domainOfAllSongs.append(max(SongData5))
domainOfAllSongs.append(min(SongData6))
domainOfAllSongs.append(max(SongData6))
domainOfAllSongs.append(min(SongData7))
domainOfAllSongs.append(max(SongData7))
MinOfDomain = min(domainOfAllSongs)
MaxOfDomain = max(domainOfAllSongs)
Domain = MaxOfDomain - MinOfDomain
print(MinOfDomain, MaxOfDomain, Domain)
#############################################################################



#############################################################################
# Random Primary Population
#############################################################################
print("-----------------------------------------")
print("Primary Population")
print("-----------------------------------------")
PrimaryPopulation = []
for i in range(0, NumberOfPrimaryPopulation):
    PrimaryPopulation.append([])
    print(i)
    for _ in range(0, int(SongLength*SampleRate)):
        PrimaryPopulation[i].append(random.randint(MinOfDomain, MaxOfDomain))
#############################################################################



#############################################################################
# Percent of similarity of two songs
#############################################################################
def SimilarityOfSongs(DataOfSong1, DataOfSong2):
    SimilarityScore = []
    # 1-(DataOfSong1[i][0] - DataOfSong2[i][0])/Domain
    for i in range(0, int(SongLength*SampleRate)):
        res = abs(DataOfSong1[i] - DataOfSong2[i])
        SimilarityScore.append(1 - res / Domain)
    return sum(SimilarityScore)/len(SimilarityScore)
#############################################################################



#############################################################################
# Fitness function
#############################################################################
def Fitness(Population):
    print("-----------------------------------------")
    print("Fitness Function")
    print("-----------------------------------------")
    Scores = []
    res = 0
    for i in range(0, NumberOfPrimaryPopulation):
        res = res + SimilarityOfSongs(SongData1, Population[i])
        res = res + SimilarityOfSongs(SongData2, Population[i])
        res = res + SimilarityOfSongs(SongData3, Population[i])
        res = res + SimilarityOfSongs(SongData4, Population[i])
        res = res + SimilarityOfSongs(SongData5, Population[i])
        res = res + SimilarityOfSongs(SongData6, Population[i])
        res = res + SimilarityOfSongs(SongData7, Population[i])
        Scores.append(res/7)
        res = 0
    return Scores
#############################################################################



#############################################################################
# Roulette wheel
#############################################################################
def RouletteWheel(Population):
    print("-----------------------------------------")
    print("Roulette Wheel Mutation")
    print("-----------------------------------------")
    NewPopulation = []
    Scores = Fitness(Population)
    ScoreSum = sum(Scores)
    NormalizedScores = []
    for i in range(0, NumberOfPrimaryPopulation):
        NormalizedScores.append(Scores[i]/ScoreSum)
    res = 1 - sum(NormalizedScores)
    index = len(NormalizedScores)-1
    NormalizedScores[index] = NormalizedScores[index] + res
    q = list(range(0, len(PrimaryPopulation)))
    for i in range(0, NumberOfPrimaryPopulation):
        draw = choice(q, 1, p=NormalizedScores)
        NewPopulation.append(Population[draw[0]])
    return NewPopulation
#############################################################################



#############################################################################
# Mutation
#############################################################################
def Mutation():
    pass
#############################################################################



#############################################################################
# Crossover
#############################################################################
def Crossover():
    pass
#############################################################################



#############################################################################
# Test
#############################################################################
print(SimilarityOfSongs(SongData1, SongData2))
print(RouletteWheel(PrimaryPopulation))
#############################################################################

# heuristic to see the similarity of learning data and choose base on that to give songs value with fuzzy logic
# find max and min of learning songs and learn and generat primary population based on that.
