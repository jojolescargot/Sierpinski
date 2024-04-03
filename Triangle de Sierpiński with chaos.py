import pygame
from cmath import pi
from cmath import cos, sin
import math
import random
import numpy as np

pygame.init()







def makeTheFirstTriangle(surface,taille):
    width, height = surface.get_size()
    hauteur = math.sqrt(pow(taille, 2) - pow((taille / 2), 2))

    DotF= [width/2,height/2- 2/3*hauteur]
    DotS= [width/2 + (math.cos((330 * pi) / 180)*(hauteur * 2 / 3)), height/2 - (math.sin((330 * pi) / 180)*(hauteur * 2 / 3))]
    DotT= [width/2 + (math.cos((210 * pi) / 180)*(hauteur * 2 / 3)), height/2 - (math.sin((210 * pi) / 180)*(hauteur * 2 / 3))]
    pygame.draw.line(surface, [0,255,255], DotF, DotS)
    pygame.draw.line(surface, [0,255,255], DotS, DotT)
    pygame.draw.line(surface, [0,255,255], DotT, DotF)
    return DotF, DotS, DotT


def SlowChaos(surface, lastDot, dotF, dotS, dotT, iteration, lastTriangleRandomDot):


    # pygame.draw.line(surface, [0,0,0], lastDot, lastTriangleRandomDot)
    if(iteration != 0):
        y = random.randint(1, 3)
        if y == 1:
            triangleRandomDot = dotF
        elif y == 2:
            triangleRandomDot = dotS
        elif y == 3:
            triangleRandomDot = dotT
        
        dot = [ (lastDot[0]+triangleRandomDot[0]) / 2, (lastDot[1]+triangleRandomDot[1]) / 2]
        lastTriangleRandomDot = triangleRandomDot
        pygame.draw.line(surface, [0,255,255], lastDot, triangleRandomDot)
        pygame.draw.circle(surface,[255,255,0],dot,1)
        SlowChaos(surface, dot, dotF, dotS, dotT, iteration-1,triangleRandomDot)



def distance(x,y,dotT):
    return (x-dotT[0])**2 + (y-dotT[1])**2
    
    
def colorOnX(x,y, dotS, dotT):
    minX = dotT[0]
    maxX = dotS[0]
    leftColor = [255,0,0]
    rightColor = [0,255,0]

    color = [int(leftColor[i] + (rightColor[i] - leftColor[i]) / (maxX - minX) * (x - minX)) for i in range(3)]

    return color

def colorInCirlce(x,y,dotF, dotS, dotT):
    minX = 0
    maxX = (dotS[0] - dotT[0])**2
    rightColor = [255, 255, 0]
    leftColor = [0, 0, 255]

    color = [int(leftColor[i] + (rightColor[i] - leftColor[i]) / (maxX - minX) * (distance(x,y,dotS) - minX)) for i in range(3)]
 
    return color


def colorWithThreeVertex(x,y,dotF, dotS, dotT):
    maxDist = (dotS[0] - dotT[0])**2
    colorF = [255, 0, 0]
    colorS = [0, 255, 0]
    colorT = [0, 0, 255]
    distF = distance(x,y,dotF)
    distS = distance(x,y,dotS)
    distT = distance(x,y,dotT)

    w1 = distF  / maxDist
    w2 = distS  / maxDist
    w3 = distT  / maxDist
    W = w1 + w2 +w3
    w1 = w1 / W
    w2 = w2 / W     
    w3 = w3 / W
    color = [ w1 * colorF[i] + w2 * colorS[i]  + w3 * colorT[i]      for i in range(3)]
    return color


def fastChaos(surface, lastDot, dotF, dotS, dotT ):


        y = random.randint(1, 3)
        if y == 1:
            triangleRandomDot = dotF
        elif y == 2:
            triangleRandomDot = dotS
        elif y == 3:
            triangleRandomDot = dotT
        
        dot = [ (lastDot[0]+triangleRandomDot[0]) / 2, (lastDot[1]+triangleRandomDot[1]) / 2]


        pygame.draw.circle(surface,colorWithThreeVertex(dot[0],dot[1],dotF, dotS, dotT),dot,1)
        return dot




iteration = 100000
triangleSize = 750
lauched = True
taille = (1920,1080) 
screen = pygame.display.set_mode(taille) 

listOfDots = makeTheFirstTriangle(screen,triangleSize)
lastDot =  listOfDots[0]

for i in range (iteration):
    lastDot = fastChaos(screen,lastDot,listOfDots[0] ,listOfDots[1], listOfDots[2])

while lauched:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched=False


    pygame.display.update()



    # createARandomDotInsideATriangle(screen,listOfDots[0], listOfDots[1], listOfDots[2])