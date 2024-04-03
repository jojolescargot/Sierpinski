import numpy as np
import pygame

pygame.init()

def generatePascalTriangle(numRows):
    pascalTriangle = np.zeros((numRows, numRows), dtype=int)
    pascalTriangle[0, 0] = 1

    for i in range(1, numRows):
        for j in range(i + 1):
            if j == 0 or j == i:
                pascalTriangle[i, j] = 1
            else:
                pascalTriangle[i, j] = pascalTriangle[i - 1, j - 1] + pascalTriangle[i - 1, j]

# def generatePascalTriangle(numRows):
#     triangle = [[1]]

#     for i in range(1, numRows):
#         row = [1]

#         for j in range(1, i):
#             value = triangle[i-1][j-1] + triangle[i-1][j]
#             row.append(value)

#         row.append(1)

#         triangle.append(row)

#     return triangle

def findNumberOfElement(listOfTheTriangle):
    numberOfElement = 0
    for i in range(len(listOfTheTriangle)):
        if listOfTheTriangle[i] == 0:
            return numberOfElement 
        else:
            numberOfElement += 1
    
def PascalTriangleToSierpinskyTriangle(surface,triangle):
    width, height = surface.get_size()
    shape_triangle = np.shape(triangle)
    print(shape_triangle)
    for i in range(shape_triangle[0] - 1):
        pygame.display.update()
        NumberOfElement = findNumberOfElement(triangle[i])
        for j in range(NumberOfElement):
            if triangle[i][j] % 2 != 0:
                pygame.draw.circle(surface,(255,255,255),(1/2*width - (NumberOfElement * reduction) / 2 + (j*reduction),i*reduction),1)


reduction = 1/100
lauched = True
taille = (1200,1080)
screen = pygame.display.set_mode(taille,pygame.FULLSCREEN) 

PascalTriangleToSierpinskyTriangle(screen, generatePascalTriangle(1000))

while lauched:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched=False


    pygame.display.update()