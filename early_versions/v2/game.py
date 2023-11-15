import pygame
import sys
import os
import random

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("The game")

dir=os.path.dirname(__file__)
image_path=os.path.join(dir,"resources","image","car.png")
image_car=pygame.image.load(image_path)
image_car=pygame.transform.scale(image_car,(90,140))
image_path=os.path.join(dir,"resources","image","grassland.png")
image_grassland=pygame.image.load(image_path)
image_path=os.path.join(dir,"resources","image","Road.png")
image_road=pygame.image.load(image_path)
image_path=os.path.join(dir,"resources","image","Sky.png")
image_Sky=pygame.image.load(image_path)
image_path=os.path.join(dir,"resources","image","Sky.png")
image_Sky=pygame.image.load(image_path)
image_path=os.path.join(dir,"resources","image","Tree.png")
image_Tree=pygame.image.load(image_path)
image_Tree=pygame.transform.scale(image_Tree,(100,140))
image_path=os.path.join(dir,"resources","image","car2.png")
image_car2=pygame.image.load(image_path)
image_car2=pygame.transform.scale(image_car2,(90,140))

white=(255,255,255)
red=(225,0,0)
blue=(0,0,225)
black=(0,0,0)
green=(0,150,0)
gray=(120,120,120)
yellow=(225,225,0)

car_w=90
car_h=140
car_x=800//2-car_w//2
car_y=(600-car_h)-20
car_speed=5
 
yline_w=20
yline_h=90
yline_x=(800-yline_w)//2
yline_y=150
tree_left_x_path=(0,50,100,150)
tree_right_x_path=(560,610,660,690)
tree_left_x=random.choice(tree_left_x_path)
tree_right_x=random.choice(tree_right_x_path)
tree_left_y=25
tree_right_y=25
text_x=50
text_y=200
grassland_y=-2400
grassland_speed=3
Sky_x=0

car2_x_path=(225+car_w/2,575-car_w*1.5)
car2_x=random.randint(225+car_w/2,575-car_w*1.5)
car2_y=100
car2_speed=6

clock=pygame.time.Clock()
font=pygame.font.Font(None,160)
text=font.render("GAME OVER",True,black)
stop=False

game_over=False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
    if   stop==True:
        yline_speed=0
        car2_speed=0
        car_speed=0
        grassland_speed=0

    elif  not car_x>210 or not car_x<590-car_w:
        yline_speed=6
        car2_speed=10
        grassland_speed=2
    
    else:
        yline_speed=8
        grassland_speed=7


    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]and car_x>0:
        car_x -=car_speed 
    if keys[pygame.K_RIGHT]and car_x<750:
        car_x +=car_speed

    screen.blit(image_grassland,(0,grassland_y))
    if  grassland_y>=-2400:
        grassland_y+=grassland_speed
    if  grassland_y>=0:
        grassland_y=-2400
    screen.blit(image_road,(225,grassland_y))
    if  grassland_y>=-2400:
        grassland_y+=grassland_speed
    if  grassland_y>0:
        grassland_y=-2400
    screen.blit(image_Sky,(Sky_x,0))
    if  Sky_x<=0:
        Sky_x -=0.5
    if  Sky_x<-1600:
        Sky_x=0
    pygame.draw.rect(screen,yellow,[yline_x,yline_y,20,90])
    if  yline_y>=150:
        yline_y +=yline_speed
    if  yline_y>600:
        yline_y=150




    screen.blit(image_Tree,(tree_left_x-20,tree_left_y))
    if  tree_left_y>=25:
        tree_left_y+=yline_speed
    if  tree_left_y>=random.randint(900,10000):
        tree_left_x=random.choice(tree_left_x_path)
        tree_left_y=25

    screen.blit(image_Tree,(tree_right_x-20,tree_right_y))
    if  tree_right_y>=25:
        tree_right_y+=yline_speed
    if  tree_right_y>=random.randint(600,10000):
        tree_right_x=random.choice(tree_right_x_path)
        tree_right_y=25

    screen.blit(image_car2,(car2_x,car2_y))
    if car2_y >= 100:
        car2_y += car2_speed
    if car2_y >= random.randint(1150,5000):
        car2_x = random.randint(225+car_w/2,575-car_w*1.5)
        car2_y =100


    if  car_x<=tree_left_x+50 and car_x+car_w>=tree_left_x and car_y<=tree_left_y+70 and car_y+car_h>tree_left_y:
        screen.blit(text,(text_x,text_y))
        stop=True
        if text_y<=600:
            text_y+=10
        if text_y>=600:
            event.type = pygame.QUIT   
    if  car_x<=tree_right_x+50 and car_x+car_w>=tree_right_x and car_y<=tree_right_y+70 and car_y+car_h>tree_right_y:
        screen.blit(text,(text_x,text_y))
        stop=True
        if text_y<=600:
            text_y+=10
        if text_y>=600:
            event.type = pygame.QUIT
    
    if  car_x<=car2_x+75 and car_x+car_w>=car2_x+20 and car_y<=car2_y+120 and car_y+car_h>car2_y:
        screen.blit(text,(text_x,text_y))
        stop=True
        if text_y<=600:
            text_y+=10
        if text_y>=600:
            event.type = pygame.QUIT  

    

    screen.blit(image_car,(car_x,car_y))

    pygame.display.update() 
    
    clock.tick(60)

pygame.quit()
sys.exit()