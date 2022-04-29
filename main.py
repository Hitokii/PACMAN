from tkinter import ON
import pygame;
                                                       
#  ____   ____  _       _______     _____       _       ______   _____     ________   ______   
# |_  _| |_  _|/ \     |_   __ \   |_   _|     / \     |_   _ \ |_   _|   |_   __  |.' ____ \  
#   \ \   / / / _ \      | |__) |    | |      / _ \      | |_) |  | |       | |_ \_|| (___ \_| 
#    \ \ / / / ___ \     |  __ /     | |     / ___ \     |  __'.  | |   _   |  _| _  _.____`.  
#     \ ' /_/ /   \ \_  _| |  \ \_  _| |_  _/ /   \ \_  _| |__) |_| |__/ | _| |__/ || \____) | 
#      \_/|____| |____||____| |___||_____||____| |____||_______/|________||________| \______.' 


#DEPLACEMENT
LEFT = False;
RIGHT = False;
UP = False;
DOWN = False;



#DEFINITION D'ECRAN
w,h = 900,900;
SCREEN = pygame.display.set_mode((w,h));
HIT = False


#BACKGROUND
BG = pygame.image.load("asset/bg.png");
BG = pygame.transform.scale(BG,(w,h))
BG_hitbox = BG.get_rect();



#PACMANANIMATED
frame = 0
player = pygame.image.load("asset/2.png")
player = pygame.transform.scale(player,(40,40))
player_hitbox = player.get_rect();
player_hitbox.center = w//2,340





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
    pygame.image.load("asset/pg.png")
]

ON_COIN = False
POINT = 0
pacgumHit = []

distance = 30

#     ______      _      ____    ____ ________  
#   .' ___  |    / \    |_   \  /   _|_   __  | 
#  / .'   \_|   / _ \     |   \/   |   | |_ \_| 
#  | |   ____  / ___ \    | |\  /| |   |  _| _  
#  \ `.___]  _/ /   \ \_ _| |_\/_| |_ _| |__/ | 
#   `._____.|____| |____|_____||_____|________| 
#                                                                                      

while (True):    
    MOUSEX,MOUSEY = pygame.mouse.get_pos()

    frame +=1
    if frame <= 50:
        player = pygame.image.load("asset/2.png");
        player = pygame.transform.scale(player,(40,40))
    if frame >50:
        player = pygame.image.load("asset/1.png")
        player = pygame.transform.scale(player,(40,40))
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
            player = pygame.image.load("asset/1.png")
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
            if event.key == pygame.K_SPACE:
                pygame.quit()

#               __  __   _         _                       
#              [  |[  | (_)       (_)                      
#   .---.  .--. | | | | __  .--.  __  .--.  _ .--.  .--.   
#  / /'`\/ .'`\ | | | |[  |( (`\][  / .'`\ [ `.-. |( (`\]  
#  | \__.| \__. | | | | | | `'.'. | | \__. || | | | `'.'.  
#  '.___.''.__.[___[___[___[\__) [___'.__.'[___||__[\__) ) 
#                                                         

    #TOP COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.centerx,player_hitbox.top -5))
    if colorb == 255:
        player_hitbox.y += 1
        UP = False
    #LEFT COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.left -5,player_hitbox.centery))
    if colorb == 255:
        player_hitbox.x += 1
        LEFT = False
    #RIGHT COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.right+5,player_hitbox.centery))
    if colorb == 255:
        player_hitbox.x -= 1
        RIGHT = False
    #BOTTOM COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.centerx,player_hitbox.bottom +5))
    if colorb == 255:
        player_hitbox.y -= 1
        BOTTOM = False

    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.centerx,player_hitbox.centery))
    if colorr == 237:
        ON_COIN = True
    else:
        ON_COIN = False



    SCREEN.blit(BG, BG_hitbox)
    SCREEN.blit(player, player_hitbox)
    
    for each in range(len(pacgumarray)):
        if (each <=4):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//2.9+(each*70),h//2.65
            SCREEN.blit(pacgumarray[each],pacgumHit[each])
        if (each > 4 and each <10):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//2.9+((each-5)*70),h//1.78
            SCREEN.blit(pacgumarray[each],pacgumHit[each])
        if (each == 10):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//2.9,h//2.15
            SCREEN.blit(pacgumarray[each],pacgumHit[each])
        if (each == 11):
            pacgumHit.append(pacgumarray[each].get_rect())
            pacgumHit[each].center = w//1.52,h//2.15
            SCREEN.blit(pacgumarray[each],pacgumHit[each])

    if ((POINT//2) == len(pacgumarray)):
        pygame.quit()
    
    if (ON_COIN):
        POINT += 1

    #PACGUM
    for each in range(len(pacgumarray)):
        if (player_hitbox.colliderect(pacgumHit[each]) and ON_COIN == True ):
            ON_COIN = False
            pacgumarray[each].set_alpha(0)

    pygame.display.update()