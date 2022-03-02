#############################################################################
# Libraries
#############################################################################
import random
import scipy
from scipy.io.wavfile import read as wavread
import time
import numpy as np
import math
#############################################################################
# import wave
# w_one = wave.open('01 Up and Down.wav', 'r')
# w_two = wave.open('02 Up and Down (Piano).wav', 'r')
#
# print(w_one.readframes(1))
# print(w_two.readframes(1))
#
# if w_one.readframes(1) == w_two.readframes(1):
#     print('exactly the same')
# else:
#     print('not a match')

# [samplerate, y] = wavread('despair2.wav')
# [samplerate, z] = wavread('upanddown1.wav')
# print(samplerate, len(y)/samplerate, len(z)/samplerate)

# start = time.time()
# w = []
#
# for x in range(0, 10*samplerate):
#     y1, y2 = [y[x][0], y[x][1]]
#     z1, z2 = [z[x][0], z[x][1]]
#     w.append([int((y1+z1)/2), int((y2+z2)/2)])
#     # print(x)
#     # print(y1, y2, z1, z2)
#
# print(w)
# ww = np.array(w)
# scipy.io.wavfile.write('sample.wav', samplerate, ww.astype(np.int16))
#
# end = time.time()
# print(end - start)



#############################################################################
# General info of algorithm
#############################################################################
# Number of primary population
NumberOfPrimaryPopulation = 100
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
# Roulette wheel mutation
#############################################################################
def RouletteWheelMutation(Population):
    print("-----------------------------------------")
    print("Roulette Wheel Mutation")
    print("-----------------------------------------")
    Scores = Fitness(Population)
    ScoreSum = sum(Scores)
    NormalizedScores = []
    for i in range(0, NumberOfPrimaryPopulation):
        NormalizedScores.append(Scores[i]/ScoreSum)
    res = 1 - sum(NormalizedScores)
    index = len(NormalizedScores)-1
    NormalizedScores[index] = NormalizedScores[index] + res
    return NormalizedScores
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
RouletteWheelMutation(PrimaryPopulation)
#############################################################################

# heuristic to see the similarity of learning data and choose base on that to give songs value with fuzzy logic
# find max and min of learning songs and learn and generat primary population based on that.
