from numpy import place
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


#BACKGROUND
BG = pygame.image.load("asset/bg.png");
BG = pygame.transform.scale(BG,(w,h))
BG_hitbox = BG.get_rect();


#PACMAN
player = pygame.image.load("asset/2.png");
player = pygame.transform.scale(player,(50,50))
player_hitbox = player.get_rect();
player_hitbox.center = w//3,340


#MURS 18
collider = [
    pygame.Rect(0,0,900,35),
    pygame.Rect(25,25,25,25),
    ]



#     ______      _      ____    ____ ________  
#   .' ___  |    / \    |_   \  /   _|_   __  | 
#  / .'   \_|   / _ \     |   \/   |   | |_ \_| 
#  | |   ____  / ___ \    | |\  /| |   |  _| _  
#  \ `.___]  _/ /   \ \_ _| |_\/_| |_ _| |__/ | 
#   `._____.|____| |____|_____||_____|________| 
#                                                                                      

while (True):

#                                                                  _         
#                                                                 / |_       
#   _ .--..--.  .--.  __   _ _   __ .---. _ .--..--. .---. _ .--.`| |-.--.   
#  [ `.-. .-. / .'`\ [  | | [ \ [  / /__\[ `.-. .-. / /__\[ `.-. || |( (`\]  
#   | | | | | | \__. || \_/ |\ \/ /| \__.,| | | | | | \__.,| | | || |,`'.'.  
#  [___||__||__'.__.' '.__.'_/\__/  '.__.[___||__||__'.__.[___||__\__[\__) ) 
#                                                                            
    
    if (UP):
        player_hitbox.y -= 1
    if (DOWN):
        player_hitbox.y += 1
    if (LEFT):
        player_hitbox.x -= 1
    if (RIGHT):
        player_hitbox.x += 1

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

    i=0
    if collider[i].collidedict(player_hitbox.top):
       UP = False
    if i > len(collider):
        i = 0
    i+=1
    

    
    SCREEN.blit(BG, BG_hitbox)
    SCREEN.blit(player, player_hitbox)
    pygame.draw.rect(SCREEN,(255,0,0),collider[0])
    pygame.draw.rect(player,(255,255,255),(0,0,50,50))
    pygame.display.update()




