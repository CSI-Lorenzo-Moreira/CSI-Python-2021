import time
import pygame
import random
pygame.init()

red =(255,0,0)
green =(0,255,0)
black =(0,0,0)
blue =(91,57,250)
silver =(192, 192, 192)
dis_width =800
dis_height=600

dis=pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("this is the greatest snake of all time")
game_over=False

snake_block = 20
snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 25)

def my_Score(score):
    value = score_font.render("Your score:"+str(score), True,black)
    dis.blit(value,[0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3.5, dis_height/2])

def gameRestart():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_List=[]
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20) *20
    foody = round(random.randrange(0, dis_width - snake_block) / 20) *20


    while not game_over:
        while game_close == True:
            dis.fill(black)
            message("L. Wanna play again? Y/N", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_y:
                        gameRestart()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(silver)  
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block]) 
        my_Score(length_of_snake-1)    
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[: -1]:
            if x == snake_Head:
                game_close = True

        
        our_snake(snake_block, snake_List)

        pygame.display.update()   

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20) * 20
            foody = round(random.randrange(0, dis_height - snake_block) / 20) * 20
            length_of_snake += 1

        clock.tick(snake_speed) 

    pygame.quit()
    quit()

gameRestart()