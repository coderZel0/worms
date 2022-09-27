from rocket import Rocket
import random

class Population:
    def __init__(self):
        self.population = []
        self.matingPool = []
        self.generation = 1
        self.avgFitness = 0
        self.maxFitness = 0
        self.setPopulation()
    def setPopulation(self):
        for _ in range(20): 
            self.population.append(Rocket(300,500)) 
    def evaluate(self):
        count =0
        for rocket in self.population:
            if rocket.done:
                count +=1
                if self.maxFitness<rocket.fitness:
                    self.maxFitness = rocket.fitness
        if count == len(self.population):
            for rocket in self.population:
                self.matingPool.extend([rocket for i in range(self.matingChance(rocket))])
            newPop = []
            for _ in range(len(self.population)):    
                parX = self.randomParent()
                parY = self.randomParent()
                newPop.append(self.getChild(parX,parY))
            self.population = newPop  
            self.generation +=1
            self.maxFitness = 0
            self.avgFitness = 0  

    def matingChance(self,rocket):
        return int(rocket.fitness//self.maxFitness)
    def getChild(self,parentX,parentY):
        genes = [parentX.dna.genes[i] for i in range(len(parentX.dna.genes)//2)] +  [parentY.dna.genes[i] for i in range(len(parentY.dna.genes)//2)]
        child = Rocket(300,500)
        child.dna.genes = genes
        return child
    def randomParent(self):
        return self.matingPool[random.randint(0,len(self.matingPool)-1)]    
    def start(self,surface):
        for rocket in self.population:
            rocket.render(surface)