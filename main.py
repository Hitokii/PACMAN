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


#PACMAN
player = pygame.image.load("asset/2.png");
player = pygame.transform.scale(player,(40,40))
player_hitbox = player.get_rect();
player_hitbox.center = w//3,340






#MURS 18
#collider = [
#    #MUR PRINCIPAUX
#    pygame.Rect(0,0,900,35),
#    pygame.Rect(0,0,35,395),
#    pygame.Rect(0,460,35,500),
#    pygame.Rect(870,0,35,395),
#    pygame.Rect(870,460,35,500),
#    pygame.Rect(0,870,900,35),
#    pygame.Rect(0,870,900,35),
#    #PLATFORM
#    pygame.Rect(90,84,97,55),
#    pygame.Rect(250,84,120,60),
#    pygame.Rect(95,195,93,30),
#    pygame.Rect(720,195,93,30),
#    ]

empty_square = pygame.Rect(-50,-50,1,1)
current_collision = empty_square

#     ______      _      ____    ____ ________  
#   .' ___  |    / \    |_   \  /   _|_   __  | 
#  / .'   \_|   / _ \     |   \/   |   | |_ \_| 
#  | |   ____  / ___ \    | |\  /| |   |  _| _  
#  \ `.___]  _/ /   \ \_ _| |_\/_| |_ _| |__/ | 
#   `._____.|____| |____|_____||_____|________| 
#                                                                                      

while (True):
    
    MOUSEX,MOUSEY = pygame.mouse.get_pos()


#                                                                  _         
#                                                                 / |_       
#   _ .--..--.  .--.  __   _ _   __ .---. _ .--..--. .---. _ .--.`| |-.--.   
#  [ `.-. .-. / .'`\ [  | | [ \ [  / /__\[ `.-. .-. / /__\[ `.-. || |( (`\]  
#   | | | | | | \__. || \_/ |\ \/ /| \__.,| | | | | | \__.,| | | || |,`'.'.  
#  [___||__||__'.__.' '.__.'_/\__/  '.__.[___||__||__'.__.[___||__\__[\__) ) 
#                                                                            
    
    if (UP):
        player_hitbox.y -= 1
        player = pygame.image.load("asset/2.png");
        player = pygame.transform.scale(player,(40,40))
        player = pygame.transform.rotate(player,90)
    if (DOWN):
        player_hitbox.y += 1
        player = pygame.image.load("asset/2.png");
        player = pygame.transform.scale(player,(40,40))
        player = pygame.transform.rotate(player,-90)
    if (LEFT):
        player_hitbox.x -= 1
        player = pygame.image.load("asset/2.png");
        player = pygame.transform.scale(player,(40,40))
        player = pygame.transform.rotate(player,180)
    if (RIGHT):
        player_hitbox.x += 1
        player = pygame.image.load("asset/2.png");
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

#               __  __   _         _                       
#              [  |[  | (_)       (_)                      
#   .---.  .--. | | | | __  .--.  __  .--.  _ .--.  .--.   
#  / /'`\/ .'`\ | | | |[  |( (`\][  / .'`\ [ `.-. |( (`\]  
#  | \__.| \__. | | | | | | `'.'. | | \__. || | | | `'.'.  
#  '.___.''.__.[___[___[___[\__) [___'.__.'[___||__[\__) ) 
#                                                         

    #TOP COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.centerx,player_hitbox.top))
    if colorb == 255:
        player_hitbox.y += 1
        UP = False
    #LEFT COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.left,player_hitbox.centery))
    if colorb == 255:
        player_hitbox.x += 1
        LEFT = False
    #RIGHT COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.right,player_hitbox.centery))
    if colorb == 255:
        player_hitbox.x -= 1
        RIGHT = False
    #BOTTOM COLOR
    colorr,colorg,colorb,colora = pygame.Surface.get_at(SCREEN,(player_hitbox.centerx,player_hitbox.bottom))
    if colorb == 255:
        player_hitbox.y -= 1
        BOTTOM = False





    
    SCREEN.blit(BG, BG_hitbox)
    SCREEN.blit(player, player_hitbox)

#    if (HIT):
#        pygame.draw.rect(player,(255,255,255),(0,0,50,50))
#        for each in range(len(collider)):
#            pygame.draw.rect(SCREEN,(255,0,0),collider[each])


    pygame.display.update()




