import pygame
import random

screenWidth = 1200
screenHeight = 1200
displaySurface = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("AI Dots")
clock = pygame.time.Clock()
run = True
fps = 10
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
black = [0,0,0]

windSpeed = 2
dotsList = []
numberOfDots = 500
dotGoodDirectionGene = []

class dots(object):
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.xSpeed = 0
        self.ySpeed = 0
        self.xSpeedAverage = 0
        self.ySpeedAverage = 0
        self.steps = 0
    def draw(self):
        pygame.draw.circle(displaySurface, self.color, (self.x, self.y), self.radius)
    def move(self):
        if (self.xSpeed < 3 and self.ySpeed < 3) and (self.xSpeed > -3 and self.ySpeed > -3):
            self.xSpeed = random.randrange(-10,10)
            self.ySpeed = random.randrange(-10,10)
        self.x += self.xSpeed
        self.y += self.ySpeed 

def redrawGameWindow():
    displaySurface.fill(white)
    goal.draw()
    for dot in dotsList:
        dot.draw()
    pygame.display.update()
def createFirstGeneration():
    while len(dotsList) < numberOfDots:
        dotsList.append(dots(300, 550, black, 3))
    for dot in dotsList:
        dot.xSpeed = random.randrange(-10, 10)
        dot.ySpeed = random.randrange(-10, 10)
        if dot.xSpeed == 0 or dot.ySpeed == 0:
            dot.xSpeed += 10
            dot.ySpeed += 10
def createGeneration():
    if len(dotGoodDirectionGene) >= 10:
        while len(dotsList) < numberOfDots:
            dotsList.append(dots(300, 550, black, 3))
        for dot in dotsList:
            dot.xSpeed, dot.ySpeed = dotGoodDirectionGene[random.randrange(0,len(dotGoodDirectionGene))]
    else:
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        dotGoodDirectionGene.append((random.randrange(-5,5),random.randrange(-5,5)))
        for element in dotGoodDirectionGene:
            if (element [1] < 1 and element[1] > -1) and (element [0] < 1 and element[0] > -1):
                dotGoodDirectionGene.pop(dotGoodDirectionGene.index(element))
        while len(dotsList) < numberOfDots:
            dotsList.append(dots(300, 550, black, 3))
        for dot in dotsList:
            dot.xSpeed, dot.ySpeed = dotGoodDirectionGene[random.randrange(0,len(dotGoodDirectionGene))] 
goal = dots(random.randrange(0,600),random.randrange(0,600), red, 20)
createFirstGeneration ()

while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        fps += 1
    if keys[pygame.K_DOWN]:
        fps -= 1
    for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    run = False
    for dot in dotsList:
        if (dot.steps>20 and dot.steps<60) or random.randrange(-90,3):    # wind
            dot.x += windSpeed + random.randrange(-1,2)
        else:
            dot.x -= windSpeed + random.randrange(-1,2)

        if dot.x >= screenWidth or dot.x <= 0 or dot.y >= screenHeight or dot.y <= 0:    
            for element in dotGoodDirectionGene:
                if element == (dot.xSpeed,dot.ySpeed) and len(dotGoodDirectionGene)>1:
                    dotGoodDirectionGene.pop(dotGoodDirectionGene.index(element))
            dotsList.pop(dotsList.index(dot))
        if ((goal.x + goal.radius) > dot.x and (goal.x - goal.radius) < dot.x) and ((goal.y + goal.radius) > dot.y and (goal.y - goal.radius) < dot.y):
            dotGoodDirectionGene.append((dot.xSpeedAverage//dot.steps,dot.ySpeedAverage//dot.steps))
            dotsList.pop(dotsList.index(dot))
        else:
            dot.xSpeedAverage += dot.xSpeed
            dot.ySpeedAverage += dot.ySpeed
            dot.steps += 1
            dot.move()

        if len(dotsList) <= 0:
            if len(dotGoodDirectionGene):
                createGeneration()
            else:
                createFirstGeneration() 
    redrawGameWindow()
    clock.tick(fps)

pygame.quit()