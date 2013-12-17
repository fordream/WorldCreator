# This is... AwesomeGL 1.0!
# Made to work with pygame.

'''
    A     W       W EEEEEEE  SSSSS   OOOOO
   A A    W       W E       S       O     O
  AAAAA   W   W   W EEEEEEE  SSSSS  O     O
 A     A   W W W W  E             S O     O
A       A   W   W   EEEEEEE  SSSSS   OOOOO


'''
import pygame, math

class Camera:
    def __init__(self,pos=[0,0,0],face=[0,0]):
        self.pos = pos
        self.face = face
    def cam(self):
        return [self.pos,self.face]
    

class obj:
    def __init__(self,pos,faces):
        self.pos = pos
        self.faces = faces
    def render(self,cam):
        canrender = False
        
        if self.pos[0] < cam[0][0]+10000:
            if self.pos[1] < cam[0][1]+10000:
                if self.pos[1] < cam[0][2]+10000:
                    canrender = True
