import math
import random
import pygame
from pygame import mixer
import time

# starts pygame
pygame.init()

# screen
screen = pygame.display.set_mode((800, 500))

# main menu and game over screen
game_over = pygame.image.load('game over screen.png')

# gun variables
gunx = 375
guny = 225
# game state, menu, actual game, sub-menu
game_state = 'menu'

# gun images and effects
gun_image = pygame.image.load('dhis_muzzleflash_sized.png')
gun_image_fired = pygame.image.load('dhis570pixmuzzle size muzzle falsh transparent.png')
boom_effect = pygame.image.load('explosion (1).png')

# ball iamges
ball_img = pygame.image.load('Red ball.png')
ball_pop_1 = pygame.image.load('ball pop 1.png')
ball_pop_2 = pygame.image.load('ball pop 2.png')

# music and sounds
gun_sound = 'none'
music = pygame.mixer.music.load('Bhonchenchapo Background.wav')

# score 
score = 0
font = pygame.font.Font('Minecraft.ttf',32)
textx = 50
texty = 50

# enemies and lives
global num_enemies
num_enemies = 3
lives = 10
lives_img = pygame.image.load('bullet life.png')
enemy_adding_value = 2
hardening_value = score/10
next_hardening_value = 1
b = 2

# varibale for harder games
a = 1

# gun shot delay variable
flow = 0

#speed variables
speeda = 2
speedb = 3

# logo and caption
logo_icon = pygame.image.load('dhis_muzzleflash_sized.png')
pygame.display.set_icon(logo_icon)
pygame.display.set_caption('Dhiskew!!')

# ball varibales
ballx = random.randint(-600,0)
bally = random.randint(200,400)
#------
ballx = []
bally = []
speeds = []
ball_images = []
animation_time = []

# loop for assigning the first position of the ball
for i in range(num_enemies):
    x = random.randint(1, 20)
    if x < 6:
        ballx.append(random.randint(-700, 0))
        bally.append(random.randint(200,400))
    elif x < 11:
        ballx.append(random.randint(800, 1500))
        bally.append(random.randint(200,400))
    elif x <  16:
        ballx.append(random.randint(100, 400))
        bally.append(random.randint(-700, 0))
    elif x < 21:
        ballx.append(random.randint(100, 400))
        bally.append(random.randint(500, 1200))
    
    ball_images.append(ball_img)
    animation_time.append(30)
    speeds.append(random.uniform(speeda,speedb))

# function for collision

def collision():
    distance_cx = abs(mx - (ballx[i] +37))
    distance_cy = abs(my - (bally[i]  + 30))
    global distance_c
    distance_c = math.sqrt(math.pow((distance_cx+distance_cy), 2))

    # ball collision
    distance_bx = abs(gunx - (ballx[i] -5))
    distance_by = abs(guny - (bally[i] -5))
    distance_B = math.sqrt(math.pow((distance_bx+distance_by), 2))

    if pygame.mouse.get_pressed() == (1, 0, 0) and distance_c < 30 and flow > 230 and distance_B > 24:
        return True
    elif distance_B < 24:
        return False
    else:
        return False

 


# music play
# pygame.mixer.music.play(-1)

# event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        
    
    # loop for assigning the first position of the ball
    for i in range(num_enemies):
        x = random.randint(1, 20)
        if x < 6:
            ballx.append(random.randint(-700, 0))
            bally.append(random.randint(200,400))
        elif x < 11:
            ballx.append(random.randint(800, 1500))
            bally.append(random.randint(200,400))
        elif x <  16:
            ballx.append(random.randint(100, 400))
            bally.append(random.randint(-700, 0))
        elif x < 21:
            ballx.append(random.randint(100, 400))
            bally.append(random.randint(500, 1200))
        
        ball_images.append(ball_img)
        animation_time.append(30)
        speeds.append(random.uniform(speeda,speedb))
        
    
    
    
    # things to do when still alive
    if lives > 0 and game_state == 'play' and gun_sound!= 'none':

        # screen colour
        screen.fill((255, 255, 255))
        
        mx, my = pygame.mouse.get_pos()

        # when to show gun fired and play dhiskew

        if pygame.mouse.get_pressed() == (1, 0, 0) and flow == 0:
            flow += 250
            
        if 0 != flow:
            flow -= 1
            
        if pygame.mouse.get_pressed() == (1, 0, 0) and flow > 230:
            gun_image_show = gun_image_fired
            gun_sound.play()
        else:
            gun_image_show = gun_image
        
        # ball movement
        # distance part
        for i in range(num_enemies):
            
            # ball animation 
            if animation_time[i] > 15 and animation_time[i] < 24:
                ball_images[i] = ball_pop_1
            elif animation_time[i] > 0 and animation_time[i] < 14:
                ball_images[i] = ball_pop_2
            else:                    
                ball_images[i] = ball_img
            
            
            screen.blit(ball_images[i], (ballx[i] , bally[i] ))

            
            distancex, distancey = ballx[i]  - (gunx + 9), bally[i]  - (guny+8)
            distance = math.sqrt(math.pow(abs(distancex) + abs(distancey), 2))
            if distancex == 0:
                distancex += 1
            else:
                distancex = distancex
            movement_pixels = distancey / distancex
            
            x = random.randint(1, 10)
            speed_y_limit = random.uniform(speeda + 1, speedb + 1)
            speed_y_limit_n = 2/ speed_y_limit

            if distance > 5:
        
                
                #speed calculations
                speedx = 1/speeds[i] 
                speedy =  abs(movement_pixels) * (1 / speeds[i])
                speed_need = speedy/speed_y_limit_n
                
                if  speed_y_limit_n < speedy:
                    speedy = speedy/speed_need
                    speedx  = speedx/speed_need
                
                
                
                # movement based on position
                if distancex < 0:
                    ballx[i] += speedx
                else:
                    ballx[i] -= speedx
                if distancey < 0:
                    bally[i] += speedy
                else:
                    bally[i] -= speedy
            
            

                    


            # collision part
            
            if collision():
                
                x = random.randint(1,20)
                if x < 6:
                    ballx[i]=(random.randint(-700, -499))
                    bally[i]=(random.randint(200,400))
                elif x < 11:
                    ballx[i]=(random.randint(1100, 1500))
                    bally[i]=(random.randint(200,400))
                elif x < 16:
                    ballx[i]=(random.randint(100, 800))
                    bally[i]=(random.randint(-700, -400))
                elif x < 21:
                    ballx[i]=(random.randint(100, 400))
                    bally[i]=(random.randint(931, 1200))
                score+=1

                
            # whether ball hit the gun or not
            distance_bx = abs(gunx - (ballx[i] -5))
            distance_by = abs(guny - (bally[i] -5))
            distance_B = math.sqrt(math.pow((distance_bx+distance_by), 2))
            
            if distance_B < 24:
                x = random.randint(1,20)
                
                animation_time[i] -=1
                if animation_time[i] == 0:
                    
                    if x < 6:
                        ballx[i]=(random.randint(-700, -499))
                        bally[i]=(random.randint(200,400))
                    elif x < 11:
                        ballx[i]=(random.randint(1100, 1500))
                        bally[i]=(random.randint(200,400))
                    elif x < 16:
                        ballx[i]=(random.randint(100, 800))
                        bally[i]=(random.randint(-700, -400))
                    elif x < 21:
                        ballx[i]=(random.randint(100, 400))
                        bally[i]=(random.randint(931, 1200))
                    lives -=1
                    animation_time[i]+=30
            
            # score placement
            score_text =font.render(str(score), True, (0,0,0))
            screen.blit(score_text, (textx,texty))
    
            # progressively hardening the game
            hardening_value = score/10

            
            if hardening_value == next_hardening_value:
                next_hardening_value = 1
                next_hardening_value = next_hardening_value + a
                speeda -= 0.2
                speedb -= 0.2
                a += 1
                if (a-1) == enemy_adding_value:
                    enemy_adding_value = 2
                    enemy_adding_value * b
                    b+=1
                    num_enemies+=1

            
                
            
        # draws the lives
        for i in range(lives):
            screen.blit(lives_img, (780 - ((i+1)*25 ),20))

        


        # distance part
        x_dis = abs(gunx - mx) + 0.1
        y_dis = abs(guny - my) + 0.1

        # angle finder
        if mx > gunx and my < guny:
            gun_degree1 = math.degrees(math.atan(y_dis / x_dis))
        elif mx < gunx and my < guny:
            gun_degree1 = 180 - (math.degrees(math.atan(y_dis / x_dis)))
        elif mx < gunx and my > guny:
            gun_degree1 = (math.degrees(math.atan(y_dis / x_dis))) + 180
        elif mx > gunx and my > guny:
            gun_degree1 = 360 - (math.degrees(math.atan(y_dis / x_dis)))
        else:
            gun_degree1 = 0

        # draws the gun

        rotated_gun = pygame.transform.rotate(gun_image_show, gun_degree1)
        screen.blit(rotated_gun, (gunx, guny))
        

        # boom effect
        if pygame.mouse.get_pressed() == (1, 0, 0) and flow > 230:
            screen.blit(boom_effect, (mx - 27, my - 25))
    

        pygame.display.update()
    
    
    # when dead    
    elif game_state == 'play' and lives == 0:
        # screen
        screen.fill((255,255,255))
        # font renders
        font = pygame.font.Font('Minecraft.ttf',96)
        end_text = font.render(('You died dummy'), True, (255,0,0))
        end_text_2 = font.render(('Your score is : ' ), True, (255,0,0))
        score_text = font.render(str(score), True, (255,0,0))
        # font drawings
        screen.blit(end_text,(30,100))
        screen.blit(end_text_2, (30,216))
        screen.blit(score_text,(350,325))
        pygame.display.update()
        time.sleep(5)
        break
        
    # main menu drawn
    elif game_state == 'menu':
        # main menu drawn
        menu = pygame.image.load('Main_menu.png')
        screen.blit(menu, (0,0))
        
        # extra varibales
        mx, my = pygame.mouse.get_pos()

        # if clicked
        # play game button
        play_game = pygame.image.load('play_diskew_main_menu_interacted.png')
        
        if mx > 109 and mx < 646 and my > 330 and my < 396:
            screen.blit(play_game,(110,332))

        # sound buttons
        sound_1 = pygame.image.load('sound option 1 interacted.png')
        sound_2 = pygame.image.load('sound option 2 interacted (1).png')    
        
        if mx > 680 and mx < 750 and my > 33 and my < 92:
            screen.blit(sound_1, (678,25))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                gun_sound = mixer.Sound('Shaans suggestion.mp3')
            
                
        elif mx > 680 and mx < 750 and my > 110 and my < 172:
            screen.blit(sound_2, (679,105))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                gun_sound = mixer.Sound('Raiyans Suggestion.mp3')
        
        if gun_sound!= 'none' and pygame.mouse.get_pressed() == (1, 0, 0) and mx > 109 and mx < 646 and my > 330 and my < 396:
            game_state = 'play'
        
        # highscore showing
        highscores = []
        highscore_s = open('highscore.txt','r')
        highscore_show = highscore_s.read().splitlines()
        for i in highscore_show:
            highscores.extend(i.split())
        for i in range(len(highscores)):
            highscores[i] = int(highscores[i])
        highest_score = max(highscores)
        # writing the score
        font = pygame.font.Font('Minecraft.ttf',48)
        highscores_text = font.render(('Highscore:' + str(highest_score)), True, (0,0,0))
        screen.blit(highscores_text, (0,0))

        pygame.display.update()




# storing the highscore 
store_score = open('highscore.txt','a')    
store_score.write(str(score)+ ' ')
