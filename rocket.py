import random
import pygame,math


class DNA:
    def __init__(self):
        self.genes = []
        self.setGenes()
    def setGenes(self):
        for i in range(15):
            x = random.randint(0,600)
            y= random.randint(0,600)
            vector = pygame.Vector2(x,y)
            self.genes.append(vector)

class Rocket:
    def __init__(self,x,y):
        self.dna = DNA()
        self.image = pygame.Surface((20,20))
        self.image.fill("green")
        self.pos = pygame.Vector2(x,y) 
        self.prevPos = self.pos
        self.rect = self.image.get_rect(topleft=(x,y))
        self.vel = (random.randint(0,1))+0.8 
        self.fitness = 0
        self.timer =0
        self.maxCount = random.randint(60,70)
        self.index =0
        self.done = False
        self.dir = pygame.Vector2(0)
        self.genrtor = self.getDir()
    def getDir(self):
        for item in self.dna.genes:
            yield item    
    def update(self):
        self.timer +=1
        if not self.done:
            if self.timer>self.maxCount:
                self.calcDir()
                self.timer =0  
        self.pos += self.vel * self.dir
        self.rect = self.pos
    def render(self,surface):
        self.update()
        surface.blit(self.image,self.rect)    
    def calcDir(self):
        #self.dir =pygame.Vector2(0)
        try:
            ePos = next(self.genrtor)
            self.dir= (ePos - self.pos).normalize()   
        except StopIteration:
            self.done = True
            self.fitness = 600 - self.rect.y
            self.dir = pygame.Vector2(0) 
            self.image.fill("red")    
        
    