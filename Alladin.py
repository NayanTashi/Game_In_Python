import pygame,random
import sys,time
from pygame.locals import *
pygame.init()
mario=pygame.image.load("ald.png")
background=pygame.image.load("sky.png")

aladdin=pygame.image.load("ald.png")
eagle=pygame.image.load("eagle.png")
lamp=pygame.image.load("lamp.png")
width=1024
height=700
blue=(77,98,3)
screen=pygame.display.set_mode((width,height),0,32)
y=0
red=(255,0,0)
clock=pygame.time.Clock()

x=0
z=0
x1=0
y1=0
fps=25
smallfont =pygame.font.SysFont('timesnewroman',30)
mediumfont =pygame.font.SysFont('timesnewroman',50)
largefont =pygame.font.SysFont('timesnewroman',80)

def scoreboard(score):
     sc=mediumfont.render("score board:"+str(score),True,blue)
     screen.blit(sc,(50,50))
     pygame.display.update()


def message_to_screen(msg,color,ydisp=0,size="small"):
    textSurf,textRect=object_text(msg,color,size)
    textRect.center=(width/2),(height/2)+ydisp
    screen.blit(textSurf,textRect)
def object_text(msg,color,size):
    if size=="small":
    
        textSurface=smallfont.render(msg,True,color)
        return textSurface,textSurface.get_rect()
    elif size=="medium":
        textSurface=mediumfont.render(msg,True,color)
        return textSurface,textSurface.get_rect()
    elif size=="large":
        textSurface=largefont.render(msg,True,color)
        return textSurface,textSurface.get_rect()   


def gameloop():
    curimg=1
    score=0
    gameover=False
    backg=background
    lop=False
    global x1
    global y1
    x2=0
    y2=0
    x=0
    randx=width   
    randy=50
    lx=random.randrange(30,width-30)
    ly=random.randrange(30,height-30)
    while not lop:
        while gameover==True:
            message_to_screen("Game over",red,-50,size="large")
            message_to_screen("press c to continue q to quit",red,80,size="medium")
            
            pygame.display.update()
            
            for event in pygame.event.get():
                 if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_q:
                         lop=True
                         gameover==False
                         pygame.quit()
                         quit
                     if event.key==pygame.K_c:
                         x1=0
                         y1=0
                         gameloop()
                         
            
        
        
        if randx<0:
            randy=random.randrange(0,height)
            randx=width
        randx1=0
        
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
               lop=True
               pygame.quit()
                
           if event.type==pygame.KEYDOWN:
              randx1 -=60
              if event.key==pygame.K_LEFT:
                   x2 =-10
                   x =-50
                   randx1 -=60
              elif event.key==pygame.K_RIGHT:
                    x2 =+10
                    x=-50
                    randx1 -=60
              elif event.key==pygame.K_UP:
                    randx1 -=60
                    x=-50
                    y2=-10
              elif event.key==pygame.K_DOWN:
                        randx1 -=60
                        y2=+10
                        x=-50
        x1 +=x2
        y1 +=y2
        randx +=randx1
        ##randy +=randy1
        if randx-50 in range(x1-50,x1+50) and randy in range(y1-40,y1+40):
           message_to_screen("Game over",red,-50,size="large")
           gameover=True
           
            
           pygame.display.update()
        if x1>width or x1<0 or y1>height or y1<0:
            message_to_screen("Game over",red,-50,size="large")
            gameover=True
            
            pygame.display.update()
        if x1+10 in range(lx-70,lx+70) and y1-10 in range(ly-40,ly+40):
            lx=random.randrange(20,width-30)
            ly=random.randrange(20,height-30)
            score +=1
         
            
                   
        screen.blit(backg,(0,0))
        screen.blit(lamp,(lx,ly))
        screen.blit(aladdin,(x1,y1))
        screen.blit(eagle,(randx,randy))
        scoreboard(score)
        pygame.display.update()
        clock.tick(fps)

gameloop()
                            

                           
                            
                   






