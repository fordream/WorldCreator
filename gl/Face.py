import pygame

class face:
    def __init__(self,color,poslist):
        self.color = color
        self.poslist = poslist
    def render(surf,cam):
        for pos in self.poslist:
            z = pos[2]

            del pos[2]

            pos[0] -= z + cam.pos[0]
            pos[1] -= z + cam.pos[1]
        pygame.draw.polygon(surf,self.color,self.poslist)
