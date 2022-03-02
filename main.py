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

# [samplerate, y] = wavread('Glow.wav')
# [samplerate, z] = wavread('02 Up and Down (Piano).wav')
# print(len(y), len(z))
#
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
# Libraries
#############################################################################
import random
import scipy
from scipy.io.wavfile import read as wavread
import time
import numpy as np
#############################################################################



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
SongLength = 6
#############################################################################



#############################################################################
# Random Primary Population
#############################################################################
PrimaryPopulation = []
for i in range(0, NumberOfPrimaryPopulation):
    PrimaryPopulation.append([])
    print(i)
    for _ in range(0, SongLength*SampleRate):
        PrimaryPopulation[i].append([random.randint(-32768, 32767), random.randint(-32768, 32767)])
#############################################################################



#############################################################################
# Roulette wheel mutation
#############################################################################
def RouletteWheelMutation():
    pass
#############################################################################



#############################################################################
# Crossover
#############################################################################
def Crossover():
    pass
#############################################################################
