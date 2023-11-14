import pygame, time, sys

print(pygame.font.get_fonts())

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)



with open("highscores.txt","r") as highscores:
    for line in highscores:
        print(line)


    
rally=0
highscore=0

speed=1
stopTimer=False

pygame.font.init()
font = pygame.font.Font(None, 36)

username=""

usr_inp_rect = pygame.Rect(100, 150, 320, 50)
active = False

x=350
y=250
x_offset=1
y_offset=-1

scoreA=0
scoreB=0

y_paddleA=230
y_paddleB=230

state="menu"

up1=False
down1=False
up2=False
down2=False

PI=3.141592653589793
 
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()


while not done:
    
    
    for event in pygame.event.get():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        
            
    if state=="menu":
        username=input("Enter name: ")
        username=username+"\n"
        with open("usernames.txt", "a+") as usernames:
            usernames.write(str(username))
            
        state="highscores"
        
        pygame.display.flip()

        clock.tick(60)

    elif state=="highscores":
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    state="game"
        
        
        font = pygame.font.SysFont('lemon', 40, True, False)
        text = font.render(("Highscores: "),True,WHITE)
        screen.blit(text, [240, 10])
        
        y_name=20
        y_score=20

        with open("highscores.txt", "r") as highscores:
            for line in highscores:
                y_score+=50
                text = font.render((str(line)),True,WHITE)
                screen.blit(text, [400, y_score])
        
        
        with open("usernames.txt", "r") as usernames:
            for line in usernames:
                y_name+=50
                text = font.render((str(line)),True,WHITE)
                screen.blit(text, [120, y_name])

        pygame.display.flip()        
        clock.tick(60)

        e=input()
        state="game"

            
    elif state=="game":

        if event.type == pygame.QUIT:
                done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up1=True
            elif event.key == pygame.K_s:
                down1=True
            elif event.key == pygame.K_UP:
                up2=True
            elif event.key == pygame.K_DOWN:
                down2=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up1=False
            if event.key == pygame.K_s:
                down1=False
            if event.key == pygame.K_UP:
                up2=False
            if event.key == pygame.K_DOWN:
                down2=False

            
                       

        if (x>=670 and x<=680) and ((y_paddleB<=y) and ((y_paddleB+80)>=y)): 
            x_offset=x_offset*-1
            rally+=1
        if (x<=10):
        #and ((y_paddleA<=y) and ((y_paddleA+80)>=y)):
            x_offset=x_offset*-1
            speed+=0.1
        #if x<=5:
                
         #   scoreB+=1
          #  x=350
           # y=250
            #stopTimer=True
            #time.sleep(1)
        if x>=695:
            scoreA+=1
            rally=0
                
            x=350
            y=250
            stopTimer=True
            #time.sleep(1)
        if y>=490 or y<=10:
            y_offset=y_offset*-1
          
        screen.fill(BLACK)
            
        font = pygame.font.SysFont('lemon', 40, True, False)
        text = font.render(str(rally),True,WHITE)
        screen.blit(text, [160, 10])

        text = font.render("Highscore:" ,True,WHITE)
        screen.blit(text, [300, 10])
        
        text = font.render(str(highscore),True,WHITE)
        screen.blit(text, [560, 10])

        #text = font.render(str(scoreB),True,WHITE)
        #screen.blit(text, [450, 10])
                
         
        pygame.draw.circle(screen, WHITE, [x,y], 10)
        #pygame.draw.rect(screen, WHITE, [10,y-40,10,80],0)
        pygame.draw.rect(screen, WHITE, [680,y_paddleB,10,80],0)
           
         
        pygame.display.flip()
         
        clock.tick(60)

        x=x+(x_offset*5*speed)
        y=y+(y_offset*5*speed)

        #if up1==True and y_paddleA>0:
        #    y_paddleA-=5
        #elif down1==True and y_paddleA<=420:
        #    y_paddleA+=5
        if up2==True and y_paddleB>0:
            y_paddleB-=5
        elif down2==True and y_paddleB<=420:
            y_paddleB+=5

            #if (x>=345 and x<=355) and (y>=245 and y<=255):
             #   time.sleep(1)

        if stopTimer:
            time.sleep(1)
            stopTimer=False
            speed=1

            #if scoreA==5 or scoreB==5:
     
        #y_paddleA=y-40

        if rally>highscore:
            highscore=rally
print(highscore)
with open("highscores.txt", "a+") as highscores:
    highscore=str(str(highscore)+"\n")
    highscores.write(str(highscore))
    

 
# Close the window and quit.
pygame.quit()

usernames.close()
highscores.close()
