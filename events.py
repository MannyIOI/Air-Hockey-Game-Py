import pygame

def moveup(shape,event):
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP:
            # print("here")
            if shape.dPos[1] < -0.1:
                shape.dPos += [0,0.1]
                # s.sendto(shape.dPos,server)

                
def movedown(shape,event):
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_DOWN:
            if shape.dPos[1] > -0.5:
                shape.dPos+=[0,-0.1]
                

def moveright(shape,event):
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            shape.dPos+=[0.1,0]
            # s.send(shape.dPos)

            
def moveleft(shape,event):
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            shape.dPos+=[-0.1,0]
            # s.send(shape.dPos)
            # print(s)


            
