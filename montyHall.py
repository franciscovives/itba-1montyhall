#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 07:32:55 2022

@author: francisco
"""
import numpy as np
from matplotlib import pyplot as plt

# Initializing the possible combinations of doors and 1=car 0=goat
doors = 3
universe=[0]*doors
for i in range(doors):
    universe[i]=[0]*doors
    for j in range(doors):
        universe[i][j]=0
        if (i==j):
            universe[i][j]=1
print(universe)



simulation = 10000
# Hits acumulados
change_acum = [0]*simulation
no_change_acum = [0]*simulation
rand_sel_acum = [0]*simulation

# the default selected door is the first one (0)
win_random=0
win_change_door=0
win_keep_door=0

# Run simulation
for i in range(simulation):
    car_door=np.random.randint(doors);
    if (car_door == 0):
        win_keep_door += 1
    else:
         win_change_door += 1
         change_acum[i] = win_change_door
    #Create a random choice between the open doors
    randomChoice=np.random.randint(doors-1);
    if (randomChoice == 1):
        win_random += 1
    no_change_acum[i] = win_keep_door
    rand_sel_acum[i] = win_random
    change_acum[i] = win_change_door

print("How many times each won in simulation of", simulation)
print("Random", 100*win_random/simulation, sep=": %")
print("Keep Door", 100*win_keep_door/simulation, sep=": %")
print("Change Door", 100*win_change_door/simulation, sep=": %")

plt.figure(figsize=(16,8))
plt.plot(no_change_acum, label='No cambio')
plt.plot(change_acum, label='Cambio', linestyle='dashed', linewidth=5, markersize=12)
plt.plot(rand_sel_acum, label='Al azar', linestyle='dashed', linewidth=2, markersize=12)
plt.xlabel('Iteración')
plt.ylabel('hits')
plt.legend()
plt.show()


