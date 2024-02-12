import pygame
import time
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
violet=(148,0,211)
green=(0,255,0)
bright_green=(0,255,0)
bright_red=(255,0,0)

dis_width=600
dis_height=400
dis=pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake game") #nosaukums

clock = pygame.time.Clock()

snake_block=10
snake_speed=15

font_style = pygame.font.SysFont("times new roman",25)
font_style = pygame.font.SysFont("comicsansms",35)
        
def your_score(score):
  value = font_style.render("Your score: " +str (score), True, blue)
  score_rect = value.get_rect()
  dis.blit(value, score_rect)

def text_objects(text, font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()

  if x + w > mouse[0] > x and y + h > mouse[1] > y:
    pygame.draw.rect(dis, ac, (x,y,w,h))
    if click[0] == 1 and action !=None:
      action()
  else:
    pygame.draw.rect(dis, ic, (x,y,w,h))
  
  smallText = pygame.font.SysFont("comicsansms",20)
  textSurf, textRect = text_objects(msg, smallText)
  textRect.center = ( (x+(w/2)), (y+(h/2)) )
  dis.blit(textSurf, textRect)
  

def unpause():
  global pause
  pause=False

def quitgame():
  pygame.quit()
  quit()

def our_snake(snake_block, snake_list):
  for x in snake_list:
    pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width/ 6, dis_height/ 3])



    button("Continue",150,450,100,50,green,bright_green,unpause)
    button("Quit",350,450,100,50,red,bright_red,quitgame)

pygame.display.update()
clock.tick(15)

def crash():

  largeText = pygame.font.SysFont("comicsansms",115)
  TextSurf, TextRect = text_objects("You crashed", largeText)
  TextRect.center = ((dis_width/2),(dis_height/2))
  dis.blit(TextSurf,TextRect)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    button("Play again",150,450,100,50,green,bright_green,game_loop)
    button("Quit",550,450,100,50,red,bright_red,quitgame)

    pygame.display.update()
    clock.tick(15)

def gameloop():
  game_over=False
  game_close=False

  x1=dis_width/ 2
  y1=dis_height/ 2

  x1_change=0
  y1_change=0

  snake_list=[]
  length_of_snake=1

  foodx=round(random.randrange(1,dis_width // 10)) * 10
  foody=round(random.randrange(1,dis_height // 10)) * 10

  food_spawn=True
  while not game_over:

    while game_close==True:
      dis.fill(black)
      message("You lost! Press Q-Quit or C-Play again", red)
      your_score(length_of_snake - 1)
      pygame.display.update()


      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            game_over=True
            game_close=False
          if event.key == pygame.K_c:
            gameloop()

    
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        game_over=True
      if paused == True:
        time.sleep(1)
      if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
          x1_change = -snake_block
          y1_change = 0
        elif event.key==pygame.K_RIGHT:
          x1_change = snake_block
          y1_change = 0
        elif event.key==pygame.K_UP:
          y1_change = -snake_block
          x1_change = 0
        elif event.key==pygame.K_DOWN:
          y1_change = snake_block
          x1_change = 0
        if event.key==pygame.K_p:
          paused = True
        if event.key==pygame.K_u:
          paused = False
          
    
    pygame.display.update()

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
      game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(black)
    pygame.draw.rect(dis, violet, [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > (length_of_snake):
      del snake_list[0]

    for x in snake_list[: -1]:
      if x == snake_head:
        game_close = True

    our_snake(snake_block, snake_list)
    your_score(length_of_snake - 1)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
      foodx = round(random.randrange(1, dis_width // 10)) * 10
      foody = round(random.randrange(1, dis_height // 10)) * 10
      food_spawn = False
      length_of_snake += 2

    clock.tick(snake_speed)
    pygame.display.update() 

  pygame.quit()
  quit()

gameloop()