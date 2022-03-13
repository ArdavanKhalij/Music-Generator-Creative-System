############################################################################################
# Libraries
############################################################################################
import math
import random
import matplotlib.pyplot as plt
from numpy.random import choice
import copy
############################################################################################



############################################################################################
# General info of algorithm
############################################################################################
# Number of primary population
NumberOfPrimaryPopulation = 500
# Number of Generations
NumberOfGenerations = 300
# Mutation Probability
MutationProbability = 0.1
# Length of each piece
LengthOfEachPiece = 20
# Length of result
LengthOfResult = 10
# Domain
Domain = 36
############################################################################################



############################################################################################
# Chords Distances
############################################################################################
ChordsDistances = [
    # ['Major', ['x', 4, 3, 'empty', 'empty']],
    # ['Minor', ['x', 3, 4, 'empty', 'empty']],
    # ['Augmented', ['x', 4, 4, 'empty', 'empty']],
    # ['Diminished', ['x', 3, 3, 'empty', 'empty']],
    # ['Major_7', ['x', 4, 3, 4, 'empty']],
    # ['Minor_7', ['x', 3, 4, 3, 'empty']],
    # ['Dominant_7', ['x', 4, 3, 3, 'empty']],
    # ['Diminished_7', ['x', 3, 3, 3, 'empty']],
    # ['Augmented_Major', ['x', 4, 4, 3, 'empty']],
    # ['Minor_Major_7', ['x', 3, 4, 4, 'empty']],
    # ['Half_Diminished_7', ['x', 3, 3, 4, 'empty']],
    # ['Major_6', ['x', 4, 3, 2, 'empty']],
    # ['Minor_6', ['x', 3, 4, 2, 'empty']],
    # ['Major_9', ['x', 4, 3, 4, 3]],
    # ['Minor_9', ['x', 3, 4, 3, 4]],
    ['Dominant_9', ['x', 4, 3, 3, 4]],
    # ['Sus_2', ['x', 2, 5, 'empty', 'empty']],
    # ['Sus_4', ['x', 5, 2, 'empty', 'empty']]
]
############################################################################################



############################################################################################
# Suitable distances
############################################################################################
def SuitableDistances(Song):
    i = 0
    Score = 0
    while i < len(Song) - 2:
        if Song[i] != 0 or Song[i + 1] != 0:
            if abs(Song[i]-Song[i + 1]) == 0:
                Score = Score + 1
            elif abs(Song[i]-Song[i + 1]) == 1:
                if Song[i] == 2 or Song[i] == 4 or Song[i] == 7 or Song[i] == 9 or Song[i] == 11 or Song[i + 1] == 2 or Song[i + 1] == 4 or Song[i + 1] == 7 or Song[i + 1] == 9 or Song[i + 1] == 11:
                    Score = Score + 1.5
                else:
                    Score = Score + 2.5
            else:
                pass
        i = i + 1
    i = 0
    while i < len(Song) - 4:
        if Song[i] != 0 or Song[i + 1] != 0 or Song[i + 2] != 0:
            if Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                Score = Score + 4
            elif Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                Score = Score + 4
            elif Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 3:
                Score = Score + 4
            elif Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i +1] == 3:
                Score = Score + 4
            elif Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 4:
                Score = Score + 4
            elif Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 4:
                Score = Score + 4
            elif Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 3:
                Score = Score + 4
            elif Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i +1] == 3:
                Score = Score + 4
            elif Song[i + 2] - Song[i + 1] == 2 and Song[i + 1] - Song[i] == 5:
                Score = Score + 4
            elif Song[i + 1] - Song[i + 2] == 2 and Song[i] - Song[i + 1] == 5:
                Score = Score + 4
            elif Song[i + 2] - Song[i + 1] == 5 and Song[i + 1] - Song[i] == 2:
                Score = Score + 4
            elif Song[i + 1] - Song[i + 2] == 5 and Song[i] - Song[i +1] == 2:
                Score = Score + 4
            else:
                pass
        i = i + 1
    i = 0
    while i < len(Song) - 5:
        if Song[i] != 0 or Song[i + 1] != 0 or Song[i + 2] != 0 or Song[i + 3] != 0:
            if Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                Score = Score + 4.5
            elif Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                Score = Score + 4.5
            elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 3:
                Score = Score + 4.5
            elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 3:
                Score = Score + 4.5
            elif Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 3:
                Score = Score + 4.5
            elif Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 3:
                Score = Score + 4.5
            elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 3:
                Score = Score + 4.5
            elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 3:
                Score = Score + 4.5
            elif Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 3:
                Score = Score + 4.5
            elif Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 3:
                Score = Score + 4.5
            elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 4:
                Score = Score + 4.5
            elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 4:
                Score = Score + 4.5
            elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                Score = Score + 4.5
            elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                Score = Score + 4.5
            elif Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 2:
                Score = Score + 4.5
            elif Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 2:
                Score = Score + 4.5
            elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 2:
                Score = Score + 4.5
            elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 2:
                Score = Score + 4.5
            else:
                pass
        i = i + 1
    i = 0
    while i < len(Song) - 6:
        if Song[i] != 0 or Song[i + 1] != 0 or Song[i + 2] != 0 or Song[i + 3] != 0 or Song[i + 4] != 0:
            if Song[i + 4] - Song[i + 3] == 4 and Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 3:
                Score = Score + 5
            elif Song[i + 3] - Song[i + 4] == 4 and Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 3:
                Score = Score + 5
            elif Song[i + 4] - Song[i + 3] == 3 and Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                Score = Score + 5
            elif Song[i + 3] - Song[i + 4] == 3 and Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                Score = Score + 5
            elif Song[i + 4] - Song[i + 3] == 4 and Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                Score = Score + 5
            elif Song[i + 3] - Song[i + 4] == 4 and Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                Score = Score + 5
        i = i + 1
    return Score
############################################################################################
# def SimilarityOfSongs(DataOfSong1, DataOfSong2):
#     SimilarityScore = []
#     for i in range(0, LengthOfEachPiece):
#         res = abs(DataOfSong1[i]-DataOfSong2[i])
#         SimilarityScore.append(1 - math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(res/Domain))))))
#     return 100 * sum(SimilarityScore) / len(SimilarityScore)
# ############################################################################################
# def SimilarityOfSongs(DataOfSong1, DataOfSong2):
#     score = 0
#     i = 0
#     while i < (LengthOfEachPiece - 1):
#         if DataOfSong1[i] == 0 or DataOfSong1[i+1] == 0 or DataOfSong2[i] == 0 or DataOfSong2[i+1] == 0:
#             i = i + 2
#             continue
#         x1 = DataOfSong1[i + 1] - DataOfSong1[i]
#         x2 = DataOfSong2[i + 1] - DataOfSong2[i]
#         ΔX = x2 - x1
#         if ΔX == 0:
#             score = score + 2
#         else:
#             score = score - (2 - (2 / abs(ΔX)))
#         i = i + 2
#     return score
############################################################################################
def SimilarityOfSongs(DataOfSong1, DataOfSong2):
    SimilarityScore = []
    for i in range(0, LengthOfEachPiece):
        res = abs(DataOfSong1[i]-DataOfSong2[i])
        SimilarityScore.append(1 - math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(res/Domain))))))
    x = 100 * sum(SimilarityScore) / len(SimilarityScore)
    score = 0
    i = 0
    while i < (LengthOfEachPiece - 1):
        if DataOfSong1[i] == 0 or DataOfSong1[i + 1] == 0 or DataOfSong2[i] == 0 or DataOfSong2[i + 1] == 0:
            i = i + 2
            continue
        x1 = DataOfSong1[i + 1] - DataOfSong1[i]
        x2 = DataOfSong2[i + 1] - DataOfSong2[i]
        ΔX = x2 - x1
        if ΔX == 0:
            score = score + 2
        else:
            score = score - (2 - (2 / abs(ΔX)))
        i = i + 2
    return x + score
############################################################################################



############################################################################################
# suitable distances
############################################################################################
# GoodDistances
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
#         Scores.append(res/len(songs))
#         res = 0
#     return Scores
############################################################################################
def Fitness(Population):
    Scores = []
    res = 0
    for i in range(0, len(Population)):
        s = SuitableDistances(Population[i])
        Scores.append(s)
        s = 0
    return Scores
############################################################################################
# def Fitness(Population):
#     Scores = []
#     res = 0
#     for i in range(0, len(Population)):
#         k1 = random.randint(0, len(songs) - 1)
#         k2 = random.randint(0, len(songs) - 1)
#         while k2 == k1:
#             k2 = random.randint(0, len(songs) - 1)
#         res = res + SimilarityOfSongs(songs[k1], Population[i])
#         res = res + SimilarityOfSongs(songs[k1], Population[i])
#         Scores.append(res/2)
#         res = 0
#     return Scores
############################################################################################




############################################################################################
# Roulette wheel
############################################################################################
def RouletteWheel(Population):
    NewPopulation = []
    Scores = Fitness(Population)
    minimum = min(Scores)
    if minimum < 0:
        for i in range(0, len(Scores)):
            Scores[i] = Scores[i] - minimum
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
print(Population[IndexOfBest])
print(max(Scores))
    # return Population[IndexOfBest]
############################################################################################



############################################################################################
# make all the music
############################################################################################
# result = []
# for i in range(0, LengthOfResult):
#     n = ProduceMusicParts()
#     result.append(n)
#     # songs.append(n)
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     print(i + 1)
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print(result)
############################################################################################



############################################################################################
# Plot
############################################################################################
plt.plot(FitnessAvrage)
plt.plot(FitnessMaximum)
plt.show()
###########################################################################################
