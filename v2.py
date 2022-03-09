############################################################################################
# Libraries
############################################################################################
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
NumberOfPrimaryPopulation = 30
# Number of Generations
NumberOfGenerations = 30
# Mutation Probability
MutationProbability = 0.1
# Length
length = 100
# Input 1
song1 = [[14, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [17, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [14, 0, 0, 0, 0],
         [11, 0, 0, 0, 0],
         [14, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [17, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [14, 0, 0, 0, 0],
         [11, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
# Input 2
song2 = [[10, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [10, 0, 0, 0, 0]
         [10, 0, 0, 0, 0]]
# Input 3
song3 = [[6, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [3, 0, 0, 0, 0],
         [2, 0, 0, 0, 0],
         [3, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [3, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [8, 0, 0, 0, 0]]
# Input 4
song4 = [[10, 0, 0, 0, 0],
         [8, 10, 0, 0, 0],
         [6, 10, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [5, 10, 0, 0, 0],
         [3, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [3, 0, 0, 0, 0],
         [2, 0, 0, 0, 0],
         [3, 0, 0, 0, 0],
         [3, 0, 0, 0, 0],
         [3, 0, 0, 0, 0],
         [3, 0, 0, 0, 0]]
# Input 5
song5 = [[20, 0, 0, 0, 0],
         [20, 0, 0, 0, 0],
         [17, 0, 0, 0, 0],
         [17, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [17, 0, 0, 0, 0],
         [17, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [13, 0, 0, 0, 0],
         [13, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [8, 0, 0, 0, 0]]
# Input 6
song6 = [[15, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [13, 0, 0, 0, 0],
         [13, 0, 0, 0, 0],
         [11, 0, 0, 0, 0],
         [11, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [13, 0, 0, 0, 0],
         [11, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
# Input 7
song7 = [[7, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [13, 0, 0, 0, 0],
         [11, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [11, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [11, 0, 0, 0, 0],
         [10, 0, 0, 0, 0],
         [8, 0, 0, 0, 0],
         [6, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [5, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
# Input 8
song8 = [[8, 11, 0, 0, 0],
         [8, 11, 0, 0, 0],
         [8, 11, 0, 0, 0],
         [8, 11, 0, 0, 0],
         [6, 10, 0, 0, 0],
         [6, 10, 0, 0, 0],
         [5, 8, 0, 0, 0],
         [5, 8, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [3, 6, 0, 0, 0],
         [3, 6, 0, 0, 0],
         [5, 8, 0, 0, 0],
         [6, 10, 0, 0, 0],
         [10, 13, 0, 0, 0],
         [8, 11, 0, 0, 0],
         [6, 10, 0, 0, 0],
         [0, 0, 0, 0, 0]]
# Input 9
song9 = [[15, 0, 0, 0, 0],
         [15, 0, 0, 0, 0],
         [15, 18, 22, 0, 0],
         [15, 18, 22, 0, 0],
         [15, 18, 22, 0, 0],
         [15, 18, 22, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 17, 22, 0, 0],
         [1, 17, 22, 0, 0],
         [1, 17, 22, 0, 0],
         [1, 17, 22, 0, 0],
         [11, 0, 0, 0, 0],
         [11, 0, 0, 0, 0],
         [11, 15, 18, 0, 0],
         [11, 15, 18, 0, 0],
         [11, 15, 18, 0, 0],
         [11, 15, 18, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
############################################################################################



############################################################################################
# All 216 piano chords
############################################################################################
Chords = [
    ['C_Major', [1, 5, 8, 0, 0]],
    ['Db_Major', [2, 6, 9, 0, 0]],
    ['D_Major', [3, 7, 10, 0, 0]],
    ['Eb_Major', [4, 8, 11, 0, 0]],
    ['E_Major', [5, 9, 12, 0, 0]],
    ['F_Major', [6, 10, 13, 0, 0]],
    ['Gb_Major', [7, 11, 14, 0, 0]],
    ['G_Major', [8, 12, 15, 0, 0]],
    ['Ab_Major', [9, 13, 16, 0, 0]],
    ['A_Major', [10, 14, 17, 0, 0]],
    ['Bb_Major', [11, 15, 18, 0, 0]],
    ['B_Major', [12, 16, 19, 0, 0]],
    ['C_Minor', [1, 4, 8, 0, 0]],
    ['Db_Minor', [2, 5, 9, 0, 0]],
    ['D_Minor', [3, 6, 10, 0, 0]],
    ['Eb_Minor', [4, 7, 11, 0, 0]],
    ['E_Minor', [5, 8, 12, 0, 0]],
    ['F_Minor', [6, 9, 13, 0, 0]],
    ['Gb_Minor', [7, 10, 14, 0, 0]],
    ['G_Minor', [8, 11, 15, 0, 0]],
    ['Ab_Minor', [9, 12, 16, 0, 0]],
    ['A_Minor', [10, 13, 17, 0, 0]],
    ['Bb_Minor', [11, 14, 18, 0, 0]],
    ['B_Minor', [12, 15, 19, 0, 0]],
    ['C_Augmented', [1, 5, 9, 0, 0]],
    ['Db_Augmented', [2, 6, 10, 0, 0]],
    ['D_Augmented', [3, 7, 11, 0, 0]],
    ['Eb_Augmented', [4, 8, 12, 0, 0]],
    ['E_Augmented', [5, 9, 13, 0, 0]],
    ['F_Augmented', [6, 10, 14, 0, 0]],
    ['Gb_Augmented', [7, 11, 15, 0, 0]],
    ['G_Augmented', [8, 12, 16, 0, 0]],
    ['Ab_Augmented', [9, 13, 17, 0, 0]],
    ['A_Augmented', [10, 14, 18, 0, 0]],
    ['Bb_Augmented', [11, 15, 19, 0, 0]],
    ['B_Augmented', [12, 16, 20, 0, 0]],
    ['C_Diminished', [1, 4, 7, 0, 0]],
    ['Db_Diminished', [2, 5, 8, 0, 0]],
    ['D_Diminished', [3, 6, 9, 0, 0]],
    ['Eb_Diminished', [4, 7, 10, 0, 0]],
    ['E_Diminished', [5, 8, 11, 0, 0]],
    ['F_Diminished', [6, 9, 12, 0, 0]],
    ['Gb_Diminished', [7, 10, 13, 0, 0]],
    ['G_Diminished', [8, 11, 14, 0, 0]],
    ['Ab_Diminished', [9, 12, 15, 0, 0]],
    ['A_Diminished', [10, 13, 16, 0, 0]],
    ['Bb_Diminished', [11, 14, 17, 0, 0]],
    ['B_Diminished', [12, 15, 18, 0, 0]],
    ['C_Major_7', [1, 5, 8, 12, 0]],
    ['Db_Major_7', [2, 6, 9, 13, 0]],
    ['D_Major_7', [3, 7, 10, 14, 0]],
    ['Eb_Major_7', [4, 8, 11, 15, 0]],
    ['E_Major_7', [5, 9, 12, 16, 0]],
    ['F_Major_7', [6, 10, 13, 17, 0]],
    ['Gb_Major_7', [7, 11, 14, 18, 0]],
    ['G_Major_7', [8, 12, 15, 19, 0]],
    ['Ab_Major_7', [9, 13, 16, 20, 0]],
    ['A_Major_7', [10, 14, 17, 21, 0]],
    ['Bb_Major_7', [11, 15, 18, 22, 0]],
    ['B_Major_7', [12, 16, 19, 23, 0]],
    ['C_Minor_7', [1, 4, 8, 11, 0]],
    ['Db_Minor_7', [2, 5, 9, 12, 0]],
    ['D_Minor_7', [3, 6, 10, 13, 0]],
    ['Eb_Minor_7', [4, 7, 11, 14, 0]],
    ['E_Minor_7', [5, 8, 12, 15, 0]],
    ['F_Minor_7', [6, 9, 13, 16, 0]],
    ['Gb_Minor_7', [7, 10, 14, 17, 0]],
    ['G_Minor_7', [8, 11, 15, 18, 0]],
    ['Ab_Minor_7', [9, 12, 16, 19, 0]],
    ['A_Minor_7', [10, 13, 17, 20, 0]],
    ['Bb_Minor_7', [11, 14, 18, 21, 0]],
    ['B_Minor_7', [12, 15, 19, 22, 0]],
    ['C_Dominant', [1, 5, 8, 11, 0]],
    ['Db_Dominant', [2, 6, 9, 12, 0]],
    ['D_Dominant', [3, 7, 10, 13, 0]],
    ['Eb_Dominant', [4, 8, 11, 14, 0]],
    ['E_Dominant', [5, 9, 12, 15, 0]],
    ['F_Dominant', [6, 10, 13, 16, 0]],
    ['Gb_Dominant', [7, 11, 14, 17, 0]],
    ['G_Dominant', [8, 12, 15, 18, 0]],
    ['Ab_Dominant', [9, 13, 16, 19, 0]],
    ['A_Dominant', [10, 14, 17, 20, 0]],
    ['Bb_Dominant', [11, 15, 18, 21, 0]],
    ['B_Dominant', [12, 16, 19, 22, 0]],
    ['C_Diminished_7', [1, 4, 7, 10, 0]],
    ['Db_Diminished_7', [2, 5, 8, 11, 0]],
    ['D_Diminished_7', [3, 6, 9, 12, 0]],
    ['Eb_Diminished_7', [4, 7, 10, 13, 0]],
    ['E_Diminished_7', [5, 8, 11, 14, 0]],
    ['F_Diminished_7', [6, 9, 12, 15, 0]],
    ['Gb_Diminished_7', [7, 10, 13, 16, 0]],
    ['G_Diminished_7', [8, 11, 14, 17, 0]],
    ['Ab_Diminished_7', [9, 12, 15, 18, 0]],
    ['A_Diminished_7', [10, 13, 16, 19, 0]],
    ['Bb_Diminished_7', [11, 14, 17, 20, 0]],
    ['B_Diminished_7', [12, 15, 18, 21, 0]],
    ['C_Augmented_Major_7', [1, 5, 9, 12, 0]],
    ['Db_Augmented_Major_7', [2, 6, 10, 13, 0]],
    ['D_Augmented_Major_7', [3, 7, 11, 14, 0]],
    ['Eb_Augmented_Major_7', [4, 8, 12, 15, 0]],
    ['E_Augmented_Major_7', [5, 9, 13, 16, 0]],
    ['F_Augmented_Major_7', [6, 10, 14, 17, 0]],
    ['Gb_Augmented_Major_7', [7, 11, 15, 18, 0]],
    ['G_Augmented_Major_7', [8, 12, 16, 19, 0]],
    ['Ab_Augmented_Major_7', [9, 13, 17, 20, 0]],
    ['A_Augmented_Major_7', [10, 14, 18, 21, 0]],
    ['Bb_Augmented_Major_7', [11, 15, 19, 22, 0]],
    ['B_Augmented_Major_7', [12, 16, 20, 23, 0]],
    ['C_Minor_Major_7', [1, 4, 8, 12, 0]],
    ['Db_Minor_Major_7', [2, 5, 9, 13, 0]],
    ['D_Minor_Major_7', [3, 6, 10, 14, 0]],
    ['Eb_Minor_Major_7', [4, 7, 11, 15, 0]],
    ['E_Minor_Major_7', [5, 8, 12, 16, 0]],
    ['F_Minor_Major_7', [6, 9, 13, 17, 0]],
    ['Gb_Minor_Major_7', [7, 10, 14, 18, 0]],
    ['G_Minor_Major_7', [8, 11, 15, 19, 0]],
    ['Ab_Minor_Major_7', [9, 12, 16, 20, 0]],
    ['A_Minor_Major_7', [10, 13, 17, 21, 0]],
    ['Bb_Minor_Major_7', [11, 14, 18, 22, 0]],
    ['B_Minor_Major_7', [12, 15, 19, 23, 0]],
    ['C_Half_Diminished_7', [1, 4, 7, 11, 0]],
    ['Db_Half_Diminished_7', [2, 5, 8, 12, 0]],
    ['D_Half_Diminished_7', [3, 6, 9, 13, 0]],
    ['Eb_Half_Diminished_7', [4, 7, 10, 14, 0]],
    ['E_Half_Diminished_7', [5, 8, 11, 15, 0]],
    ['F_Half_Diminished_7', [6, 9, 12, 16, 0]],
    ['Gb_Half_Diminished_7', [7, 10, 13, 17, 0]],
    ['G_Half_Diminished_7', [8, 11, 14, 18, 0]],
    ['Ab_Half_Diminished_7', [9, 12, 15, 19, 0]],
    ['A_Half_Diminished_7', [10, 13, 16, 20, 0]],
    ['Bb_Half_Diminished_7', [11, 14, 17, 21, 0]],
    ['B_Half_Diminished_7', [12, 15, 18, 22, 0]],
    ['C_Major_6', [1, 5, 8, 10, 0]],
    ['Db_Major_6', [2, 6, 9, 11, 0]],
    ['D_Major_6', [3, 7, 10, 12, 0]],
    ['Eb_Major_6', [4, 8, 11, 13, 0]],
    ['E_Major_6', [5, 9, 12, 14, 0]],
    ['F_Major_6', [6, 10, 13, 15, 0]],
    ['Gb_Major_6', [7, 11, 14, 16, 0]],
    ['G_Major_6', [8, 12, 15, 17, 0]],
    ['Ab_Major_6', [9, 13, 16, 18, 0]],
    ['A_Major_6', [10, 14, 17, 19, 0]],
    ['Bb_Major_6', [11, 15, 18, 20, 0]],
    ['B_Major_6', [12, 16, 19, 21, 0]],
    ['C_Minor_6', [1, 4, 8, 10, 0]],
    ['Db_Minor_6', [2, 5, 9, 11, 0]],
    ['D_Minor_6', [3, 6, 10, 12, 0]],
    ['Eb_Minor_6', [4, 7, 11, 13, 0]],
    ['E_Minor_6', [5, 8, 12, 14, 0]],
    ['F_Minor_6', [6, 9, 13, 15, 0]],
    ['Gb_Minor_6', [7, 10, 14, 16, 0]],
    ['G_Minor_6', [8, 11, 15, 17, 0]],
    ['Ab_Minor_6', [9, 12, 16, 18, 0]],
    ['A_Minor_6', [10, 13, 17, 19, 0]],
    ['Bb_Minor_6', [11, 14, 18, 20, 0]],
    ['B_Minor_6', [12, 15, 19, 21, 0]],
    ['C_Major_9', [1, 5, 8, 12, 15]],
    ['Db_Major_9', [2, 6, 9, 13, 16]],
    ['D_Major_9', [3, 7, 10, 14, 17]],
    ['Eb_Major_9', [4, 8, 11, 15, 18]],
    ['E_Major_9', [5, 9, 12, 16, 19]],
    ['F_Major_9', [6, 10, 13, 17, 20]],
    ['Gb_Major_9', [7, 11, 14, 18, 21]],
    ['G_Major_9', [8, 12, 15, 19, 22]],
    ['Ab_Major_9', [9, 13, 16, 20, 23]],
    ['A_Major_9', [10, 14, 17, 21, 24]],
    ['Bb_Major_9', [11, 15, 18, 22, 25]],
    ['B_Major_9', [12, 16, 19, 23, 26]],
    ['C_Minor_9', [1, 4, 8, 11, 15]],
    ['Db_Minor_9', [2, 5, 9, 12, 16]],
    ['D_Minor_9', [3, 6, 10, 13, 17]],
    ['Eb_Minor_9', [4, 7, 11, 14, 18]],
    ['E_Minor_9', [5, 8, 12, 15, 19]],
    ['F_Minor_9', [6, 9, 13, 16, 20]],
    ['Gb_Minor_9', [7, 10, 14, 17, 21]],
    ['G_Minor_9', [8, 11, 15, 18, 22]],
    ['Ab_Minor_9', [9, 12, 16, 19, 23]],
    ['A_Minor_9', [10, 13, 17, 20, 24]],
    ['Bb_Minor_9', [11, 14, 18, 21, 25]],
    ['B_Minor_9', [12, 15, 19, 22, 26]],
    ['C_Dominant_9', [1, 5, 8, 11, 15]],
    ['Db_Dominant_9', [2, 6, 9, 12, 16]],
    ['D_Dominant_9', [3, 7, 10, 13, 17]],
    ['Eb_Dominant_9', [4, 8, 11, 14, 18]],
    ['E_Dominant_9', [5, 9, 12, 15, 19]],
    ['F_Dominant_9', [6, 10, 13, 16, 20]],
    ['Gb_Dominant_9', [7, 11, 14, 17, 21]],
    ['G_Dominant_9', [8, 12, 15, 18, 22]],
    ['Ab_Dominant_9', [9, 13, 16, 19, 23]],
    ['A_Dominant_9', [10, 14, 17, 20, 24]],
    ['Bb_Dominant_9', [11, 15, 18, 21, 25]],
    ['B_Dominant_9', [12, 16, 19, 22, 26]],
    ['C_Sus_2', [1, 3, 8, 0, 0]],
    ['Db_Sus_2', [2, 4, 9, 0, 0]],
    ['D_Sus_2', [3, 5, 10, 0, 0]],
    ['Eb_Sus_2', [4, 6, 11, 0, 0]],
    ['E_Sus_2', [5, 7, 12, 0, 0]],
    ['F_Sus_2', [6, 8, 13, 0, 0]],
    ['Gb_Sus_2', [7, 9, 14, 0, 0]],
    ['G_Sus_2', [8, 10, 15, 0, 0]],
    ['Ab_Sus_2', [9, 11, 16, 0, 0]],
    ['A_Sus_2', [10, 12, 17, 0, 0]],
    ['Bb_Sus_2', [11, 13, 18, 0, 0]],
    ['B_Sus_2', [12, 14, 19, 0, 0]],
    ['C_Sus_4', [1, 6, 8, 0, 0]],
    ['Db_Sus_4', [2, 7, 9, 0, 0]],
    ['D_Sus_4', [3, 8, 10, 0, 0]],
    ['Eb_Sus_4', [4, 9, 11, 0, 0]],
    ['E_Sus_4', [5, 10, 12, 0, 0]],
    ['F_Sus_4', [6, 11, 13, 0, 0]],
    ['Gb_Sus_4', [7, 12, 14, 0, 0]],
    ['G_Sus_4', [8, 13, 15, 0, 0]],
    ['Ab_Sus_4', [9, 14, 16, 0, 0]],
    ['A_Sus_4', [10, 15, 17, 0, 0]],
    ['Bb_Sus_4', [11, 16, 18, 0, 0]],
    ['B_Sus_4', [12, 17, 19, 0, 0]]
]
############################################################################################



############################################################################################
# Distances in Chords
############################################################################################
ChordsDistanses = [
    ['Major', ['x', 4, 3, 'empty', 'empty']],
    ['Minor', ['x', 3, 4, 'empty', 'empty']],
    ['Augmented', ['x', 4, 4, 'empty', 'empty']],
    ['Diminished', ['x', 3, 3, 'empty', 'empty']],
    ['Major_7', ['x', 4, 3, 4, 'empty']],
    ['Minor_7', ['x', 3, 4, 3, 'empty']],
    ['Dominant_7', ['x', 4, 3, 3, 'empty']],
    ['Diminished_7', ['x', 3, 3, 3, 'empty']],
    ['Augmented_Major', ['x', 4, 4, 3, 'empty']],
    ['Minor_Major_7', ['x', 3, 4, 4, 'empty']],
    ['Half_Diminished_7', ['x', 3, 3, 4, 'empty']],
    ['Major_6', ['x', 4, 3, 2, 'empty']],
    ['Minor_6', ['x', 3, 4, 2, 'empty']],
    ['Major_9', ['x', 4, 3, 4, 3]],
    ['Minor_9', ['x', 3, 4, 3, 4]],
    ['Dominant_9', ['x', 4, 3, 3, 4]],
    ['Sus_2', ['x', 2, 5, 'empty', 'empty']],
    ['Sus_4', ['x', 5, 2, 'empty', 'empty']],
]
############################################################################################



############################################################################################
# Primary Population
############################################################################################
PrimaryPopulation = []

############################################################################################



############################################################################################
# Finding the suitable Chords
############################################################################################

############################################################################################







































# ############################################################################################
# # Song Decoder
# ############################################################################################
# def SongDecoder(SongName):
#     DataOfSong = []
#     [_, y] = wavread(SongName)
#     for i in range(0, int(SongLength*SampleRate)):
#         y1, y2 = [y[i][0], y[i][1]]
#         res = int((y1 + y2) / 2)
#         DataOfSong.append(res)
#     return DataOfSong
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Data of Songs
# ############################################################################################
# SongData1 = SongDecoder(SongName1)
# SongData2 = SongDecoder(SongName2)
# SongData3 = SongDecoder(SongName3)
# SongData4 = SongDecoder(SongName4)
# SongData5 = SongDecoder(SongName5)
# SongData6 = SongDecoder(SongName6)
# SongData7 = SongDecoder(SongName7)
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Find the  local minimum and maximum
# ############################################################################################
# domainOfAllSongs = []
# domainOfAllSongs.append(min(SongData1))
# domainOfAllSongs.append(max(SongData1))
# domainOfAllSongs.append(min(SongData2))
# domainOfAllSongs.append(max(SongData2))
# domainOfAllSongs.append(min(SongData3))
# domainOfAllSongs.append(max(SongData3))
# domainOfAllSongs.append(min(SongData4))
# domainOfAllSongs.append(max(SongData4))
# domainOfAllSongs.append(min(SongData5))
# domainOfAllSongs.append(max(SongData5))
# domainOfAllSongs.append(min(SongData6))
# domainOfAllSongs.append(max(SongData6))
# domainOfAllSongs.append(min(SongData7))
# domainOfAllSongs.append(max(SongData7))
# MinOfDomain = min(domainOfAllSongs)
# MaxOfDomain = max(domainOfAllSongs)
# Domain = MaxOfDomain - MinOfDomain
# print(MinOfDomain, MaxOfDomain, Domain)
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Random Primary Population
# ############################################################################################
# print("-----------------------------------------")
# print("Primary Population")
# print("-----------------------------------------")
# PrimaryPopulation = []
# for i in range(0, NumberOfPrimaryPopulation):
#     PrimaryPopulation.append([])
#     print(i)
#     for _ in range(0, int(SongLength*SampleRate)):
#         PrimaryPopulation[i].append(random.randint(MinOfDomain, MaxOfDomain))
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Percent of similarity of two songs
# ############################################################################################
# def SimilarityOfSongs(DataOfSong1, DataOfSong2):
#     SimilarityScore = []
#     # 1-(DataOfSong1[i][0] - DataOfSong2[i][0])/Domain
#     for i in range(0, int(SongLength*SampleRate)):
#         res = abs(DataOfSong1[i] - DataOfSong2[i])
#         SimilarityScore.append(1 - res / Domain)
#     return sum(SimilarityScore)/len(SimilarityScore)
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Fitness function
# ############################################################################################
# def Fitness(Population):
#     print("-----------------------------------------")
#     print("Fitness Function")
#     print("-----------------------------------------")
#     Scores = []
#     res = 0
#     for i in range(0, len(Population)):
#         res = res + SimilarityOfSongs(SongData1, Population[i])
#         res = res + SimilarityOfSongs(SongData2, Population[i])
#         res = res + SimilarityOfSongs(SongData3, Population[i])
#         res = res + SimilarityOfSongs(SongData4, Population[i])
#         res = res + SimilarityOfSongs(SongData5, Population[i])
#         res = res + SimilarityOfSongs(SongData6, Population[i])
#         res = res + SimilarityOfSongs(SongData7, Population[i])
#         Scores.append(res/7)
#         res = 0
#     return Scores
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Roulette wheel
# ############################################################################################
# def RouletteWheel(Population):
#     print("-----------------------------------------")
#     print("Roulette Wheel")
#     print("-----------------------------------------")
#     NewPopulation = []
#     Scores = Fitness(Population)
#     ScoreSum = sum(Scores)
#     NormalizedScores = []
#     for i in range(0, len(Population)):
#         NormalizedScores.append(Scores[i]/ScoreSum)
#     res = 1 - sum(NormalizedScores)
#     index = len(NormalizedScores)-1
#     NormalizedScores[index] = NormalizedScores[index] + res
#     q = list(range(0, len(Population)))
#     for i in range(0, NumberOfPrimaryPopulation):
#         draw = choice(q, 1, p=NormalizedScores)
#         NewPopulation.append(Population[draw[0]])
#     return NewPopulation
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Mutation
# ############################################################################################
# def RSMMutation(Population):
#     print("-----------------------------------------")
#     print("Mutation")
#     print("-----------------------------------------")
#     for i in range(0, NumberOfPrimaryPopulation):
#         choose = random.uniform(0, 1)
#         if choose <= MutationProbability:
#             a = random.randint(0, int(SongLength*SampleRate))
#             b = random.randint(0, int(SongLength*SampleRate)-1)
#             while a == b:
#                 b = random.randint(0, int(SongLength * SampleRate)-1)
#             if a > b:
#                 while a > b:
#                     n1 = Population[i][a]
#                     n2 = Population[i][b]
#                     Population[i][b] = n1
#                     Population[i][a] = n2
#                     a = a - 1
#                     b = b + 1
#             else:
#                 while a < b:
#                     n1 = Population[i][a]
#                     n2 = Population[i][b]
#                     Population[i][b] = n1
#                     Population[i][a] = n2
#                     a = a + 1
#                     b = b - 1
#     return Population
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Mixing
# ############################################################################################
# def Mixing(Person1, Person2):
#     child1 = []
#     child2 = []
#     for i in range(0, len(Person1)):
#         child1.append((Person1[i]+(2*Person2[i]))/3)
#         child2.append((Person2[i] + (2 * Person1[i])) / 3)
#     return [Person1, Person2, child1, child2]
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Mating
# ############################################################################################
# def Mating(Population):
#     i = 0
#     NewPopulation = []
#     PopulationForMating = RouletteWheel(Population)
#     while i < (NumberOfPrimaryPopulation - 1):
#         n1 = PopulationForMating[i]
#         n2 = PopulationForMating[i + 1]
#         res = Mixing(n1, n2)
#         NewPopulation.append(res[0])
#         NewPopulation.append(res[1])
#         NewPopulation.append(res[2])
#         NewPopulation.append(res[3])
#         i = i + 2
#     return NewPopulation
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Test
# ############################################################################################
# FitnessAvrage = []
# FitnessMaximum = []
# IndexOfBest = 0
# print("##########################################################")
# print("Welcome")
# print("##########################################################")
# Population = copy.deepcopy(PrimaryPopulation)
# for i in range(0, NumberOfGenerations):
#     print("##########################################################")
#     print("Generation number ", i+1)
#     print("##########################################################")
#     Population2 = Mating(Population)
#     Population3 = RSMMutation(Population2)
#     Population4 = RouletteWheel(Population3)
#     Population = copy.deepcopy(Population4)
#     Scores = Fitness(Population)
#     IndexOfBest = Scores.index(max(Scores))
#     FitnessAvrage.append(sum(Scores)/len(Scores))
#     FitnessMaximum.append(max(Scores))
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Produce the song
# ############################################################################################
# data = Population[IndexOfBest]
# for i in range(0, len(data)):
#     res = int(data[i])
#     data[i] = res
# print(data)
# data2 = np.array(data)
# scipy.io.wavfile.write('sample.wav', SampleRate, data2.astype(np.int16))
# ############################################################################################
# 
# 
# 
# ############################################################################################
# # Plot
# ############################################################################################
# plt.plot(FitnessAvrage)
# plt.plot(FitnessMaximum)
# plt.show()
###########################################################################################


# heuristic to see the similarity of learning data and choose base on that to give songs value with fuzzy logic
# find max and min of learning songs and learn and generat primary population based on that.
