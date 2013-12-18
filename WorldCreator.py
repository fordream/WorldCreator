import pygame

pygame.init()

screen = pygame.display.set_mode([640,480])
screen.fill([255,0,0])
pygame.display.set_caption("WorldCreator")
flip = pygame.display.flip
blit = screen.blit
load = pygame.image.load
fill = screen.fill

def title():
    w = load("font/w.png")
    o = load("font/o.png")
    r = load("font/r.png")
    l = load("font/l.png")
    d = load("font/d.png")
    c = load("font/c.png")
    e = load("font/e.png")
    a = load("font/a.png")
    t = load("font/t.png")
    s = load("font/s.png")

    pygame.draw.rect(screen,[0,255,0],[54,290,244,52])
    pygame.draw.rect(screen,[0,0,0],[54,290,244,52],4)
    
    blit(w,[64,100])
    blit(o,[112,100])
    blit(r,[160,100])
    blit(l,[208,100])
    blit(d,[256,100])
    blit(c,[64,150])
    blit(r,[112,150])
    blit(e,[160,150])
    blit(a,[208,150])
    blit(t,[256,150])
    blit(o,[304,150])
    blit(r,[352,150])
    blit(s,[64,300])
    blit(t,[112,300])
    blit(a,[160,300])
    blit(r,[208,300])
    blit(t,[256,300])

    
    
run = True
quittitlescreen = False

title()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
            quittitlescreen = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if pos[0] > 53:
                if pos[0] < 299:
                    if pos[1] > 289:
                        if pos[1] < 343:
                            run = False
                            quittitlescreen = True
    flip()
        

if quittitlescreen == True:
    pygame.quit()
