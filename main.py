from time import sleep
import pygame;

#  ____   ____  _       _______     _____       _       ______   _____     ________   ______   
# |_  _| |_  _|/ \     |_   __ \   |_   _|     / \     |_   _ \ |_   _|   |_   __  |.' ____ \  
#   \ \   / / / _ \      | |__) |    | |      / _ \      | |_) |  | |       | |_ \_|| (___ \_| 
#    \ \ / / / ___ \     |  __ /     | |     / ___ \     |  __'.  | |   _   |  _| _  _.____`.  
#     \ ' /_/ /   \ \_  _| |  \ \_  _| |_  _/ /   \ \_  _| |__) |_| |__/ | _| |__/ || \____) | 
#      \_/|____| |____||____| |___||_____||____| |____||_______/|________||________| \______.' 


# TODO :  TITLE SCREEN    -> textbox    (centre le !!!)





pygame.mixer.init()
pygame.font.init()


#DEFINITION D'ECRAN
w,h = 900,900;
SCREEN = pygame.display.set_mode((w,h));
HIT = False


pacfont = pygame.font.Font("asset/pacfont.ttf",20)
titletext = pygame.font.Font.render(pacfont, "PAC-man",True,(255,255,0))
titlebox = pygame.Rect(w//7,h//2,500,200)
waka = pygame.mixer.Sound("asset/waka.mp3");
waka.set_volume(0.1)


#DEPLACEMENT
LEFT = False;
RIGHT = False;
UP = False;
DOWN = False;

#DEPLACEMENT J2
LEFT2 = False;
RIGHT2 = False;
UP2 = False;
DOWN2 = False;


#BACKGROUND
BG = pygame.image.load("asset/bg.png");
BG = pygame.transform.scale(BG,(w,h))
BG_hitbox = BG.get_rect();

#PACMANANIMATED
frame = 0
player = pygame.image.load("asset/2.png")
player = pygame.transform.scale(player,(40,40))
player_hitbox = player.get_rect();
player_hitbox.center = w//1.8,250

#PACMANANIMATED
player2 = pygame.image.load("asset/2.png")
player2 = pygame.transform.scale(player,(40,40))
player_hitbox2 = player.get_rect();
player_hitbox2.center = w//2.25,250

POINT = 0
pacgumHit = []
distance = 30

pacgumarray = [
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png"),
    pygame.image.load("asset/pg.png")
]

for each in range(len(pacgumarray)):
        if (each <=4):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//2.9+(each*70),h//2.65
        if (each > 4 and each <10):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//2.9+((each-5)*70),h//1.78
        if (each == 10):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//2.9,h//2.15
        if (each == 11):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//1.52,h//2.15
        if (each > 11 and each <25):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//50+((each-11.3)* 65),h//5.3
        if (each >24 and each < 33):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//50+((each-21.8)* 65),h//1.33
        if (each >32):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//4.1,h//4+(each-33)*65



intro = pygame.mixer.Sound("asset/intro.mp3")
intro.set_volume(0.3)
introtime = 0
wakatiming = 0

#     ______      _      ____    ____ ________  
#   .' ___  |    / \    |_   \  /   _|_   __  | 
#  / .'   \_|   / _ \     |   \/   |   | |_ \_| 
#  | |   ____  / ___ \    | |\  /| |   |  _| _  
#  \ `.___]  _/ /   \ \_ _| |_\/_| |_ _| |__/ | 
#   `._____.|____| |____|_____||_____|________| 
#                                                                                      

# intro.play()
while (True):    
    introtime +=1
    wakatiming += 1
    MOUSEX,MOUSEY = pygame.mouse.get_pos()

    if wakatiming == 300:
        wakatiming = 0
    frame +=1
    if frame <= 50:
        player = pygame.image.load("asset/2.png");
        player = pygame.transform.rotate(player,180)
        player = pygame.transform.scale(player,(40,40))
    if frame >50:
        player = pygame.image.load("asset/1.png")
        player = pygame.transform.rotate(player,180)
        player = pygame.transform.scale(player,(40,40))
    if frame == 100:
        frame = 0
    if frame <= 50:
        player2 = pygame.image.load("asset/2.png");
        player2 = pygame.transform.scale(player2,(40,40))
    if frame >50:
        player2 = pygame.image.load("asset/1.png")
        player2 = pygame.transform.scale(player2,(40,40))
    if frame == 100:
        frame = 0


#                                                                  _         
#                                                                 / |_       
#   _ .--..--.  .--.  __   _ _   __ .---. _ .--..--. .---. _ .--.`| |-.--.   
#  [ `.-. .-. / .'`\ [  | | [ \ [  / /__\[ `.-. .-. / /__\[ `.-. || |( (`\]  
#   | | | | | | \__. || \_/ |\ \/ /| \__.,| | | | | | \__.,| | | || |,`'.'.  
#  [___||__||__'.__.' '.__.'_/\__/  '.__.[___||__||__'.__.[___||__\__[\__) ) 
#                                         



    if (UP):
        player_hitbox.y -= 1
        if frame <= 30:
            player = pygame.image.load("asset/2.png");
        if frame >30:
            player = pygame.image.load("asset/1.png");
        player = pygame.transform.scale(player,(40,40))
        player = pygame.transform.rotate(player,90)
    if (DOWN):
        player_hitbox.y += 1
        if frame <= 30:
            player = pygame.image.load("asset/2.png");
        if frame >30:
            player = pygame.image.load("asset/1.png")
        player = pygame.transform.scale(player,(40,40))
        player = pygame.transform.rotate(player,-90)
    if (LEFT):
        player_hitbox.x -= 1
        if frame <= 30:
            player = pygame.image.load("asset/2.png");
        if frame >30:
            player = pygame.image.load("asset/1.png")
        player = pygame.transform.scale(player,(40,40))
        player = pygame.transform.rotate(player,180)
    if (RIGHT):
        player_hitbox.x += 1
        if frame <= 30:
            player = pygame.image.load("asset/2.png");
        if frame >30:
            player = pygame.image.load("asset/1.png")
        player = pygame.transform.scale(player,(40,40))


    if (UP or DOWN or LEFT or RIGHT):
        if wakatiming == 50:
            waka.play()


    if (UP2):
        player_hitbox2.y -= 1
        if frame <= 30:
            player2 = pygame.image.load("asset/2.png");
        if frame >30:
            player2 = pygame.image.load("asset/1.png")
        player2 = pygame.transform.scale(player2,(40,40))
        player2 = pygame.transform.rotate(player2,90)
    if (DOWN2):
        player_hitbox2.y += 1
        if frame <= 30:
            player2 = pygame.image.load("asset/2.png");
        if frame >30:
            player2 = pygame.image.load("asset/1.png")
        player2 = pygame.transform.scale(player2,(40,40))
        player2 = pygame.transform.rotate(player2,-90)
    if (LEFT2):
        player_hitbox2.x -= 1
        if frame <= 30:
            player2 = pygame.image.load("asset/2.png");
        if frame >30:
            player2 = pygame.image.load("asset/1.png")
        player2 = pygame.transform.scale(player2,(40,40))
        player2 = pygame.transform.rotate(player2,180)
    if (RIGHT2):
        player_hitbox2.x += 1
        if frame <= 30:
            player2 = pygame.image.load("asset/2.png");
        if frame >30:
            player2 = pygame.image.load("asset/1.png")
        player2 = pygame.transform.scale(player2,(40,40))

#                        _               __         
#                       / |_            [  |        
#   .---.  .--.  _ .--.`| |-_ .--.  .--. | | .--.   
#  / /'`\/ .'`\ [ `.-. || |[ `/'`\/ .'`\ | |( (`\]  
#  | \__.| \__. || | | || |,| |   | \__. | | `'.'.  
#  '.___.''.__.'[___||__\__[___]   '.__.[___[\__) ) 
#                                                   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_UP:
                UP = True
                DOWN = False
                LEFT = False
                RIGHT = False
            if event.key == pygame.K_DOWN:
                DOWN = True
                UP = False
                LEFT = False
                RIGHT = False
            if event.key == pygame.K_LEFT:
                LEFT = True
                RIGHT = False
                UP = False
                DOWN = False
            if event.key == pygame.K_RIGHT:
                RIGHT = True
                LEFT = False
                UP = False
                DOWN = False
            if event.key == pygame.K_z:
                UP2 = True
                DOWN2 = False
                LEFT2 = False
                RIGHT2 = False
            if event.key == pygame.K_s:
                DOWN2 = True
                UP2 = False
                LEFT2 = False
                RIGHT2 = False
            if event.key == pygame.K_q:
                LEFT2 = True
                RIGHT2 = False
                UP2 = False
                DOWN2 = False
            if event.key == pygame.K_d:
                RIGHT2 = True
                LEFT2 = False
                UP2 = False
                DOWN2 = False
            if event.key == pygame.K_SPACE:
                pygame.quit()

#               __  __   _         _                       
#              [  |[  | (_)       (_)                      
#   .---.  .--. | | | | __  .--.  __  .--.  _ .--.  .--.   
#  / /'`\/ .'`\ | | | |[  |( (`\][  / .'`\ [ `.-. |( (`\]  
#  | \__.| \__. | | | | | | `'.'. | | \__. || | | | `'.'.  
#  '.___.''.__.[___[___[___[\__) [___'.__.'[___||__[\__) )                            

    #TOP COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.centerx,player_hitbox.top -5))
    if colorb >= 100 and colorr <= 100:
        player_hitbox.y += 1
    #LEFT COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.left -5,player_hitbox.centery))
    if colorb >= 100 and colorr <= 100:
        player_hitbox.x += 1
    #RIGHT COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.right+5,player_hitbox.centery))
    if colorb >= 100 and colorr <= 100:
        player_hitbox.x -= 1
    #BOTTOM COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.centerx,player_hitbox.bottom +5))
    if colorb >= 100 and colorr <= 100:
        player_hitbox.y -= 1

    #PLAYER 2
    #TOP COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox2.centerx,player_hitbox2.top -5))
    if colorb >= 100 and colorr <= 100:
        player_hitbox2.y += 1
    #LEFT COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox2.left -5,player_hitbox2.centery))
    if colorb >= 100 and colorr <= 100:
        player_hitbox2.x += 1
    #RIGHT COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox2.right+5,player_hitbox2.centery))
    if colorb >= 100 and colorr <= 100:
        player_hitbox2.x -= 1
    #BOTTOM COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox2.centerx,player_hitbox2.bottom +5))
    if colorb >= 100 and colorr <= 100:
        player_hitbox2.y -= 1



    SCREEN.blit(BG, BG_hitbox)
    SCREEN.blit(player, player_hitbox)
    SCREEN.blit(player2, player_hitbox2)
    pygame.draw.rect(SCREEN,(255,255,255),titlebox,1)

    for each in range(len(pacgumarray)):
        SCREEN.blit(pacgumarray[each],pacgumHit[each])


    for each in range(len(pacgumarray)):
        if (player_hitbox.colliderect(pacgumHit[each])) or (player_hitbox2.colliderect(pacgumHit[each])):
            pacgumHit[each].x = 5000
            POINT +=1
            print(POINT)
    
    if (POINT == len(pacgumHit)):
        pygame.quit()


    if (introtime == 10):
        sleep(5)

    
    pygame.display.update()