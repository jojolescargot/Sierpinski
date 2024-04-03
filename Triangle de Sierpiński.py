import pygame
from cmath import pi
from cmath import cos, sin
import math
import random
pygame.init()

def drawTriangle( surface, Dot_f,  Dot_s,  Dot_t,  Iteration):


    if Iteration != 0:

        pointF =  [(Dot_f[0]+Dot_s[0]) / 2, (Dot_f[1]+Dot_s[1]) / 2]
        pointS =  [(Dot_s[0]+Dot_t[0]) / 2, (Dot_s[1]+Dot_t[1]) / 2]
        pointT =  [(Dot_t[0]+Dot_f[0]) / 2, (Dot_t[1]+Dot_f[1]) / 2]
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pygame.draw.line(surface, [r,g,b], tuple(pointF), tuple(pointS))
        pygame.draw.line(surface, [r,g,b], tuple(pointS), tuple(pointT))
        pygame.draw.line(surface, [r,g,b], tuple(pointT), tuple(pointF))

        Iteration -= 1

        drawTriangle(surface,Dot_f,pointF,pointT,Iteration)

        drawTriangle(surface,pointF,Dot_s,pointS,Iteration)

        drawTriangle(surface,pointT,pointS,Dot_t,Iteration)
        pygame.display.update()
        return


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




iteration = 10
triangleSize = 750
lauched = True
taille = (1920,1080)
screen = pygame.display.set_mode(taille) 

listOfDots = makeTheFirstTriangle(screen,triangleSize)
drawTriangle(screen,listOfDots[0], listOfDots[1], listOfDots[2], iteration)

while lauched:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched=False


    pygame.display.update()