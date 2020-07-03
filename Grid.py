import numpy as np
import matplotlib.pyplot as plt
import math
import random


"Klasse welche einen Raum für x Bakterien darstellt und die Größe des gesamten Raums definieren kann"

class space:
    def __init__(self, x, y):
        "Koordinaten entrsprechen der Mitte des entsprechenden Spaces"
        self.x = x
        self.y = y
        "Definieren Macimale Bakterien pro Space und Aktuelle Bakterien Anzahl und deren Nummerierung"
        self.bacteriaMax = 5
        self.bacteriaNow = 0
        self.bacteria = []

    def middle(self):
        return self.x, self.y


    def spawn(self, i):
        if self.bacteriaNow == self.bacteriaMax:
            return False
        else:
            self.bacteriaNow = self.bacteriaNow + 1
            self.bacteria.append(i)
            return True




"Bekommt die Größe des Grids übergeben, es sollten Integer Zahlen sein welche die Anzahl an Gridspaces beschreibt"

def generateGrid(size):
    grid = []
    k = range(size)
    for i in k:
        grid.append([])
        for j in k:
            grid[i].append(space(i * size + size/2, j * size + size/2))
    return grid

"generiert Grid mit fester QUADRATISCHER Größe"
grid = generateGrid(10)


"Checks Enviromenrt and returns every BActeria which is in the 8 surrounding spaces"
def check_local_enviroment(x, y):
    x = math.floor(x)
    y = math.floor(y)
    retlist = []
    k = range(-1, 2, 1)
    for i in k:
        for j in k:
            templist = [grid[x + i][y + j].bacteria]
            for bacteria in templist:
                retlist.append(bacteria)
    return retlist

def spawn(x,y, bacteria):
    x = math.floor(x)
    y = math.floor(y)
    tempspace = grid[x][y]
    tempspace.spawn(bacteria)
    grid[x][y] = tempspace
#ich habemir die freiheit genommen eine initiator spawn function hinzuzufügen
def init_spawn(bacteria):
    x=random.uniform(0,10)
    y=random.uniform(0,10)
    print(x)
    x = math.floor(x)
    y = math.floor(y)
    tempspace = grid[x][y]
    tempspace.spawn(bacteria)
    grid[x][y] = tempspace
#Die Funktion ist vielleicht ganz gut um einen Überblick zu bewahren, aber ist eigentlich nicht notwendig
def show_grid(size):
    '''shows the current distribution of bacteria in the grid'''
    vis_grid=[]
    for i in range(10):
        for l in range (10):
            vis_grid.append(grid[i][l].bacteria)
    print(vis_grid)
"Damit könnt ihjr kurz die fuunktion checken"

spawn(3.5, 5.7, 3)
spawn(3.5, 5.7, 6)
spawn(3.5, 5.7, 7)
spawn(3.5, 5.7, 8)
spawn(3.5, 5.7, 0)
print(check_local_enviroment(2,5))
