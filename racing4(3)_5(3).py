import pygame,math
pygame.init()
from pygame.math import Vector2
screen = pygame.display.set_mode((1400, 900))
clock = pygame.time.Clock()

car1=pygame.image.load('car6.png')
angle1=0
x0,y0=720,390

car2=pygame.image.load('car4.png')
angle2=0
u0,v0=210,390

font = pygame.font.Font('freesansbold.ttf', 40)
text = font.render('Self-Driving Cars', True, 'red')

border=[0]*5
images=['img01.png','img1.png','img1.png','img1.png','img1.png']

for i in range(5):
    border[i]=pygame.image.load(images[i])
    
X=[400,100,700,700,100]
Y=[400,100,100,700,700]
x,y=0,-5

u,v=0,-5
v1=0

#y1=0
border_rect=[0]*5
Pos=[0]*5
for i in range (5):
    border_rect[i]=border[i].get_rect(center=(X[i],Y[i]))
    Pos[i]=Vector2(border_rect[i].center)
def turn():
    global x0,y0,x1,y1,CAR_pos
    x=(3*math.sin(3.14*angle1/180))
    y=(3*math.cos(3.14*angle1/180))
    CAR1=pygame.transform.rotate(car1,angle1)
    x0,y0=x0-x,y0-y
    x1,y1=x0,y0
    
def turn2():
    global u0,v0,u1,v1,CAR2_pos
    u=(3*math.sin(3.14*angle2/180))
    v=(3*math.cos(3.14*angle2/180))
    CAR2=pygame.transform.rotate(car2,angle2)
    u0,v0=u0-u,v0-v
    u1,v1=u0,v0
    u1=u0
    
while True:
    screen.fill((124,252,0))
    screen.blit(text,(900,450))
    for i in range (1,1):
        screen.blit(border[i],border_rect[i])
    screen.blit(border[0],border_rect[0])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    CAR1=pygame.transform.rotate(car1,angle1)
    CAR1_rect=CAR1.get_rect(center=(x0,y0))
    CAR1_pos=Vector2(CAR1_rect.center)
    screen.blit(CAR1,CAR1_rect)
    
    delta1=pygame.math.Vector2.length(Pos[1]-CAR1_pos)
    delta2=pygame.math.Vector2.length(Pos[2]-CAR1_pos)
    delta3=pygame.math.Vector2.length(Pos[3]-CAR1_pos)
    delta4=pygame.math.Vector2.length(Pos[4]-CAR1_pos)
    
    CAR2=pygame.transform.rotate(car2,angle2)
    CAR2_rect=CAR2.get_rect(center=(u0,v0))
    CAR2_pos=Vector2(CAR2_rect.center)
    screen.blit(CAR2,CAR2_rect)
    ddelta1=pygame.math.Vector2.length(Pos[1]-CAR2_pos)
    ddelta2=pygame.math.Vector2.length(Pos[2]-CAR2_pos)
    ddelta3=pygame.math.Vector2.length(Pos[3]-CAR2_pos)
    ddelta4=pygame.math.Vector2.length(Pos[4]-CAR2_pos)  
    
    
    if angle1==0:
        y0=y0-5
        
    if angle2==0:                             #1
        v0=v0-5
#-----------------------------------------------------------------
    if abs(delta2)<50:
        if angle1>=0 and angle1<90:
            angle1=angle1+10
            turn()
    if angle1==90:
        x0=x0-5
        y0=y1
        
    if abs(ddelta1)<190:                        #2
        if angle2>-90 and angle2<=0:
            angle2=angle2-10
            turn2()

    if angle2==-90: u0,v0=u0+5,v1
#--------------------------------------------------------------
    if abs(delta1)<50:
        if angle1>=90 and angle1<180:
            angle1=int(angle1+10)
            turn()
    if angle1==180:
        y0=y0+5
        x0=x1
        
    if abs(ddelta2)<190:                        #3
        if angle2>-180 and angle2<=-90:
            angle2=int(angle2-10)
            turn2()
    if angle2==-180: v0,u0=v0+5,u1
#--------------------------------------------------------------
    if abs(delta4)<50:
        if angle1>=180 and angle1<270:
            angle1=angle1+10
            turn()
    if angle1==270:
        x0=x0+5
        y0=y1
        
    if abs(ddelta3)<190:                        #4
        if angle2>-270 and angle2<=-180:
            angle2=angle2-10
            turn2()
    if angle2==-270: u0,v0=u0-5,v1
#--------------------------------------------------
    if abs(delta3)<50:
        if angle1>=270 and angle1<360:
            angle1=angle1+10
            turn()
    if angle1==360:
        angle1=0
        y0=y0-5
        x0=x1
        
    if abs(ddelta4)<190:                         #5
        if angle2>-360 and angle2<=-270:
            angle2=(angle2-10)
            turn2()
    if angle2==-360:
        angle2=0
#-----------------------------------------------------------
    pygame.display.flip()
    clock.tick(200)            
#------------------------------------------------------------
