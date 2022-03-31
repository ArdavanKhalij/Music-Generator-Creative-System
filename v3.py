############################################################################################
# Libraries
############################################################################################
import math
import random
import matplotlib.pyplot as plt
from numpy.random import choice
import copy
from music21 import *
############################################################################################



############################################################################################
# General info of algorithm
############################################################################################
# Number of primary population
NumberOfPrimaryPopulation = 500
# Number of Generations
NumberOfGenerations = 200
# Mutation Probability
MutationProbability = 0.2
# Length of each piece
LengthOfEachPiece = 20
# Length of result
LengthOfResult = 10
# Domain
Domain = 12
# Inputs
songs = [
    [2, 3, 5, 3, 2, 11, 2, 3, 5, 3, 2, 11, 10, 10, 10, 10, 0, 0, 0, 0],
    [10, 10, 10, 10, 8, 10, 8, 8, 0, 0, 0, 0, 6, 6, 5, 5, 6, 8, 10, 10],
    [6, 6, 5, 3, 2, 3, 5, 6, 0, 0, 0, 8, 8, 8, 6, 5, 3, 5, 6, 8],
    [10, 10, 10, 5, 6, 0, 8, 6, 5, 3, 5, 10, 6, 5, 3, 2, 3, 3, 3, 3],
    [8, 8, 5, 5, 3, 3, 10, 10, 0, 0, 0, 0, 5, 5, 3, 3, 1, 1, 8, 8],
    [3, 3, 1, 1, 11, 11, 6, 6, 0, 0, 0, 0, 8, 6, 8, 10, 1, 11, 10, 0],
    [7, 10, 3, 1, 11, 10, 11, 10, 11, 10, 8, 6, 5, 5, 5, 5, 5, 0, 0, 0]
    # [1, 1, 3, 3, 5, 8, 5, 1, 1, 1, 1, 1, 3, 3, 5, 5, 5, 1, 0, 0]
]
# Chosen Chord
CHOOSEN_CHORD = 'Major'
# unavailable repeats
REPEAT = 20
# Score for continous notes
SFCN = 2
# Score for chords
SFC = 4
# Score for no change
SFNC = 1
weights = [0] * len(songs)
############################################################################################



############################################################################################
# Percent of similarity of two songs
############################################################################################
def SimilarityOfSongs(DataOfSong1, DataOfSong2):
    SimilarityScore = []
    Score = 0
    if DataOfSong1 == DataOfSong2:
        Score = 0
    else:
        for i in range(0, LengthOfEachPiece):
            res = abs(DataOfSong1[i] - DataOfSong2[i])
            SimilarityScore.append(1 - math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(res / Domain))))))
        Score = 100 * sum(SimilarityScore) / len(SimilarityScore)
    return Score
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
# def SimilarityOfSongs(DataOfSong1, DataOfSong2):
#     SimilarityScore = []
#     for i in range(0, LengthOfEachPiece):
#         res = abs(DataOfSong1[i]-DataOfSong2[i])
#         SimilarityScore.append(1 - math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(res/Domain))))))
#     x = 100 * sum(SimilarityScore) / len(SimilarityScore)
#     score = 0
#     i = 0
#     while i < (LengthOfEachPiece - 1):
#         if DataOfSong1[i] == 0 or DataOfSong1[i + 1] == 0 or DataOfSong2[i] == 0 or DataOfSong2[i + 1] == 0:
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
#     return x + score
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
                Score = Score + SFNC
            elif (Song[i] == 1 and Song[i+1] == 3) or (Song[i] == 3 and Song[i+1] == 1) or (Song[i] == 3 and Song[i+1] == 5) or (Song[i] == 5 and Song[i+1] == 3) or (Song[i] == 5 and Song[i+1] == 6) or (Song[i] == 6 and Song[i+1] == 5) or (Song[i] == 6 and Song[i+1] == 8) or (Song[i] == 8 and Song[i+1] == 6) or (Song[i] == 8 and Song[i+1] == 10) or (Song[i] == 10 and Song[i+1] == 8) or (Song[i] == 10 and Song[i+1] == 12) or (Song[i] == 12 and Song[i+1] == 10):
                Score = Score + SFCN
            else:
                pass
        i = i + 1
    i = 0
    if CHOOSEN_CHORD == 'Major' or CHOOSEN_CHORD == 'Minor' or CHOOSEN_CHORD == 'Augmented' or CHOOSEN_CHORD == 'Diminished' or CHOOSEN_CHORD == 'Sus_2' or CHOOSEN_CHORD == 'Sus_4':
        while i < len(Song) - 4:
            if Song[i] != 0 or Song[i + 1] != 0 or Song[i + 2] != 0:
                if Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                    if CHOOSEN_CHORD == 'Major':
                        Score = Score + SFC
                elif Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                    if CHOOSEN_CHORD == 'Major':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 3:
                    if CHOOSEN_CHORD == 'Minor':
                        Score = Score + SFC
                elif Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i +1] == 3:
                    if CHOOSEN_CHORD == 'Minor':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 4:
                    if CHOOSEN_CHORD == 'Augmented':
                        Score = Score + SFC
                elif Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 4:
                    if CHOOSEN_CHORD == 'Augmented':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 3:
                    if CHOOSEN_CHORD == 'Diminished':
                        Score = Score + SFC
                elif Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i +1] == 3:
                    if CHOOSEN_CHORD == 'Diminished':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 1] == 2 and Song[i + 1] - Song[i] == 5:
                    if CHOOSEN_CHORD == 'Sus_2':
                        Score = Score + SFC
                elif Song[i + 1] - Song[i + 2] == 2 and Song[i] - Song[i + 1] == 5:
                    if CHOOSEN_CHORD == 'Sus_2':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 1] == 5 and Song[i + 1] - Song[i] == 2:
                    if CHOOSEN_CHORD == 'Sus_4':
                        Score = Score + SFC
                elif Song[i + 1] - Song[i + 2] == 5 and Song[i] - Song[i +1] == 2:
                    if CHOOSEN_CHORD == 'Sus_4':
                        Score = Score + SFC
                else:
                    pass
            i = i + 1
    i = 0
    if CHOOSEN_CHORD == 'Major_7' or CHOOSEN_CHORD == 'Minor_7' or CHOOSEN_CHORD == 'Dominant_7' or CHOOSEN_CHORD == 'Diminished_7' or CHOOSEN_CHORD == 'Augmented_Major' or CHOOSEN_CHORD == 'Minor_Major_7' or CHOOSEN_CHORD == 'Half_Diminished_7' or CHOOSEN_CHORD == 'Major_6' or CHOOSEN_CHORD == 'Minor_6':
        while i < len(Song) - 5:
            if Song[i] != 0 or Song[i + 1] != 0 or Song[i + 2] != 0 or Song[i + 3] != 0:
                if Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                    if CHOOSEN_CHORD == 'Major_7':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                    if CHOOSEN_CHORD == 'Major_7':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 3:
                    if CHOOSEN_CHORD == 'Minor_7':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 3:
                    if CHOOSEN_CHORD == 'Minor_7':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 3:
                    if CHOOSEN_CHORD == 'Dominant_7':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 3:
                    if CHOOSEN_CHORD == 'Dominant_7':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 3:
                    if CHOOSEN_CHORD == 'Diminished_7':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 3:
                    if CHOOSEN_CHORD == 'Diminished_7':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 3:
                    if CHOOSEN_CHORD == 'Augmented_Major':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 3:
                    if CHOOSEN_CHORD == 'Augmented_Major':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 4:
                    if CHOOSEN_CHORD == 'Minor_Major_7':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 4:
                    if CHOOSEN_CHORD == 'Minor_Major_7':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                    if CHOOSEN_CHORD == 'Half_Diminished_7':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                    if CHOOSEN_CHORD == 'Half_Diminished_7':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 2:
                    if CHOOSEN_CHORD == 'Major_6':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 2:
                    if CHOOSEN_CHORD == 'Major_6':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 2:
                    if CHOOSEN_CHORD == 'Minor_6':
                        Score = Score + SFC
                elif Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 2:
                    if CHOOSEN_CHORD == 'Minor_6':
                        Score = Score + SFC
                else:
                    pass
            i = i + 1
    i = 0
    if CHOOSEN_CHORD == 'Major_9' or CHOOSEN_CHORD == 'Minor_9' or CHOOSEN_CHORD == 'Dominant_9':
        while i < len(Song) - 6:
            if Song[i] != 0 or Song[i + 1] != 0 or Song[i + 2] != 0 or Song[i + 3] != 0 or Song[i + 4] != 0:
                if Song[i + 4] - Song[i + 3] == 4 and Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 4 and Song[i + 1] - Song[i] == 3:
                    if CHOOSEN_CHORD == 'Major_9':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 4] == 4 and Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 4 and Song[i] - Song[i + 1] == 3:
                    if CHOOSEN_CHORD == 'Major_9':
                        Score = Score + SFC
                elif Song[i + 4] - Song[i + 3] == 3 and Song[i + 3] - Song[i + 2] == 4 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                    if CHOOSEN_CHORD == 'Minor_9':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 4] == 3 and Song[i + 2] - Song[i + 3] == 4 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                    if CHOOSEN_CHORD == 'Minor_9':
                        Score = Score + SFC
                elif Song[i + 4] - Song[i + 3] == 4 and Song[i + 3] - Song[i + 2] == 3 and Song[i + 2] - Song[i + 1] == 3 and Song[i + 1] - Song[i] == 4:
                    if CHOOSEN_CHORD == 'Dominant_9':
                        Score = Score + SFC
                elif Song[i + 3] - Song[i + 4] == 4 and Song[i + 2] - Song[i + 3] == 3 and Song[i + 1] - Song[i + 2] == 3 and Song[i] - Song[i + 1] == 4:
                    if CHOOSEN_CHORD == 'Dominant_9':
                        Score = Score + SFC
            i = i + 1
    return Score
############################################################################################



############################################################################################
# Repeated note
############################################################################################
def Repeat(song):
    repeat = 0
    Score = 0
    for i in range(0, 12):
        for j in song:
            if i == j:
                repeat = repeat + 1
        if (repeat / len(song) * 100) >= REPEAT:
            Score = Score - repeat
        repeat = 0
    return Score
############################################################################################



############################################################################################
# Fitness
############################################################################################
def Fitness(Population):
    Scores = []
    res = 0
    for i in range(0, len(Population)):
        if len(songs) > 0:
            for j in range(0, len(songs)):
                res = res + weights[j]*SimilarityOfSongs(songs[j], Population[i])
            res = res / len(songs) + SuitableDistances(Population[i])
        else:
            pass
            res = SuitableDistances(Population[i])
        res = res + Repeat(Population[i]) + SuitableDistances(Population[i])
        Scores.append(res)
        res = 0
    return Scores
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
# playing the music
############################################################################################
def PLAY(Songs):
    StringForPlay = []
    for song in Songs:
        for NOTE in song:
            if NOTE == 0:
                StringForPlay.append(note.Rest())
            elif NOTE == 1:
                StringForPlay.append(note.Note('C'))
            elif NOTE == 2:
                StringForPlay.append(note.Note('C#'))
            elif NOTE == 3:
                StringForPlay.append(note.Note('D'))
            elif NOTE == 4:
                StringForPlay.append(note.Note('D#'))
            elif NOTE == 5:
                StringForPlay.append(note.Note('E'))
            elif NOTE == 6:
                StringForPlay.append(note.Note('F'))
            elif NOTE == 7:
                StringForPlay.append(note.Note('F#'))
            elif NOTE == 8:
                StringForPlay.append(note.Note('G'))
            elif NOTE == 9:
                StringForPlay.append(note.Note('G#'))
            elif NOTE == 10:
                StringForPlay.append(note.Note('A'))
            elif NOTE == 11:
                StringForPlay.append(note.Note('A#'))
            elif NOTE == 12:
                StringForPlay.append(note.Note('B'))
            else:
                pass
    s = stream.Stream(StringForPlay)
    s.show()
    print(s)
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
def ProduceMusicParts():
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
    return Population[IndexOfBest]
############################################################################################



############################################################################################
# make all the music
############################################################################################
result = []
for i in range(0, LengthOfResult):
    ####################
    weights = [0] * len(songs)
    for j in range(0, len(songs)):
        for k in range(0, len(songs)):
            if j != k:
                r = SimilarityOfSongs(songs[j], songs[k])
                weights[j] = weights[j] + (100 - r) / r
                weights[k] = weights[k] + (100 - r) / r
    s = sum(weights)
    for j in range(0, len(weights)):
        weights[j] = weights[j] / s
    print(weights)
    ####################
    n = ProduceMusicParts()
    result.append(n)
    if i == 0:
        songs.append(n)
    else:
        songs.pop()
        songs.append(n)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(i + 1)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
PLAY(result)
print(result)
############################################################################################



############################################################################################
# Plot
############################################################################################
# plt.plot(FitnessAvrage)
# plt.plot(FitnessMaximum)
# plt.show()
###########################################################################################
