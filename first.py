import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

x=550
y=50
direction=-1

PI=3.141592653589793
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if x==50:
        direction=1
    if x==650:
        direction=-1
     
    # --- Game logic should go here
   
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)
 
    # --- Drawing code should go here

    # Draw a rectangle
    pygame.draw.rect(screen,GREEN,[0,300,250,250],0)
    pygame.draw.rect(screen,GREEN,[450,300,250,250],0)
    pygame.draw.rect(screen,BLACK,[250,200,200,300],6)
    pygame.draw.rect(screen,BLACK,[275,225,50,50],5)
    pygame.draw.rect(screen,BLACK,[375,225,50,50],5)
    pygame.draw.rect(screen,BLACK,[325,400,50,100],5)
    pygame.draw.polygon(screen, BLACK, [[444,200],[254,200],[350,100], ], 10)
    # Draw a circle
    pygame.draw.circle(screen, YELLOW, [x,y], 30)
    #pygame.draw.arc(screen, GREEN, [100,100,250,200],  PI/2,     PI, 2)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

    x=x+(direction*2)
    y=(((x-330)**2)*0.001)+50
   
 
# Close the window and quit.
pygame.quit()
