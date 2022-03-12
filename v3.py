############################################################################################
# Libraries
############################################################################################
import math
import random
import matplotlib.pyplot as plt
import scipy
from numpy.random import choice
from scipy.io.wavfile import read as wavread
import copy
import numpy as np
############################################################################################



############################################################################################
# General info of algorithm
############################################################################################
# Number of primary population
NumberOfPrimaryPopulation = 500
# Number of Generations
NumberOfGenerations = 200
# Mutation Probability
MutationProbability = 0.1
# Length of each piece
LengthOfEachPiece = 20
# Length of result
LengthOfResult = 10
# Domain
Domain = 36
# Inputs
songs = [
    [2, 3, 5, 3, 2, 11, 2, 3, 5, 3, 2, 11, 10, 10, 10, 10, 0, 0, 0, 0],
    [10, 10, 10, 10, 8, 10, 8, 8, 0, 0, 0, 0, 6, 6, 5, 5, 6, 8, 10, 10],
    [6, 6, 5, 3, 2, 3, 5, 6, 0, 0, 0, 8, 8, 8, 6, 5, 3, 5, 6, 8],
    [10, 10, 10, 5, 6, 0, 8, 6, 5, 3, 5, 10, 6, 5, 3, 2, 3, 3, 3, 3],
    [8, 8, 5, 5, 3, 3, 10, 10, 0, 0, 0, 0, 5, 5, 3, 3, 1, 1, 8, 8],
    [3, 3, 1, 1, 11, 11, 6, 6, 0, 0, 0, 0, 8, 6, 8, 10, 1, 11, 10, 0],
    [7, 10, 3, 1, 11, 10, 11, 10, 11, 10, 8, 6, 5, 5, 5, 5, 5, 0, 0, 0]
]
############################################################################################



############################################################################################
# Primary Population
############################################################################################
# PrimaryPopulation = []
# for i in range(0, NumberOfPrimaryPopulation):
#     PrimaryPopulation.append([])
#     for j in range(0, LengthOfEachPiece):
#         PrimaryPopulation[i].append(random.randint(0, 12))
############################################################################################



############################################################################################
# Percent of similarity of two songs
############################################################################################
def SimilarityOfSongs(DataOfSong1, DataOfSong2):
    SimilarityScore = []
    for i in range(0, LengthOfEachPiece):
        res = abs(DataOfSong1[i]-DataOfSong2[i])
        SimilarityScore.append(1 - math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(res/Domain))))))
    return 100 * sum(SimilarityScore) / len(SimilarityScore)
############################################################################################



############################################################################################
# Fitness
############################################################################################
# def Fitness(Population):
#     Scores = []
#     res = []
#     for i in range(0, len(Population)):
#         res.append(SimilarityOfSongs(songs[0], Population[i]))
#         res.append(SimilarityOfSongs(songs[1], Population[i]))
#         res.append(SimilarityOfSongs(songs[2], Population[i]))
#         res.append(SimilarityOfSongs(songs[3], Population[i]))
#         res.append(SimilarityOfSongs(songs[4], Population[i]))
#         res.append(SimilarityOfSongs(songs[5], Population[i]))
#         res.append(SimilarityOfSongs(songs[6], Population[i]))
#         x1 = max(res)
#         index = res.index(x1)
#         res[index] = 0
#         x2 = max(res)
#         Scores.append((x1+x2)/2)
#         res.clear()
#     return Scores
############################################################################################
# def Fitness(Population):
#     Scores = []
#     res = 0
#     for i in range(0, len(Population)):
#         for j in range(0, len(songs)):
#             res = res + SimilarityOfSongs(songs[j], Population[i])
#         Scores.append(res/9)
#         res = 0
#     return Scores
############################################################################################
def Fitness(Population):
    Scores = []
    res = 0
    for i in range(0, len(Population)):
        k1 = random.randint(0, len(songs) - 1)
        k2 = random.randint(0, len(songs) - 1)
        while k2 == k1:
            k2 = random.randint(0, len(songs) - 1)
        res = res + SimilarityOfSongs(songs[k1], Population[i])
        res = res + SimilarityOfSongs(songs[k1], Population[i])
        Scores.append(res/2)
        res = 0
    return Scores
############################################################################################




############################################################################################
# Roulette wheel
############################################################################################
def RouletteWheel(Population):
    NewPopulation = []
    Scores = Fitness(Population)
    ScoreSum = sum(Scores)
    NormalizedScores = []
    for i in range(0, len(Population)):
        NormalizedScores.append(Scores[i]/ScoreSum)
    # res = 1 - sum(NormalizedScores)
    # index = len(NormalizedScores)-1
    # NormalizedScores[index] = NormalizedScores[index] + res
    q = list(range(0, len(Population)))
    for i in range(0, NumberOfPrimaryPopulation):
        # Best = Scores.index(max(Scores))
        # NewPopulation.append(Population[Best])
        # Scores[Best] = 0
        draw = choice(q, 1, p=NormalizedScores)
        NewPopulation.append(Population[draw[0]])
    # print(sum(Fitness(Population))/len(Fitness(Population)), sum(Fitness(NewPopulation))/len(Fitness(NewPopulation)))
    return NewPopulation
############################################################################################



############################################################################################
# Mutation
############################################################################################
def Mutation(Population):
    for i in range(0, NumberOfPrimaryPopulation):
        choose = random.uniform(0, 1)
        if choose <= MutationProbability:
            n = random.randint(0, LengthOfEachPiece-1)
            Population[i][n] = random.randint(0, 12)
    return Population
############################################################################################



############################################################################################
# Mating
############################################################################################
def OnePointCrossover(Population):
    i = 0
    NewPopulation = RouletteWheel(Population)
    result = []
    while i < NumberOfPrimaryPopulation:
        P1 = NewPopulation[i]
        P2 = NewPopulation[i + 1]
        BreakingPoint = random.randint(0, LengthOfEachPiece - 1)
        result.append(NewPopulation[i])
        result.append(NewPopulation[i + 1])
        p1 = []
        p2 = []
        for j in range(0, LengthOfEachPiece):
            if j <= BreakingPoint:
                p1.append(NewPopulation[i][j])
                p2.append(NewPopulation[i+1][j])
            else:
                p1.append(NewPopulation[i + 1][j])
                p2.append(NewPopulation[i][j])
        result.append(p1)
        result.append(p2)
        i = i + 2
    return result
############################################################################################



############################################################################################
# Test
############################################################################################
def ProduceMusicParts():
    FitnessAvrage = []
    FitnessMaximum = []
    IndexOfBest = 0
    print("##########################################################")
    print("Welcome")
    print("##########################################################")
    PrimaryPopulation = []
    for i in range(0, NumberOfPrimaryPopulation):
        PrimaryPopulation.append([])
        for j in range(0, LengthOfEachPiece):
            PrimaryPopulation[i].append(random.randint(0, 12))
    Population = copy.deepcopy(PrimaryPopulation)
    for i in range(0, NumberOfGenerations):
        print("Generation number", i+1)
        Population2 = OnePointCrossover(Population)
        Population3 = Mutation(Population2)
        Population4 = RouletteWheel(Population3)
        Population = copy.deepcopy(Population4)
        Scores = Fitness(Population)
        IndexOfBest = Scores.index(max(Scores))
        FitnessAvrage.append(sum(Scores)/len(Scores))
        FitnessMaximum.append(max(Scores))
    Scores = Fitness(Population)
    IndexOfBest = Scores.index(max(Scores))
    # print(Population[IndexOfBest])
    print(max(Scores))
    return Population[IndexOfBest]
############################################################################################



############################################################################################
# make all the music
############################################################################################
result = []
for i in range(0, LengthOfResult):
    n = ProduceMusicParts()
    result.append(n)
    # songs.append(n)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(i + 1)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(result)
############################################################################################



############################################################################################
# Plot
############################################################################################
# plt.plot(FitnessAvrage)
# plt.plot(FitnessMaximum)
# plt.show()
###########################################################################################
