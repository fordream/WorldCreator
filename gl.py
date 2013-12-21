import pygame

class Cube:
    def __init__(self,size,color,pos):
        self.color = color
        self.size = size
        self.pos = pos
    def render(self,surf):
        print self.size
        print self.pos
        
        pygame.draw.rect(surf,self.color,[self.pos[0],self.pos[1],self.size,self.size])

        pygame.draw.polygon(surf,self.color,[self.pos,[self.pos[0]-self.size/4,self.pos[1]-self.pos[1]/4],[self.pos[0]+self.size+self.size/4,self.pos[1]-self.pos[1]/4],[self.pos[0]+self.size,self.pos[1]]])

        pygame.draw.polygon(surf,self.color,[[self.pos[0]+self.size,self.pos[1]+self.pos[1]],[self.pos[0]+self.size+self.size/4,self.pos[1]-self.size/4],[self.pos[0]+self.size+self.size/4,self.pos[1]+self.size-self.size/4],[self.pos[0]+self.size,self.pos[1]+self.size]])
