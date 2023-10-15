import pygame
import sys
import os

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("The game")

dir=os.path.dirname(__file__)
image_path=os.path.join(dir,"resources\image\car.png")
image_car=pygame.image.load(image_path)
image_car=pygame.transform.scale(image_car,(90,140))
image_path=os.path.join(dir,"resources\image\grassland.png")
image_grassland=pygame.image.load(image_path)
image_path=os.path.join(dir,"resources\image\Road.png")
image_road=pygame.image.load(image_path)
image_path=os.path.join(dir,"resources\image\Sky.png")
image_Sky=pygame.image.load(image_path)


white=(255,255,255)
red=(225,0,0)
blue=(0,0,225)
black=(0,0,0)
green=(0,150,0)
gray=(120,120,120)
yellow=(225,225,0)

car_w=50
car_h=100
car_x=(800-car_w)//2
car_y=(600-car_h)-20
car_speed=2
 
yline_w=20
yline_h=90
yline_x=(800-yline_w)//2
yline_y=150
grassland_y=-1200
Sky_x=0
yline_speed=3


clock=pygame.time.Clock()

game_over=False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True


    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]and car_x>0:
        car_x -=car_speed 
    if keys[pygame.K_RIGHT]and car_x<750:
        car_x +=car_speed
    
    
    screen.blit(image_grassland,(0,grassland_y))
    if  grassland_y>=-1200:
        grassland_y+=yline_speed
    if  grassland_y>=500:
        grassland_y=-1200
    screen.blit(image_road,(225,grassland_y))
    if  grassland_y>=-1200:
        grassland_y+=yline_speed
    if  grassland_y>200:
        grassland_y=-1200
    screen.blit(image_Sky,(Sky_x,0))
    if  Sky_x<=0:
        Sky_x -=0.5
    if  Sky_x<-224:
        Sky_x=0
    pygame.draw.rect(screen,yellow,[yline_x,yline_y,20,90])
    if  yline_y>=150:
        yline_y +=yline_speed
    if  yline_y>600:
        yline_y=150

    screen.blit(image_car,(car_x-21,car_y-40))
    
    pygame.display.update() 

    clock.tick(144)

pygame.quit()
sys.exit()

    
pygame.display.update() 

clock.tick(144)

pygame.quit()
sys.exit()