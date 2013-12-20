import pygame

class face:
    def __init__(self,color,poslist):
        self.color = color
        self.poslist = poslist
    def render(surf,cam):
        for pos in self.poslist:
            z = pos[2]

            del pos[2]

            pos[0] = 640-pos[0] + cam.pos
        pygame.draw.polygon(surf,self.color,self.poslist)
