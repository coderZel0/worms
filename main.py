import pygame

from rocket import Rocket
from population import Population


pygame.init()
rockets= []
screen = pygame.display.set_mode((600,600))


for _ in range(10):
    rockets.append(Rocket(300,500))

population = Population()    
#Font
font = pygame.font.Font('font.ttf', 20)
generationFont =font.render(str(population.generation),False,(255,255,255))
genRect = generationFont.get_rect(center=(10,10))

while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    generationFont =font.render("Generation: "+str(population.generation),False,(255,255,255))        
    screen.blit(generationFont,genRect)
    population.start(screen)
    population.evaluate()
    pygame.time.Clock().tick(60)
    pygame.display.flip()        