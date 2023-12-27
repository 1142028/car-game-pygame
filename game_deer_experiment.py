import pygame
import sys
import os
import random
import time

pygame.init()

screen=pygame.display.set_mode((800,900))
pygame.display.set_caption("The game")

dir=os.path.dirname(__file__)
image_files={
    "car.png": (90, 140),
    "car_R.png": (90, 140),
    "car_L.png": (90, 140),
    "spring_road.png": None,       
    "winter_road.png": None,     
    "autumn_road.png": None,     
    "spring_night_road.png": None,       
    "winter_night_road.png": None,     
    "autumn_night_road.png": None,
    "spring_tree.png": (150, 210),
    "autumn_tree.png": (150, 210),
    "winter_tree.png": (150, 210),
    "spring_night_tree.png": (150, 210),
    "autumn_night_tree.png": (150, 210),
    "winter_night_tree.png": (150, 210),
    "car2.png": (90, 140)
    }
images={}
for name,size in image_files.items():
    image_path=os.path.join(dir,'resources','image',name)
    image=pygame.image.load(image_path)
    if size:
        image = pygame.transform.scale(image, size)
    images[name.split('.')[0]] = image

image_car = images["car"]
image_road = images["spring_road"]
image_Tree = images["spring_tree"]
image_car2 = images["car2"]

def spring():
    global image_Tree,image_road,season
    image_Tree=images["spring_tree"]
    image_road = images["spring_road"]
    season=spring
def autumn():
    global image_Tree,image_road,season
    image_Tree=images["autumn_tree"]
    image_road = images["autumn_road"]
    season=autumn
def winter():
    global image_Tree,image_road,season
    image_Tree=images["winter_tree"]
    image_road = images["winter_road"]
    season=winter

def day():
    global image_road,image_Tree,Time
    if season==spring:
        image_road=images["spring_road"]
        image_Tree=images["spring_tree"]
    if season==winter:
        image_road=images["winter_road"]
        image_Tree=images["winter_tree"]
    if season==autumn:
        image_road=images["autumn_road"]
        image_Tree=images["autumn_tree"]
    Time=day

def night():
    global image_road,image_Tree,Time
    if season==spring:
        image_road=images["spring_night_road"]
        image_Tree=images["spring_night_tree"]
    if season==winter:
        image_road=images["winter_night_road"]
        image_Tree=images["winter_night_tree"]
    if season==autumn:
        image_road=images["autumn_night_road"]
        image_Tree=images["autumn_night_tree"]
    Time=night
 

deer=[pygame.transform.scale(pygame.image.load(os.path.join(dir,'resources','image','deer',f'deer ({i}).png')) ,(200,200)) for i in range(1, 12)]
def Deer():
    global deer_index, deer_start, deer_x, deer_y, deer_last_update_time
    deer_index = 0
    deer_start = True
    deer_x = -100
    deer_y = random.choice(range(0, 500))
    deer_last_update_time = pygame.time.get_ticks()

    while deer_start:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                deer_start = False

  
        screen.blit(image_road, (0, road_y))
        pygame.draw.rect(screen, yellow, [yline_x, yline_y, 20, 90])
        screen.blit(image_Tree, (tree_left_x - 20, tree_left_y))
        screen.blit(image_Tree, (tree_right_x - 20, tree_right_y))
        screen.blit(image_car2, (car2_x, car2_y))
        screen.blit(image_car, (car_x, car_y))


        screen.blit(deer[deer_index], (deer_x, deer_y))

        pygame.display.flip()

        if current_time - deer_last_update_time >= 100:
            deer_index += 1
            deer_x += 10
            deer_last_update_time = current_time

        clock.tick(60)

        if deer_index >= len(deer):
            deer_index=0
        if deer_x>=800:
            deer_start=False    


anime=[pygame.transform.scale(pygame.image.load(os.path.join(dir,'resources','animation',f'anime ({i}).png')) ,(800,600)) for i in range(1, 32)]
def animation():
    anime_start=True
    anime_index=0
    while anime_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                anime_start=False
        screen.blit(anime[anime_index], (0, 150))
        pygame.display.flip()
        clock.tick(15)
        anime_index+= 1
        if anime_index >= len(anime):
            anime_start=False
    time.sleep(0.5 )

gameover=[pygame.transform.scale(pygame.image.load(os.path.join(dir,'resources','image','gameover',f'gameover ({i}).png')) ,(800,600)) for i in range(1, 21)]
def over_animation():
    over_start=True
    over_index=0
    while over_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over_start=False
        screen.blit(gameover[over_index], (0, 150))
        pygame.display.flip()
        clock.tick(15)
        over_index+= 1
        if over_index >= len(gameover):
            over_start=False
    time.sleep(0.5 )

def reset_game():
    global car_x, car_y, yline_x, yline_y, tree_left_x, tree_right_x, tree_left_y, tree_right_y
    global road_y,image_car, car2_x, car2_y, text_x, text_y, score 
    boom()

    image_car=images["car"]
    car_x=800//2-car_w//2
    car_y=(900-car_h)-20
    yline_x=(800-yline_w)//2
    yline_y=-150
    tree_left_x=random.choice(tree_left_x_path)
    tree_right_x=random.choice(tree_right_x_path)
    tree_left_y=-210
    tree_right_y=-210
    road_y=-2000
    car2_x=random.randint(225+car_w/2,575-car_w*1.5)
    car2_y=-200
    text_x=50
    text_y=200
    score=-60

Boom=[pygame.transform.scale(pygame.image.load(os.path.join(dir,'resources','image',f'bone({i}).png')) ,(250,250)) for i in range(1,8)]
def boom():
    boom_start=True
    boom_index=0
    while boom_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boom_start=False
        screen.blit(Boom[boom_index], (car_x-70, car_y-70))
        pygame.display.flip()
        clock.tick(5)
        boom_index+= 1
        if boom_index >= len(Boom):
            boom_start=False
        
def season_change():
    global season_score
    if season_score>=1000:
        season_score=0
        if season==spring:
            autumn()
        elif season==autumn:
            winter()
        else:
            spring()

def replacement():
    global Time_score
    if Time_score>=500:
        Time_score=0
        if Time==day:
            night()
        elif Time==night:
            day()

white=(255,255,255)
red=(225,0,0)
blue=(0,0,225)
black=(0,0,0)
green=(0,150,0)
gray=(120,120,120)
yellow=(225,225,0)
shadow_color = (50, 50, 50)
highlight_color = (255, 255, 255)

car_w=90
car_h=140
car_x=800//2-car_w//2
car_y=(900-car_h)-50
 
yline_w=20
yline_h=200
yline_x=(800-yline_w)//2
yline_y=-150

tree_left_x_path=(0,50,100,150)
tree_right_x_path=(560,610,660,690)
tree_left_x=random.choice(tree_left_x_path)
tree_right_x=random.choice(tree_right_x_path)
tree_left_y=-25
tree_right_y=-25

road_y=-2000


car2_x_path=(225+car_w/2,575-car_w*1.5)
car2_x=random.randint(225+car_w/2,575-car_w*1.5)
car2_y=-200

font=pygame.font.Font(None,100)
font2=pygame.font.Font(None,40)
font3=pygame.font.Font(None,60)
text=font.render("click space can reset",True,black)
text_x=50
text_y=200

stop=False
clock=pygame.time.Clock()
score=-60
season_score=-60
Time_score=-60
last_score_update_time=time.time()


    

game_over=False
animation()
season=spring
Time=day
while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
    if   stop==True:
        yline_speed=0
        car2_speed=0
        car_speed=0
        road_speed=0
        if keys[pygame.K_SPACE]:
            reset_game()
            stop=False
    elif not car_x>200 or not car_x<600-car_w:
        yline_speed=6*2
        car2_speed=15
        road_speed=yline_speed
        car_speed=3*2
    elif   score<0:
        yline_speed=0
        car2_speed=0
        car_speed=0
        road_speed=0
    else:
        yline_speed=10*2
        road_speed=yline_speed
        car2_speed=13
        car_speed=7*2
        image_car=images["car"]


    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]and car_x>0:
        car_x -=car_speed 
        image_car=images['car_L']
    if keys[pygame.K_RIGHT]and car_x<750:
        car_x +=car_speed
        image_car=images['car_R']
    


    screen.blit(image_road,(0,road_y))
    if  road_y>=-2000:
        road_y+=road_speed
    if  road_y>0:
        road_y=-2000
    pygame.draw.rect(screen,yellow,[yline_x,yline_y,yline_w,yline_h])
    if  yline_y>=-150:
        yline_y +=yline_speed
    if  yline_y>1000:
        yline_y=-150

    screen.blit(image_Tree,(tree_left_x-20,tree_left_y))
    if  tree_left_y>=-210:
        tree_left_y+=yline_speed
    if  tree_left_y>=random.randint(1000,10000):
        tree_left_x=random.choice(tree_left_x_path)
        tree_left_y=-210

    screen.blit(image_Tree,(tree_right_x-20,tree_right_y))
    if  tree_right_y>=-210:
        tree_right_y+=yline_speed
    if  tree_right_y>=random.randint(1000,10000):
        tree_right_x=random.choice(tree_right_x_path)
        tree_right_y=-210

    screen.blit(image_car2,(car2_x,car2_y))
    if car2_y >= -200:
        car2_y += car2_speed
    if car2_y >= random.randint(1150,5000):
        car2_x = random.randint(225+car_w/2,575-car_w*1.5)
        car2_y =-200

    current_time=time.time()
    if stop==True:
        current_time=0
    if current_time-last_score_update_time>=0.05:
        score+=1
        season_score+=1
        Time_score+=1
        last_score_update_time=current_time
        season_change()
        replacement()

    if not game_over and score>0:
        point=font2.render("points:"+str(score),True,black)
        screen.blit(point,(0,0))
    if score>500:
        text=font.render("You are awesome",True,black)
    
    
    if score <-40:
        start=font3.render("3",True,red)
        screen.blit(start,(400,300))
    elif score>-40 and score<-20:
        start=font3.render("2",True,red)
        screen.blit(start,(400,300))
    elif score>-20 and score<0:
        start=font3.render("1",True,red)
        screen.blit(start,(400,300))
    
    screen.blit(image_car,(car_x,car_y))

    if  car_x<=tree_left_x+75 and car_x+car_w>=tree_left_x and car_y<=tree_left_y+170 and car_y+car_h>tree_left_y:
        screen.blit(text,(text_x,text_y))
        stop=True       
        if text_y<=1000:
            text_y+=2
        if text_y>=1000:
            game_over=True
    if  car_x<=tree_right_x+70 and car_x+car_w>=tree_right_x+40 and car_y<=tree_right_y+170 and car_y+car_h>tree_right_y:
        screen.blit(text,(text_x,text_y))
        stop=True
        if text_y<=1000:
            text_y+=2
        if text_y>=1000:
            game_over=True
    elif    car_x<=car2_x+75 and car_x+car_w>=car2_x+20 and car_y<=car2_y+120 and car_y+car_h>car2_y:
        screen.blit(text,(text_x,text_y))
        stop=True
        if text_y<=1000:
            text_y+=2
        if text_y>=1000:
            game_over=True
               



    pygame.display.flip()
    pygame.time.Clock().tick(500)
    pygame.display.update() 
    clock.tick(60)

over_animation()
pygame.quit()
sys.exit()